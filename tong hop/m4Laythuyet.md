Alright class, welcome. Please take your seats.

Good morning, everyone. I'm glad to see you all here for our course on Cybersecurity and Artificial Intelligence. Today, we're diving into one of the most practical and relatable topics: **Module 4 - Detection of Email Threats with AI**. 📧

The email inbox is a primary battleground in cybersecurity. For decades, it's been the main entry point for attackers trying to deliver malware, steal credentials, or commit fraud. Early on, defenders used simple rule-based filters. For instance, a rule might say, "If the email contains the word 'Viagra', block it." But what did attackers do? They started writing 'V\!agra' or 'V.i.a.g.r.a'. The defenders' rules became a fragile game of cat and mouse.

This is where AI comes in. Instead of relying on rigid, pre-programmed rules, we can train models to *learn* what spam or phishing looks like based on thousands of examples. They can identify complex patterns that a human could never write a rule for. Today, we will explore four foundational machine learning algorithms that power modern email security systems.

Let's begin.

-----

## Spam Detection with the Perceptron

### Theory 🧠

The **Perceptron** is the simplest form of a neural network; you can think of it as a single artificial neuron. It's a linear classifier, meaning it tries to separate data by drawing a straight line.

Imagine a simple decision-maker. It takes in several pieces of evidence (we call these **features** or inputs), weighs how important each piece of evidence is (these are the **weights**), and sums them up. If this total sum crosses a certain threshold (the **activation function**), it makes a decision: "yes" or "no".

In spam detection, the features could be the count of certain words in an email. The model learns by adjusting its weights. If it incorrectly classifies a spam email as legitimate ("ham"), it will increase the importance (the weight) of the "spammy" words found in that email, making it more likely to classify it correctly next time. This process is repeated thousands of times until the weights are properly tuned.

### Example 🧮

Let's classify the email subject: "**Buy cheap viagra now\!**"

1.  **Feature Extraction**: We first convert the text into numbers. We'll use a simple "bag-of-words" model where the features are the counts of specific words.
      * `count('buy')`: 1
      * `count('cheap')`: 1
      * `count('viagra')`: 1
      * `count('hello')`: 0 (This word isn't in our subject line)
2.  **Applying Weights**: The model has already been trained and has learned weights for these words. Spammy words will have positive weights, and normal words will have negative or zero weights.
      * `w_buy`: +0.6
      * `w_cheap`: +0.5
      * `w_viagra`: +1.2
      * `w_hello`: -0.4
3.  **Calculation**: We multiply the counts by their weights and sum them up.
      * `Score = (1 * 0.6) + (1 * 0.5) + (1 * 1.2) + (0 * -0.4) = 2.3`
4.  **Decision**: Let's say our Perceptron's decision threshold is `0.5`. Since `2.3` is greater than `0.5`, the model classifies the email as **Spam**.

### Real-Life Scenarios

  * **Hacker's Side 😈**: A hacker knows the Perceptron is looking for specific keywords. To bypass it, they might use **word obfuscation** (e.g., `v i a g r a`, `ch3ap`) or use synonyms that the model hasn't been trained on. A more advanced technique is to put the spam message inside an image. A simple text-based Perceptron cannot read text in an image, rendering it blind to the attack.
  * **Defender's Side 🛡️**: A cybersecurity team would use a Perceptron as a fast, first-line-of-defense filter. It's computationally inexpensive, meaning it can process millions of emails very quickly. They would constantly retrain the model with new spam and ham examples to ensure its weights are up-to-date with the latest attacker techniques.

-----

## Spam Detection with Support Vector Machines (SVMs)

### Theory 🧠

A **Support Vector Machine (SVM)** is another classification algorithm, but it operates on a more sophisticated principle. If a Perceptron just wants to find *any* line to separate two groups, an SVM wants to find the *best possible* line.

Imagine you have red and blue marbles on a table. An SVM draws a line to separate them, but it also ensures this line is as far away as possible from the nearest red marble and the nearest blue marble. This space between the line and the closest points is called the **margin**. A wider margin leads to a more confident and robust model. The points that define this margin are called **support vectors**.

Furthermore, SVMs have a powerful "kernel trick" that allows them to find complex, non-linear boundaries. If you can't separate the marbles with a straight line, the SVM can project the data into a higher dimension where a straight line (or plane) *can* separate them.

### Example 🧮

Let's visualize email data.

1.  **Feature Extraction**: Let's use two features:
      * x-axis: Percentage of capitalized words.
      * y-axis: Frequency of the word "free".
2.  **Plotting the Data**: We plot our training emails on a 2D graph. Spam emails (like "FREE IPHONE CLICK NOW\!\!\!") will likely cluster in the top-right corner (high capitalization, high frequency of "free"). Legitimate emails (ham) will cluster near the bottom-left.
3.  **Finding the Hyperplane**: The SVM algorithm will then draw a line (in 2D, a line is a hyperplane) that perfectly separates these two clusters, maximizing the margin between them.
4.  **Classification**: When a new email arrives, we extract its features, plot it on the graph, and see which side of the line it falls on. If it's on the spam side, it gets blocked.

### Real-Life Scenarios

  * **Hacker's Side 😈**: An attacker might craft a message designed to lie very close to the decision boundary. This email would have some spammy characteristics but not enough to clearly fall into the spam category. For example, a professionally formatted email with just one suspicious link and mild urgency. These "ambiguous" emails are the hardest for an SVM to classify correctly.
  * **Defender's Side 🛡️**: Cybersecurity analysts love SVMs because they are highly accurate and less prone to overfitting than some other models. The maximum margin principle makes them very robust. They are particularly effective in high-dimensional spaces, which is common in text classification where every unique word can be a dimension.

-----

## Phishing Detection with Logistic Regression

### Theory 🧠

Despite its name, **Logistic Regression** is used for classification. Its key feature is that it predicts **probability**. Instead of a simple "yes" or "no," it tells you the *likelihood* that an input belongs to a class. For example, "There is a 92% probability that this email is phishing."

It works by taking the weighted sum of inputs (like the Perceptron) and feeding it into a special function called the **Sigmoid function**. The sigmoid function is an S-shaped curve that squishes any real number into a value between 0 and 1, which we can then interpret as a probability.

The mathematical formula for the sigmoid function is:
$$P(\text{class}=1) = \frac{1}{1 + e^{-z}}$$
where $z$ is the weighted sum of the input features.

### Example 🧮

Let's analyze an email for phishing cues.

1.  **Feature Extraction**: We look for common phishing indicators. These are often binary (yes/no) features.
      * `has_urgency` (e.g., "account suspended"): 1 (Yes)
      * `sender_in_contacts`: 0 (No)
      * `url_is_ip_address` (e.g., [http://192.168.1.1/login](https://www.google.com/search?q=http://192.168.1.1/login)): 1 (Yes)
      * `has_generic_greeting` (e.g., "Dear Valued Customer"): 1 (Yes)
2.  **Calculation**: The model, with its pre-trained weights, computes the score `z`. Let's say the calculation results in `z = 2.4`.
3.  **Probability**: We plug this into the sigmoid function:
    $$P(\text{Phishing}) = \frac{1}{1 + e^{-2.4}} \approx \frac{1}{1 + 0.09} \approx 0.917$$
4.  **Decision**: The model outputs a probability of \~92%. A defender can set a policy: if the probability is \> 85%, quarantine the email and alert the security team.

### Real-Life Scenarios

  * **Hacker's Side (Phisher) 🎣**: Phishers try to craft emails that lower this probability score. They might register a domain that looks very similar to a legitimate one (**typosquatting**, e.g., `gooogle.com` instead of `google.com`). They will avoid obvious phishing words and copy the exact branding and language of a trusted company to make the email appear authentic, manipulating features to stay below the detection threshold.
  * **Defender's Side 🛡️**: The probabilistic output of logistic regression is incredibly valuable for a Security Operations Center (SOC). It allows for a **tiered response**. An email with a 99% phishing probability can be deleted automatically. An email with a 75% score might be sent to the user's junk folder with a large warning banner. A 60% score might just have its links disabled. This granular control is more effective than a simple block/allow system.

-----

## Using Naïve Bayes for Spam Detection

### Theory 🧠

The **Naïve Bayes** classifier is a probabilistic model based on the famous **Bayes' Theorem**. In simple terms, the theorem allows us to find the probability of an event happening given that another event has already occurred.

For spam, the question is: "What is the probability that an email is **Spam**, *given that it contains the words 'free', 'viagra', and 'winner'*?"

The theorem looks like this:
$$P(\text{Spam} | \text{words}) = \frac{P(\text{words} | \text{Spam}) \cdot P(\text{Spam})}{P(\text{words})}$$

The algorithm gets its name from its "naïve" assumption: it assumes that every word (feature) in the email is **independent** of all the others. This is obviously not true in language—"New York" is a single concept—but this simplification makes the computation extremely fast and, surprisingly, it works very well for text classification.

### Example 🧮

Let's classify the email: "**Offer for you**"

The model has already been trained and knows the following probabilities from its training data:

  * P("offer" | Spam) = 10% (The word "offer" appears in 10% of spam emails)
  * P("offer" | Ham) = 1%
  * P("for" | Spam) = 15%
  * P("for" | Ham) = 20%
  * P("you" | Spam) = 25%
  * P("you" | Ham) = 30%
  * The overall probability of any email being spam is P(Spam) = 40%, and P(Ham) = 60%.

The classifier calculates two scores:

1.  **Score for Spam**: `P(Spam) * P("offer"|Spam) * P("for"|Spam) * P("you"|Spam)`
    `= 0.40 * 0.10 * 0.15 * 0.25 = 0.0015`
2.  **Score for Ham**: `P(Ham) * P("offer"|Ham) * P("for"|Ham) * P("you"|Ham)`
    `= 0.60 * 0.01 * 0.20 * 0.30 = 0.00036`

Since the score for Spam (`0.0015`) is higher than the score for Ham (`0.00036`), the model classifies the email as **Spam**.

### Real-Life Scenarios

  * **Hacker's Side 😈**: Attackers can perform a **Bayesian poisoning attack**. Knowing the filter relies on word probabilities, they can stuff a spam email with a large number of words that are highly likely to appear in legitimate emails (e.g., copying a neutral paragraph from a news article). This flood of "good" words can overwhelm the few "bad" words (like a malicious link), tricking the classifier into thinking the email is legitimate.
  * **Defender's Side 🛡️**: Naïve Bayes is one of the oldest but still most widely used spam filters. It's incredibly fast to train and run, and it doesn't require a massive dataset to perform well. Many email clients use a Naïve Bayes filter that learns from your personal behavior—every time you mark an email as spam, you are helping to retrain the model and improve its accuracy.

That concludes our tour of these four foundational models. In the real world, a sophisticated email security gateway won't rely on just one. It will use an **ensemble** of models, combining their strengths to create a multi-layered defense that is incredibly difficult for attackers to bypass.

Great — let’s treat this as if you are sitting in my university class.
We are now entering **Module 4 – Detection of Email Threats With Artificial Intelligence (AI)**.

This module is critical because **email is still the #1 vector for cyberattacks** (spam, phishing, malicious attachments, business email compromise). Attackers exploit the human factor, while defenders must combine filtering rules, AI, and threat intelligence to keep inboxes safe.

I will walk you through the **theory → examples → real-life hacker vs. defender scenarios** for each subtopic.

---

# 📘 Module 4 – Detection of Email Threats With AI

### Topics

1. Spam Detection with **Perceptron**
2. Spam Detection with **Support Vector Machines (SVMs)**
3. Phishing Detection with **Logistic Regression**
4. Spam Detection with **Naïve Bayes**

---

## 1. Spam Detection with Perceptron

### 🧠 Theory

* A **perceptron** is the simplest form of a neural network (single-layer).
* It classifies input into **spam** or **not spam** by calculating a weighted sum of features (like keywords, sender reputation, suspicious links).
* If the sum exceeds a threshold → spam, otherwise → legitimate.

Mathematically:

$$
y = \begin{cases}
1 & \text{if } (w \cdot x + b) > 0 \quad \text{(spam)} \\
0 & \text{otherwise (ham)}
\end{cases}
$$

where

* **x** = feature vector (e.g., \[contains “Viagra”, has suspicious link, sender domain reputation])
* **w** = learned weights
* **b** = bias

### 💻 Example (Python)

```python
from sklearn.linear_model import Perceptron

X = [[0,1], [1,1], [1,0], [0,0]]  # toy features
y = [1, 1, 0, 0]  # labels: 1=spam, 0=ham

clf = Perceptron()
clf.fit(X, y)
print(clf.predict([[1,0]]))  # test with suspicious email
```

### ⚔️ Real Life Scenario

* **Hacker side**: Spammers randomize keywords (“Vi\@gr@” instead of “Viagra”) to evade simple perceptron filters.
* **Defender side**: Early spam filters (late 90s) used perceptrons to block repetitive spam campaigns. Still useful today in lightweight IoT mail gateways where computing power is limited.

---

## 2. Spam Detection with Support Vector Machines (SVMs)

### 🧠 Theory

* **SVMs** are stronger than perceptrons.
* They find the **best hyperplane** that separates spam vs. ham emails with the **largest margin**.
* Works well in high-dimensional spaces (thousands of email features: word frequency, attachments, HTML tags).

### 💻 Example (Python)

```python
from sklearn import svm

X = [[0,1], [1,1], [1,0], [0,0]]  
y = [1, 1, 0, 0]  

clf = svm.SVC(kernel='linear')
clf.fit(X, y)
print(clf.predict([[1,0]]))  # predict spam
```

### ⚔️ Real Life Scenario

* **Hacker side**: Spammers try to generate “borderline” emails that lie close to the SVM decision boundary (e.g., mixing normal text with phishing content).
* **Defender side**: Security companies (like Google’s Gmail) trained large SVMs on millions of emails to drastically reduce spam around 2005–2010.

---

## 3. Phishing Detection with Logistic Regression

### 🧠 Theory

* Logistic Regression predicts the **probability** an email is phishing.
* Instead of a hard yes/no like perceptron, it outputs:

  $$
  P(\text{phishing}|x) = \frac{1}{1 + e^{-(w \cdot x + b)}}
  $$
* Features: suspicious URLs, mismatched “from” address, urgent language (“verify immediately”), attachment types.
* If probability > threshold (e.g., 0.7) → mark as phishing.

### 💻 Example (Python)

```python
from sklearn.linear_model import LogisticRegression

X = [[1,0,0], [0,1,1], [1,1,0], [0,0,1]]  
y = [1,0,1,0]  # 1=phishing, 0=legit  

clf = LogisticRegression()
clf.fit(X, y)
print(clf.predict_proba([[1,0,0]]))  # phishing probability
```

### ⚔️ Real Life Scenario

* **Hacker side**: Phishers use psychology (“your account will be locked”) to raise click-through rates. They exploit human bias, not just technology.
* **Defender side**: Logistic regression is widely used in **email gateways (Proofpoint, Microsoft 365)** to assign phishing risk scores. Emails above threshold are quarantined.

---

## 4. Using Naïve Bayes for Spam Detection

### 🧠 Theory

* Naïve Bayes uses **Bayes’ theorem** with the assumption that email features are independent.
* Very popular in the early 2000s (SpamAssassin, Thunderbird).
* Formula:

$$
P(\text{spam}|x) = \frac{P(x|\text{spam})P(\text{spam})}{P(x)}
$$

* Example:

  * Word “free” occurs in 70% of spam but only 5% of ham.
  * If an email has “free”, the probability it’s spam is high.

### 💻 Example (Python)

```python
from sklearn.naive_bayes import MultinomialNB

X = [[2,1,0], [0,0,2], [1,2,0], [0,1,1]]  
y = [1,1,0,0]  # spam=1, ham=0  

clf = MultinomialNB()
clf.fit(X, y)
print(clf.predict([[1,0,1]]))  # predict spam/ham
```

### ⚔️ Real Life Scenario

* **Hacker side**: Spammers use **“Bayes poisoning”** by inserting benign words (“meeting, project, invoice”) into spam emails to trick the model.
* **Defender side**: Naïve Bayes was lightweight and effective for small businesses; still used in resource-limited mail servers.

---

# 🔑 Summary of Module 4

* **Perceptron** → Simple, fast, but weak (good for teaching basics).
* **SVM** → Strong classifier for spam/ham, used in production historically.
* **Logistic Regression** → Excellent for phishing probability scoring.
* **Naïve Bayes** → Classic, still effective in lightweight environments.

---

👉 Question for you, Tuấn:
Do you want me to **extend this module with hands-on coding labs** (step-by-step Jupyter notebooks with datasets like Enron Spam Dataset or Vietnamese phishing dataset), so you can practice training these models, or do you prefer I keep the teaching more **theoretical + case studies** style?

Excellent! Practice is where theory becomes **muscle memory**.
I’ll design **practice exercises for each part of Module 4** (Perceptron, SVM, Logistic Regression, Naïve Bayes).

Each exercise has:

1. **Hands-on task** (Python + dataset idea)
2. **Conceptual thinking question** (forces you to reflect on attacker vs defender strategies)

---

# 📝 Module 4 – Practice Exercises

---

## 1. Spam Detection with Perceptron

### 🔧 Exercise (Hands-on)

* Load a **toy dataset** (you can create your own small set of 10–20 emails).
* Extract simple features such as:

  * contains the word “free” (1/0)
  * contains suspicious link (1/0)
  * subject length > 50 (1/0)
* Train a **Perceptron classifier** to distinguish spam vs ham.

👉 Code hint:

```python
from sklearn.linear_model import Perceptron
import numpy as np

X = np.array([[1,1,0], [0,0,1], [1,0,1], [0,1,0]])  
y = np.array([1,0,1,0])  # spam=1, ham=0

clf = Perceptron()
clf.fit(X, y)
print(clf.predict([[1,1,0]]))  # test new email
```

### 💡 Thinking Question

* Suppose you are a spammer. How could you **manipulate the subject line** or word spelling to bypass a perceptron-based filter?
* As a defender, how could you **add new features** to make the perceptron more robust?

---

## 2. Spam Detection with SVMs

### 🔧 Exercise (Hands-on)

* Use the **Enron Spam Dataset** (available on Kaggle or UCI ML repo).
* Extract word frequencies as features using `CountVectorizer` in scikit-learn.
* Train an **SVM classifier** and test its accuracy.
* Compare linear vs RBF kernel performance.

👉 Code hint:

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

emails = ["Win a free iPhone", "Meeting at 10am", "Earn $$$ working from home"]
labels = [1,0,1]  # spam=1

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3)

clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
```

### 💡 Thinking Question

* Attackers sometimes craft “borderline” spam that looks half-legit.

  * Example: “Your invoice is attached – special offer inside!”
* Why would such emails be difficult for SVMs?
* What defense techniques can improve the margin (e.g., adding metadata like sender reputation)?

---

## 3. Phishing Detection with Logistic Regression

### 🔧 Exercise (Hands-on)

* Build a small dataset of **phishing vs legitimate URLs** (manually or from PhishTank).
* Extract features such as:

  * URL length
  * presence of “@” symbol
  * number of dots in domain
  * whether HTTPS is used
* Train a **Logistic Regression** model to output phishing probability.

👉 Code hint:

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1,0,1],[0,1,0],[1,1,0]])  # features
y = np.array([1,0,1])  # phishing=1, legit=0

clf = LogisticRegression()
clf.fit(X, y)
print(clf.predict_proba([[1,0,0]]))  # phishing probability
```

### 💡 Thinking Question

* Hackers use psychological tricks in phishing (urgency, authority, fear).
* If logistic regression only uses **technical features** (like URL length), what important **human/social features** might be missing?
* How could you integrate NLP to catch suspicious wording like “verify immediately” or “password reset”?

---

## 4. Using Naïve Bayes for Spam Detection

### 🔧 Exercise (Hands-on)

* Use scikit-learn’s `MultinomialNB` with a small email dataset.
* Train the model and test how it reacts when you add **“benign words”** into spam emails. (Simulate **Bayes poisoning attack**).

👉 Code hint:

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = ["free money offer", "project meeting tomorrow", "cheap meds buy now"]
labels = [1,0,1]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

clf = MultinomialNB()
clf.fit(X, labels)
print(clf.predict(vectorizer.transform(["free project tomorrow"])))
```

### 💡 Thinking Question

* As a hacker, how could you “poison” the training data to reduce the filter’s accuracy?
* As a defender, what strategies (like retraining with fresh data, using ensemble models) could you apply to resist poisoning?

---

# 🎯 Wrap-Up Exercise for Module 4

1. Collect **10–20 emails** (mix of spam, phishing, and legitimate).
2. Extract simple features (keywords, URL features, subject length, sender domain).
3. Train **all 4 models (Perceptron, SVM, Logistic Regression, Naïve Bayes)**.
4. Compare accuracy, precision, recall.
5. Write a one-page reflection: *Which model works best and why? How would a hacker try to beat it?*

---

👉 Tuấn, would you like me to **provide you with a pre-prepared mini dataset (CSV)** so you can immediately start these exercises in Python, or do you prefer I guide you to **collect your own dataset (emails + phishing URLs)** to make it more realistic?


Any questions?
