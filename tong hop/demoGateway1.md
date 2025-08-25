# ===============================
# SMTP AI Gateway Demo – Python Skeleton
# FastAPI + WebSocket + SQLite/In-Memory Inbox + Naive Bayes (stub) + LLM (stub)
# ===============================
# Project layout (single file for demo; split into modules in real project):
# - config: settings & feature flags
# - models: Pydantic schemas
# - storage: Inbox (SQLite or in-memory)
# - filters.naive_bayes: placeholder train/predict
# - filters.llm: provider-agnostic LLM call stubs (OpenAI/OpenRouter/Grok)
# - filters.policy: decision orchestration (NB -> LLM on suspicion)
# - gateway: FastAPI app with HTTP + WebSocket endpoints
# - run: Uvicorn entrypoint
# ===============================

from __future__ import annotations

import asyncio
import json
import logging
import os
import queue
import sqlite3
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# -------------------------------
# config
# -------------------------------
class Settings(BaseModel):
    app_name: str = "smtp-ai-gateway-demo"
    use_sqlite: bool = False  # switch to True to persist inbox
    sqlite_path: str = "/tmp/inbox.db"
    enable_ws: bool = True

    # Naive Bayes thresholds (stub)
    nb_suspicious_threshold: float = 0.6  # >= triggers LLM

    # LLM providers (only one needs to be configured; all are optional in skeleton)
    llm_provider: str = "openai"  # openai | openrouter | grok
    openai_api_key: Optional[str] = None
    openrouter_api_key: Optional[str] = None
    grok_api_key: Optional[str] = None

    # Safety / demo flags
    allow_external_llm_calls: bool = False  # keep False in skeleton


SETTINGS = Settings()

# -------------------------------
# models (schemas)
# -------------------------------
class Message(BaseModel):
    sender: str = Field(..., description="email-like identifier of sender")
    receiver: str = Field(..., description="email-like identifier of receiver")
    subject: str = Field("", description="message subject")
    body: str = Field(..., description="message body text (no HTML in demo)")
    thread_id: Optional[str] = Field(None, description="conversation/thread id")
    timestamp: float = Field(default_factory=lambda: time.time())


class ClassifiedMessage(Message):
    nb_score: float = 0.0
    llm_verdict: Optional[str] = None  # "ok" | "scam" | None
    decision: str = "delivered"  # delivered | flagged | blocked
    reason: Optional[str] = None


class TrainItem(BaseModel):
    text: str
    label: str  # "legit" | "phishing" | "bec"


class TrainSet(BaseModel):
    items: List[TrainItem]


# -------------------------------
# utils: simple preprocessing (stub)
# -------------------------------
class TextPreprocessor:
    @staticmethod
    def normalize(text: str) -> str:
        # TODO: lowercase, strip diacritics, remove HTML, collapse whitespace, etc.
        return " ".join(text.lower().split())


# -------------------------------
# storage: Inbox implementations
# -------------------------------
class InboxBase:
    def save(self, msg: ClassifiedMessage) -> None:
        raise NotImplementedError

    def list(self, limit: int = 100) -> List[ClassifiedMessage]:
        raise NotImplementedError


class InMemoryInbox(InboxBase):
    def __init__(self) -> None:
        self._msgs: List[ClassifiedMessage] = []

    def save(self, msg: ClassifiedMessage) -> None:
        self._msgs.append(msg)

    def list(self, limit: int = 100) -> List[ClassifiedMessage]:
        return list(reversed(self._msgs))[:limit]


class SQLiteInbox(InboxBase):
    def __init__(self, path: str) -> None:
        self._conn = sqlite3.connect(path, check_same_thread=False)
        self._init_schema()

    def _init_schema(self) -> None:
        cur = self._conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS inbox(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                json TEXT NOT NULL,
                ts REAL NOT NULL
            )
            """
        )
        self._conn.commit()

    def save(self, msg: ClassifiedMessage) -> None:
        cur = self._conn.cursor()
        cur.execute(
            "INSERT INTO inbox(json, ts) VALUES(?, ?)",
            (msg.json(), msg.timestamp),
        )
        self._conn.commit()

    def list(self, limit: int = 100) -> List[ClassifiedMessage]:
        cur = self._conn.cursor()
        cur.execute("SELECT json FROM inbox ORDER BY id DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        out: List[ClassifiedMessage] = []
        for (j,) in rows:
            out.append(ClassifiedMessage.parse_raw(j))
        return out


# Dependency factory
INBOX: InboxBase = SQLiteInbox(SETTINGS.sqlite_path) if SETTINGS.use_sqlite else InMemoryInbox()


# -------------------------------
# filters: Naive Bayes (stub)
# -------------------------------
class NaiveBayesFilter:
    """Skeleton NB classifier. In real code, store vocabulary, priors, likelihoods.
    Here we return a heuristic score for demo purposes.
    """

    def __init__(self) -> None:
        self.trained = False
        self.keywords_suspicious = {
            "chuyển khoản", "tài khoản mới", "khẩn", "gấp", "invoice", "bank", "swift",
            "update account", "wire", "urgent", "gift card", "otp", "reset password",
        }

    def train(self, dataset: TrainSet) -> None:
        # TODO: build vocabulary, compute P(class), P(token|class)
        self.trained = True

    def predict_proba(self, text: str) -> float:
        """Return probability that text is suspicious (0..1). Pure heuristic for skeleton."""
        if not self.trained:
            # Conservative default if not trained
            return 0.5
        norm = TextPreprocessor.normalize(text)
        tokens = set(norm.split())
        hit = len(tokens & self.keywords_suspicious)
        # Map keyword hits to a crude probability
        return min(1.0, 0.2 + 0.15 * hit)


NB_FILTER = NaiveBayesFilter()


# -------------------------------
# filters: LLM Analyzer (provider-agnostic stubs)
# -------------------------------
class LLMVerdict(str, Enum):
    ok = "ok"
    scam = "scam"
    uncertain = "uncertain"


class LLMAnalyzer:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def analyze(self, msg: Message, nb_score: float) -> LLMVerdict:
        """Skeleton: call out to provider or return deterministic local verdict.
        Do NOT send data to external API unless allow_external_llm_calls=True.
        """
        prompt = self._build_prompt(msg, nb_score)
        if not self.settings.allow_external_llm_calls:
            # Local heuristic fallback for demo
            if nb_score >= 0.85:
                return LLMVerdict.scam
            if nb_score >= 0.6:
                return LLMVerdict.uncertain
            return LLMVerdict.ok
        # Otherwise, pick provider
        provider = (self.settings.llm_provider or "openai").lower()
        if provider == "openrouter":
            return await self._call_openrouter(prompt)
        if provider == "grok":
            return await self._call_grok(prompt)
        return await self._call_openai(prompt)

    def _build_prompt(self, msg: Message, nb_score: float) -> str:
        return (
            "You are an email security analyst. Classify the following message as 'ok' or 'scam'\n"
            f"NB_suspicion_score: {nb_score}\n"
            f"From: {msg.sender}\nTo: {msg.receiver}\nSubject: {msg.subject}\nBody: {msg.body}\n"
            "Explain briefly and output a single token label: ok or scam."
        )

    async def _call_openai(self, prompt: str) -> LLMVerdict:
        # TODO: implement with openai SDK
        # Placeholder behavior
        await asyncio.sleep(0.05)
        return LLMVerdict.uncertain

    async def _call_openrouter(self, prompt: str) -> LLMVerdict:
        # TODO: implement with OpenRouter HTTP API
        await asyncio.sleep(0.05)
        return LLMVerdict.uncertain

    async def _call_grok(self, prompt: str) -> LLMVerdict:
        # TODO: implement with xAI Grok API
        await asyncio.sleep(0.05)
        return LLMVerdict.uncertain


LLM = LLMAnalyzer(SETTINGS)


# -------------------------------
# filters: Policy / Orchestration
# -------------------------------
class Decision(str, Enum):
    delivered = "delivered"
    flagged = "flagged"
    blocked = "blocked"


class PolicyEngine:
    def __init__(self, nb: NaiveBayesFilter, llm: LLMAnalyzer, settings: Settings) -> None:
        self.nb = nb
        self.llm = llm
        self.settings = settings

    async def evaluate(self, msg: Message) -> ClassifiedMessage:
        nb_score = self.nb.predict_proba(f"{msg.subject} \n {msg.body}")
        if nb_score < self.settings.nb_suspicious_threshold:
            return ClassifiedMessage(**msg.dict(), nb_score=nb_score, decision=Decision.delivered)

        # Suspicious → escalate to LLM
        verdict = await self.llm.analyze(msg, nb_score)
        if verdict == LLMVerdict.scam:
            return ClassifiedMessage(
                **msg.dict(),
                nb_score=nb_score,
                llm_verdict=verdict,
                decision=Decision.blocked,
                reason="LLM: likely BEC/phishing",
            )
        if verdict == LLMVerdict.uncertain:
            return ClassifiedMessage(
                **msg.dict(),
                nb_score=nb_score,
                llm_verdict=verdict,
                decision=Decision.flagged,
                reason="Suspicious content – manual review",
            )
        return ClassifiedMessage(**msg.dict(), nb_score=nb_score, llm_verdict=verdict, decision=Decision.delivered)


POLICY = PolicyEngine(NB_FILTER, LLM, SETTINGS)


# -------------------------------
# gateway: FastAPI app
# -------------------------------
app = FastAPI(title="SMTP AI Gateway – Demo", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> Dict[str, Any]:
    return {"status": "ok", "app": SETTINGS.app_name}


@app.post("/train")
def train(data: TrainSet) -> Dict[str, Any]:
    NB_FILTER.train(data)
    return {"status": "trained", "items": len(data.items)}


@app.post("/send", response_model=ClassifiedMessage)
async def send(msg: Message) -> ClassifiedMessage:
    classified = await POLICY.evaluate(msg)
    if classified.decision != Decision.blocked:
        INBOX.save(classified)
    return classified


@app.get("/inbox", response_model=List[ClassifiedMessage])
def inbox(limit: int = 100) -> List[ClassifiedMessage]:
    return INBOX.list(limit=limit)


# --- Optional WebSocket for live streaming decisions ---
class ConnectionManager:
    def __init__(self) -> None:
        self.active: List[WebSocket] = []

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self.active.append(ws)

    def disconnect(self, ws: WebSocket) -> None:
        if ws in self.active:
            self.active.remove(ws)

    async def broadcast(self, message: Dict[str, Any]) -> None:
        for ws in list(self.active):
            try:
                await ws.send_text(json.dumps(message))
            except Exception:
                self.disconnect(ws)


WS_MANAGER = ConnectionManager()


@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    if not SETTINGS.enable_ws:
        await ws.close(code=4403)
        return
    await WS_MANAGER.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            payload = json.loads(data)
            msg = Message(**payload)
            classified = await POLICY.evaluate(msg)
            if classified.decision != Decision.blocked:
                INBOX.save(classified)
            await WS_MANAGER.broadcast({"event": "classified", "data": classified.dict()})
    except WebSocketDisconnect:
        WS_MANAGER.disconnect(ws)


# -------------------------------
# run: uvicorn entrypoint (for local dev)
# -------------------------------
# Usage:
#   uvicorn this_file:app --reload --port 8080
#   curl -X POST http://localhost:8080/send -H 'Content-Type: application/json' \
#        -d '{"sender":"alice@corp.com","receiver":"ap@vendor.com","subject":"Thanh toán","body":"Vui lòng chuyển khoản vào tài khoản mới."}'
#   curl http://localhost:8080/inbox
# -------------------------------



  

Đã dựng xong skeleton code vào canvas cho bạn rồi — gồm FastAPI gateway, inbox (SQLite/in-memory), bộ lọc Naive Bayes “stub”, lớp gọi LLM (OpenAI/OpenRouter/Grok) dạng adapter, policy điều phối, HTTP + WebSocket endpoint, và hướng chạy bằng uvicorn.

Bạn muốn mình:

* tách ra thành nhiều file đúng cấu trúc thư mục (package chuẩn),
* hay bổ sung ví dụ script train Naive Bayes với dataset giả lập + file `.env` để cấu hình khóa API LLM?

  Hiểu rồi 👍. Mình sẽ bổ sung thêm **2 phần** cho bạn:

1. **Ví dụ script huấn luyện Naive Bayes với dataset giả lập** (spam vs ham emails).
2. **File `.env` mẫu** để cấu hình API key của LLM (OpenAI, OpenRouter, Grok).

---

### 1. `train_naive_bayes.py`

Script này tạo dataset giả lập nhỏ, train với `scikit-learn`, sau đó lưu model ra file pickle (`naive_bayes_model.pkl`).

```python
# train_naive_bayes.py
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dataset giả lập
emails = [
    "Win money now, click here",  # spam
    "Congratulations, you won a lottery prize",  # spam
    "Dear friend, please see the attached invoice",  # spam
    "Your account has been compromised, reset password",  # spam
    "Let's meet tomorrow at 10am",  # ham
    "Are you available for the project discussion?",  # ham
    "Please review the attached report",  # ham
    "Lunch at the cafeteria today?",  # ham
]

labels = [
    "spam", "spam", "spam", "spam",
    "ham", "ham", "ham", "ham"
]

# Vectorizer + model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

# Save model + vectorizer
with open("naive_bayes_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Naive Bayes model trained and saved as naive_bayes_model.pkl")
```

Khi chạy `python train_naive_bayes.py`, bạn sẽ có `naive_bayes_model.pkl`.
Sau này trong `naive_bayes_filter.py` chỉ cần load file này để phân loại email.

---

### 2. `.env` file mẫu

```ini
# .env

# OpenAI API
OPENAI_API_KEY=sk-yourkey

# OpenRouter API
OPENROUTER_API_KEY=sk-yourkey

# Grok API
GROK_API_KEY=sk-yourkey

# LLM provider preference (openai | openrouter | grok)
LLM_PROVIDER=openai
```

Trong Python bạn có thể load bằng `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

👉 Bạn có muốn mình chỉnh luôn phần `naive_bayes_filter.py` trong skeleton code để **tự động load `naive_bayes_model.pkl`** nếu có, thay vì stub như bây giờ không?


  Câu hỏi của bạn rất thực tế 👍, mình phân tích chi tiết để bạn dễ hình dung:

---

## 1. Nếu thay dataset tiếng Anh → tiếng Việt

* **Naive Bayes** trong scikit-learn không phân biệt ngôn ngữ.
* Điều quan trọng là **tiền xử lý dữ liệu** (tokenizer, stopwords, tách từ).

  * Nếu dataset của bạn là **tiếng Việt thuần văn bản** → bạn nên dùng `underthesea`, `pyvi` hoặc `viTokenizer` để tách từ thay vì chỉ `.split()`.
  * Còn nếu dataset đã ở dạng "chuỗi văn bản ngắn, không cần phân tách nhiều" thì giữ nguyên code cũng chạy được, nhưng độ chính xác sẽ thấp hơn.

👉 Tóm lại: **chỉ cần thay đổi bước tiền xử lý** nếu muốn tối ưu cho tiếng Việt, còn lại train script không cần sửa gì nhiều.

---

## 2. Model sau khi train được lưu ở đâu?

Trong script `train_naive_bayes.py`, mình đã demo lưu model bằng **joblib**:

```python
import joblib
joblib.dump(nb_model, "naive_bayes_model.pkl")
```

📌 File `naive_bayes_model.pkl` chính là model đã train xong, lưu trong thư mục chạy script.

---

## 3. Chương trình chính load model thế nào?

Trong **gateway** hoặc **service Flask/FastAPI**, bạn load model như sau:

```python
import joblib

nb_model = joblib.load("naive_bayes_model.pkl")
```

Sau đó có thể gọi `nb_model.predict([message])` để phân loại từng email/message.

---

## 4. Muốn train thêm có được không?

* **Scikit-learn Naive Bayes (MultinomialNB)** có hỗ trợ **incremental learning** qua hàm `partial_fit`.
* Tuy nhiên, code mẫu ban đầu của mình chỉ dùng `fit()` (train từ đầu).
* Nếu muốn train thêm, bạn có 2 lựa chọn:

### (a) Train lại toàn bộ

* Gom dataset cũ + dataset mới → train lại từ đầu với `fit()`.
* Ưu điểm: đơn giản, dễ triển khai.
* Nhược: dataset lớn thì hơi lâu.

### (b) Train thêm bằng `partial_fit`

Ví dụ:

```python
nb_model.partial_fit(X_new, y_new, classes=["ham", "spam"])
joblib.dump(nb_model, "naive_bayes_model.pkl")
```

* Cách này hữu ích khi dữ liệu đến liên tục (streaming).
* Nhưng bạn phải đảm bảo khi gọi `partial_fit` lần đầu tiên thì phải truyền đầy đủ danh sách `classes`.

---

👉 Tóm lại:

* **Không cần thay đổi nhiều khi sang tiếng Việt**, chỉ cần xử lý tách từ.
* **Model lưu ra file `.pkl`** trong thư mục train.
* **Chương trình chính load bằng `joblib.load()`**.
* **Có thể train thêm** bằng `partial_fit`, nhưng cách dễ nhất là train lại toàn bộ.

---

Bạn muốn mình viết thêm **phiên bản train Naive Bayes tiếng Việt với underthesea + partial\_fit** để bạn test luôn không?


  Chuẩn luôn 👍. Nếu bạn muốn tránh `underthesea` (vì nặng, phụ thuộc nhiều), ta có thể chuyển sang **Pyvi** – nó nhẹ hơn và dễ cài. Bạn sẽ dùng `ViTokenizer` để tách từ trước khi huấn luyện Naive Bayes.

### Cập nhật `train_naive_bayes.py` với **Pyvi**

```python
import os
import pickle
import pandas as pd
from pyvi import ViTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Đường dẫn lưu model
MODEL_PATH = "models/naive_bayes_vn.pkl"

def tokenize_vietnamese(text):
    """
    Sử dụng Pyvi để tách từ cho tiếng Việt.
    """
    return ViTokenizer.tokenize(text)

def train_naive_bayes(dataset_path: str):
    # Giả sử dataset có 2 cột: "text", "label"
    df = pd.read_csv(dataset_path)

    X = df["text"].astype(str).apply(tokenize_vietnamese)
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Pipeline gồm vectorizer + Naive Bayes
    pipeline = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("classifier", MultinomialNB())
    ])

    pipeline.fit(X_train, y_train)

    # Đánh giá thử
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Lưu model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipeline, f)

    print(f"✅ Model đã lưu tại {MODEL_PATH}")

if __name__ == "__main__":
    # Ví dụ train với dataset giả lập
    train_naive_bayes("datasets/phishing_dataset_vn.csv")
```

---

### Load model trong chương trình chính

```python
import pickle

MODEL_PATH = "models/naive_bayes_vn.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

# Ví dụ dự đoán
if __name__ == "__main__":
    model = load_model()
    test_email = "Xin chúc mừng, bạn đã trúng thưởng 1 tỷ VNĐ!"
    print(model.predict([test_email]))
```

---

### Về việc **train thêm**

* Model ở đây được lưu bằng `pickle`, nó **không hỗ trợ incremental training**.
* Nếu bạn muốn **train thêm dữ liệu mới**, cách tốt nhất là:

  1. Load lại dataset cũ + dữ liệu mới → train lại từ đầu.
  2. Hoặc chuyển sang model `sklearn.naive_bayes.MultinomialNB` có thể dùng `partial_fit()` (nhưng bạn cần giữ lại vectorizer consistent).

👉 Nếu dataset của bạn **tăng dần theo thời gian**, thì mình sẽ chỉnh pipeline để hỗ trợ **incremental learning**.

---

Bạn có muốn mình chỉnh lại thành **pipeline hỗ trợ `partial_fit`** để bạn có thể nạp thêm dữ liệu mà không cần train lại từ rỗng không?

  
