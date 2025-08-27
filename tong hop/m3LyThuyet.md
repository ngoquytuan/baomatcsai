# Module 3: Application of Machine Learning in Cyber Security

Welcome to Module 3! Today we'll explore how machine learning techniques are applied to cybersecurity challenges. Think of machine learning as giving computers the ability to learn patterns from data - much like how you might learn to recognize suspicious behavior by observing patterns over time.

## 1. Train-Test Splitting of Data

### Theory
Train-test splitting is the fundamental practice of dividing your dataset into two parts:
- **Training set** (typically 70-80%): Used to teach the algorithm
- **Test set** (typically 20-30%): Used to evaluate how well the algorithm learned

This prevents **overfitting** - when a model memorizes training data but fails on new, unseen data.

### Real-World Example
**Defender Scenario**: A bank wants to detect fraudulent transactions. They have 100,000 historical transactions (60,000 legitimate, 40,000 fraudulent). They use 80,000 for training their ML model and keep 20,000 hidden for testing.

**Hacker Perspective**: Attackers study this concept too. If they know a system was trained only on certain attack patterns, they might craft novel attacks that weren't in the training data.

```python
# Example code
from sklearn.model_selection import train_test_split

# Split network traffic data
X_train, X_test, y_train, y_test = train_test_split(
    network_features, attack_labels, 
    test_size=0.2, random_state=42
)
```

## 2. Standardization of Data

### Theory
Standardization transforms data so all features have:
- Mean = 0
- Standard deviation = 1

This is crucial because ML algorithms can be biased toward features with larger scales.

### Real-World Example
**Scenario**: Analyzing network traffic where you have:
- Packet size: ranges 64-1500 bytes
- Connection duration: ranges 0.1-3600 seconds
- Number of packets: ranges 1-10,000

Without standardization, the algorithm might focus only on packet count (largest numbers) and ignore packet size patterns that could indicate attacks.

**Defender Application**: A SOC (Security Operations Center) standardizes all log features before feeding them to their anomaly detection system, ensuring equal treatment of different metrics.

**Attacker Evasion**: Sophisticated attackers might try to operate within "normal" ranges for multiple standardized features simultaneously to avoid detection.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use same scaling parameters
```

## 3. Principal Component Analysis (PCA)

### Theory
PCA reduces data dimensionality while preserving the most important information. It finds new axes (principal components) that capture maximum variance in the data.

Think of it like taking a 3D shadow and projecting it onto a 2D wall - you lose some information but keep the essential shape.

### Real-World Example
**Defender Use Case**: A company monitors 500 different network metrics per minute. PCA helps identify the 20 most important metrics that capture 95% of the variation, making analysis faster and more focused.

**Practical Scenario**: 
- Original: 500 network features (bandwidth, packet types, protocols, etc.)
- After PCA: 20 components that explain most network behavior patterns
- Benefit: Faster detection, less storage, clearer visualization

**Attacker Consideration**: Attackers might try to manipulate less important features (those captured in lower principal components) to stay hidden.

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Reduce network traffic features from 100 to 10 dimensions
pca = PCA(n_components=10)
X_reduced = pca.fit_transform(X_train_scaled)

# Visualize explained variance
plt.plot(pca.explained_variance_ratio_)
plt.title('Variance Explained by Each Component')
```

## 4. Using Markov Chains to Generate Text

### Theory
Markov chains predict the next state based only on the current state, following the principle that "the future depends only on the present, not the past."

For text: Next word depends only on the current word(s), not the entire history.

### Cybersecurity Applications

**Defender Side - Password Policy Analysis**:
```
Real password patterns: "Password123" → "Password124" → "Password125"
Markov chain learns: After "Password", numbers often follow
```

**Attacker Side - Social Engineering**:
Attackers train Markov chains on company emails to generate convincing phishing messages that match the organization's communication style.

**Practical Example**: 
- Input: 1000 legitimate company emails
- Markov chain learns writing patterns
- Output: Automatically generated phishing emails that sound authentic

```python
import random

class MarkovChain:
    def __init__(self):
        self.transitions = {}
    
    def train(self, text):
        words = text.split()
        for i in range(len(words)-1):
            current = words[i]
            next_word = words[i+1]
            if current not in self.transitions:
                self.transitions[current] = []
            self.transitions[current].append(next_word)
    
    def generate(self, start_word, length=20):
        result = [start_word]
        current = start_word
        
        for _ in range(length-1):
            if current in self.transitions:
                next_word = random.choice(self.transitions[current])
                result.append(next_word)
                current = next_word
        
        return ' '.join(result)
```

## 5. XGBoost Classifier

### Theory
XGBoost (eXtreme Gradient Boosting) combines many weak decision trees to create a strong classifier. It's like having a committee of experts where each expert learns from the mistakes of previous experts.

Key advantages:
- Handles missing data well
- Built-in regularization (prevents overfitting)
- Excellent performance on structured data

### Real-World Example
**Malware Classification**:
- **Features**: File size, API calls, strings, entropy
- **Problem**: Traditional antivirus signatures miss new variants
- **XGBoost Solution**: Learns complex patterns from file characteristics

**Defender Scenario**: Microsoft uses XGBoost-like algorithms in Windows Defender to classify suspicious files based on hundreds of behavioral features.

**Attacker Response**: Malware authors use adversarial techniques, slightly modifying files to change XGBoost input features while maintaining malicious functionality.

```python
import xgboost as xgb
from sklearn.metrics import accuracy_score

# Train XGBoost for malware detection
model = xgb.XGBClassifier(
    objective='binary:logistic',
    max_depth=6,
    learning_rate=0.1,
    n_estimators=100
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

# Feature importance - which file characteristics matter most?
importance = model.feature_importances_
```

## 6. Time Series Analysis using Statsmodel

### Theory
Time series analysis examines data points collected over time to identify trends, seasonality, and anomalies. In cybersecurity, many threats have temporal patterns.

Key components:
- **Trend**: Long-term increase/decrease
- **Seasonality**: Regular patterns (daily, weekly, monthly)
- **Noise**: Random variation
- **Anomalies**: Unusual spikes or drops

### Real-World Examples

**Defender Use Case - DDoS Detection**:
- Normal traffic: 1000 requests/minute with daily patterns
- DDoS attack: Sudden spike to 50,000 requests/minute
- Time series models detect the abnormal increase

**Business Email Compromise (BEC)**:
- Normal pattern: CEO sends 5-10 emails/day to finance
- Attack pattern: Sudden 20 urgent payment requests in one hour
- Time series analysis flags this anomaly

```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

# Analyze network traffic over time
traffic_data = pd.read_csv('network_traffic.csv', parse_dates=['timestamp'])
traffic_data.set_index('timestamp', inplace=True)

# Decompose the time series
decomposition = seasonal_decompose(traffic_data['requests_per_minute'], 
                                 model='additive', period=24*60)  # Daily pattern

# Detect anomalies - points far from trend+seasonal
residuals = decomposition.resid
threshold = 3 * residuals.std()
anomalies = residuals[abs(residuals) > threshold]
```

## 7. Detecting Anomaly with Isolation Forest

### Theory
Isolation Forest detects anomalies by randomly isolating data points. The idea: anomalies are rare and different, so they can be isolated with fewer random splits.

Think of it like finding a person in a crowd:
- Normal people: Need many questions to isolate ("Are you tall? Male? Wearing red?")
- Unusual person: Need fewer questions ("Are you 8 feet tall?" - Done!)

### Real-World Applications

**Network Intrusion Detection**:
```python
from sklearn.ensemble import IsolationForest

# Train on normal network traffic
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(normal_traffic_features)

# Detect anomalies in new traffic
anomaly_scores = iso_forest.decision_function(new_traffic)
anomalies = iso_forest.predict(new_traffic)  # -1 for anomalies, 1 for normal
```

**Defender Example**: Bank uses Isolation Forest to detect unusual transactions:
- Normal: Small, regular purchases
- Anomaly: Large international transfer at 3 AM

**Attacker Evasion**: Sophisticated attackers study normal patterns and make small, incremental changes to avoid isolation.

## 8. Natural Language Processing (NLP)

### Theory
NLP helps computers understand and analyze human language. In cybersecurity, it's used for analyzing text-based threats like phishing emails, malicious social media posts, and command injection attacks.

### Applications

**Email Security**:
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Extract features from email text
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
email_features = vectorizer.fit_transform(email_texts)

# Train classifier
classifier = MultinomialNB()
classifier.fit(email_features, spam_labels)
```

**Real Scenarios**:

**Phishing Detection**:
- **Legitimate**: "Your monthly statement is ready for review"
- **Phishing**: "URGENT: Account suspended! Click here immediately!"
- **NLP detects**: Urgency words, poor grammar, suspicious links

**Social Engineering on Social Media**:
- **Attacker**: Creates fake LinkedIn profiles with AI-generated professional posts
- **Defender**: NLP models analyze posting patterns, language consistency, and network connections

## 9. Model Performance Evaluation

### Theory
You can't manage what you don't measure. In cybersecurity, wrong predictions have serious consequences:
- **False Positives**: Blocking legitimate users (business impact)
- **False Negatives**: Missing real attacks (security breach)

Key Metrics:
- **Accuracy**: Overall correctness
- **Precision**: Of predicted attacks, how many were real?
- **Recall**: Of real attacks, how many did we catch?
- **F1-Score**: Balance between precision and recall

### Real-World Impact

**Intrusion Detection System**:
```python
from sklearn.metrics import classification_report, confusion_matrix

# Evaluate model performance
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Calculate business impact
false_positives = sum((y_pred == 1) & (y_test == 0))
false_negatives = sum((y_pred == 0) & (y_test == 1))

print(f"Legitimate users blocked: {false_positives}")
print(f"Attacks missed: {false_negatives}")
```

**Business Decision Example**:
- High precision model: Few false alarms, but might miss some attacks
- High recall model: Catches most attacks, but many false alarms
- SOC teams must balance based on risk tolerance

## Connecting It All Together

Let's see how these concepts work together in a complete cybersecurity ML pipeline:

```python
# Complete pipeline example
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import xgboost as xgb

# Create ML pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),           # Standardize features
    ('pca', PCA(n_components=50)),          # Reduce dimensions
    ('classifier', xgb.XGBClassifier())      # Classify threats
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    network_data, attack_labels, test_size=0.2
)

# Train pipeline
pipeline.fit(X_train, y_train)

# Evaluate
predictions = pipeline.predict(X_test)
print(classification_report(y_test, predictions))
```

## Key Takeaways for Cybersecurity Professionals

1. **Data Quality Matters**: Garbage in, garbage out. Standardization and proper splitting are crucial.

2. **Dimensionality Reduction**: PCA helps focus on what matters most in high-dimensional security data.

3. **Ensemble Methods**: XGBoost often outperforms single algorithms in security applications.

4. **Time Awareness**: Many attacks have temporal patterns - use time series analysis.

5. **Anomaly Detection**: Isolation Forest excels at finding unknown threats.

6. **Text Analysis**: NLP is essential for email security and social engineering detection.

7. **Evaluation is Critical**: Wrong metrics lead to wrong decisions in security.

Remember: Attackers are constantly evolving. Your ML models must evolve too through continuous learning and adaptation!
