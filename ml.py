# Machine Learning (ML)

## 1. What is Machine Learning?

**Machine Learning (ML)** is a branch of **Artificial Intelligence (AI)** where computers learn patterns from data and use those patterns to make predictions or decisions without being explicitly programmed for every situation.

### Simple Example

Suppose we want to predict whether a student will pass.

Instead of manually writing rules:

```text
IF study_hours > 5 AND attendance > 75%
    → Pass
ELSE
    → Fail
```

We provide historical data to an ML model:

| Study Hours | Attendance | Result |
| ----------: | ---------: | ------ |
|           8 |        90% | Pass   |
|           6 |        80% | Pass   |
|           2 |        60% | Fail   |
|           3 |        65% | Fail   |
|           7 |        85% | Pass   |

The model learns the relationship between the **inputs** and the **result**.

For a new student:

```text
Study Hours = 5
Attendance = 78%
```

The model may predict:

```text
Pass
```

---

# 2. How Machine Learning Works

A typical ML workflow is:

```text
                 DATA
                   │
                   ▼
          ┌─────────────────┐
          │ Data Collection │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Data Cleaning   │
          │ & Preprocessing │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Feature         │
          │ Selection       │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Train ML Model  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Evaluate Model  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Make Prediction │
          └─────────────────┘
```

### General ML Process

1. Collect data
2. Clean the data
3. Preprocess the data
4. Select or create features
5. Split data into training and testing sets
6. Train the model
7. Evaluate the model
8. Tune the model if required
9. Make predictions on new data

---

# 3. Important ML Terminology

## Dataset

A **dataset** is a collection of data used for training and/or evaluating an ML model.

Example:

| Age | Salary | Purchased |
| --: | -----: | --------- |
|  22 |  25000 | No        |
|  35 |  60000 | Yes       |
|  42 |  80000 | Yes       |

---

## Features

**Features are the input variables used by the model to make a prediction.**

In the above example:

```text
Age
Salary
```

are features.

Features are commonly represented by **X**.

```text
X = [Age, Salary]
```

---

## Target / Label

The **target** or **label** is the output that we want the model to predict.

Here:

```text
Purchased
```

is the target.

It is commonly represented by **y**.

```text
y = Purchased
```

### Example

```text
Features (X)              Target (y)

Age                       Purchased
Salary                    ↓
                          Yes / No
```

---

## Model

A **model** is a mathematical representation that learns patterns from data and uses those patterns to make predictions.

Examples:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Neural Networks

---

# 4. Training and Testing

A dataset is commonly divided into:

```text
                Dataset
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
     Training Data      Testing Data
          │                 │
          ▼                 │
     Train Model            │
          │                 │
          └────────┬────────┘
                   ▼
             Evaluate Model
```

## Training Data

Training data is used to **teach the model**.

The model learns patterns and relationships from this data.

## Testing Data

Testing data is used to check how well the model performs on **unseen data**.

### Example

For 1000 records:

```text
80% → Training Data = 800 records
20% → Testing Data  = 200 records
```

An 80:20 split is common, but other splits can also be used.

---

# 5. Types of Machine Learning

There are three major types:

```text
                 Machine Learning
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
 Supervised      Unsupervised     Reinforcement
 Learning          Learning          Learning
```

---

# 6. Supervised Learning

In **supervised learning**, the training data contains both:

* Input features
* Known output/labels

```text
Input + Correct Output
          │
          ▼
        Model
          │
          ▼
     Learn Pattern
          │
          ▼
 New Input → Prediction
```

### Example

```text
Hours Studied → Result

2 → Fail
4 → Fail
6 → Pass
8 → Pass
```

The model learns from examples where the correct answer is already known.

## Types of Supervised Learning

```text
             Supervised Learning
                    │
             ┌──────┴──────┐
             ▼             ▼
        Regression    Classification
```

---

## 6.1 Regression

**Regression is used when the output is a continuous numerical value.**

### Examples

```text
House Price  → ₹50,00,000
Salary       → ₹8,50,000
Temperature  → 32.5°C
Sales        → ₹1,25,000
```

### Common Regression Algorithms

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

### Example

```text
House Area + Location + Rooms
            │
            ▼
       ML Model
            │
            ▼
   Predicted House Price
```

---

## 6.2 Classification

**Classification is used when the output belongs to a category or class.**

### Examples

```text
Email       → Spam / Not Spam

Transaction → Fraud / Not Fraud

Student     → Pass / Fail

Disease     → Positive / Negative
```

### Common Classification Algorithms

* Logistic Regression
* Decision Tree
* Random Forest
* KNN
* SVM
* Naive Bayes

### Example

```text
Age + Salary + Credit Score
            │
            ▼
       ML Model
            │
            ▼
     Loan Approved
          OR
     Loan Rejected
```

---

# 7. Unsupervised Learning

In **unsupervised learning**, the data does **not contain predefined labels**.

The model tries to discover hidden patterns or structures in the data.

```text
              Unlabeled Data
                    │
                    ▼
              ML Algorithm
                    │
                    ▼
          Discover Patterns
                    │
                    ▼
             Groups/Clusters
```

### Example

A company has customer data:

```text
Age
Income
Spending Score
```

There are no predefined customer categories.

The model can group customers based on their similarities:

```text
Cluster 1 → Low Spending Customers
Cluster 2 → Medium Spending Customers
Cluster 3 → High Spending Customers
```

### Common Unsupervised Algorithms

* K-Means Clustering
* Hierarchical Clustering
* DBSCAN
* PCA

---

# 8. Clustering

**Clustering is the process of grouping similar data points together.**

Example:

```text
              Customer Data
                   │
                   ▼
                K-Means
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Cluster 1 Cluster 2 Cluster 3
       Low       Medium    High
       Spending  Spending  Spending
```

The important point is:

> The clusters are discovered from the data; the model is not given the correct cluster labels beforehand.

---

# 9. Reinforcement Learning

In **Reinforcement Learning (RL)**, an agent learns by interacting with an environment.

The agent receives:

* **Reward** → Positive feedback for a desirable action
* **Penalty** → Negative feedback for an undesirable action

```text
        ┌─────────────┐
        │ Environment │
        └──────┬──────┘
               │
          State/Reward
               │
               ▼
          ┌─────────┐
          │  Agent  │
          └────┬────┘
               │
             Action
               │
               ▼
        ┌─────────────┐
        │ Environment │
        └─────────────┘
```

### Example

A robot is learning to reach a destination:

```text
Correct movement → +10 reward
Wrong movement   → -5 reward
Reaches target   → +100 reward
```

Over time, the agent learns which actions produce higher rewards.

---

# 10. What Does "Learning" Actually Mean?

An ML model does not literally understand data like a human.

It **adjusts mathematical parameters to reduce prediction errors**.

For example, Linear Regression uses:

```text
y = mx + c
```

Where:

```text
m → Weight
c → Bias
```

During training, the model tries to find suitable parameter values.

```text
Initial Parameters
       │
       ▼
   Prediction
       │
       ▼
 Calculate Error
       │
       ▼
 Adjust Parameters
       │
       ▼
 Better Prediction
       │
       ▼
      Repeat
```

This process is called **training**.

---

# 11. Loss Function

A **loss function** measures how far the model's prediction is from the actual value.

Example:

```text
Actual Value     = 100
Predicted Value  = 90
```

The prediction has an error of:

```text
100 - 90 = 10
```

The loss function converts prediction errors into a numerical value.

```text
Prediction
     │
     ▼
Compare with Actual
     │
     ▼
Calculate Loss
     │
     ▼
Adjust Model
```

Generally:

> **Lower loss means the model's predictions are closer to the actual values.**

Different ML problems use different loss functions.

---

# 12. Overfitting

**Overfitting occurs when a model learns the training data too specifically, including noise, and performs poorly on unseen data.**

```text
Training Performance → Very Good
Testing Performance  → Poor
```

### Example

Imagine a student memorizes every question from a practice test.

```text
Practice Test → 100%
Actual Exam   → Poor
```

This is similar to overfitting.

### In ML

```text
Training Data
      │
      ▼
Model memorizes too much
      │
      ▼
Excellent training performance
      │
      ▼
Poor performance on new data
```

---

# 13. Underfitting

**Underfitting occurs when the model is too simple to learn the important patterns in the data.**

```text
Training Performance → Poor
Testing Performance  → Poor
```

### Example

Trying to predict house prices using only house size while ignoring:

* Location
* Number of rooms
* Age
* Amenities

The model may be too simple to capture the actual relationship.

---

# 14. Good Fit

The goal is to build a model that generalizes well.

```text
Training Performance → Good
Testing Performance  → Good
```

The model should learn the important patterns without simply memorizing the training data.

---

# 15. Bias and Variance

Bias and variance help explain model errors.

## High Bias

The model is too simple.

```text
High Bias
    ↓
Underfitting
```

## High Variance

The model is too sensitive to the training data.

```text
High Variance
    ↓
Overfitting
```

### Bias-Variance Tradeoff

The goal is to find a good balance:

```text
Bias              Variance
  │                  │
  └────────┬─────────┘
           ▼
     Good Generalization
```

---

# 16. Feature Scaling

Feature scaling makes numerical features have comparable scales.

Suppose we have:

```text
Age     = 20 – 60

Salary  = 20,000 – 2,00,000
```

Salary has much larger numerical values.

Some algorithms can be affected by differences in scale.

Two common techniques are:

* Standardization
* Normalization

---

## 16.1 Standardization

Standardization transforms values so that they generally have:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

Formula:

```text
z = (x - mean) / standard deviation
```

In Python:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 16.2 Normalization

Normalization commonly scales values to a fixed range such as:

```text
0 to 1
```

---

# 17. Categorical Data

Categorical data contains values such as:

```text
Gender
------
Male
Female
Male
```

or:

```text
City
------
Chennai
Bangalore
Delhi
```

Many ML algorithms require numerical input.

Therefore, categorical values need to be converted into numerical representations.

---

# 18. One-Hot Encoding

Suppose we have:

```text
Color

Red
Blue
Green
```

One-hot encoding converts them into separate binary columns:

| Red | Blue | Green |
| --: | ---: | ----: |
|   1 |    0 |     0 |
|   0 |    1 |     0 |
|   0 |    0 |     1 |

In Python:

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
```

---

# 19. Model Evaluation

After training a model, we need to determine how well it performs.

## Classification Metrics

Common classification metrics include:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Accuracy

Accuracy measures the proportion of predictions that are correct.

```text
Accuracy = Correct Predictions / Total Predictions
```

Example:

```text
Correct Predictions = 90
Total Predictions   = 100

Accuracy = 90 / 100
         = 90%
```

### Important

Accuracy can be misleading when classes are highly imbalanced.

---

# 20. Confusion Matrix

A confusion matrix summarizes classification predictions.

For binary classification:

```text
                    Predicted
                  Positive  Negative
Actual Positive      TP        FN
Actual Negative      FP        TN
```

Where:

```text
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
```

---

# 21. Precision

Precision answers:

> **Of all the samples predicted as positive, how many were actually positive?**

Formula:

```text
Precision = TP / (TP + FP)
```

Example:

If the model predicts 100 transactions as fraud and 80 are actually fraud:

```text
Precision = 80 / 100
          = 80%
```

---

# 22. Recall

Recall answers:

> **Of all the actual positive samples, how many did the model correctly identify?**

Formula:

```text
Recall = TP / (TP + FN)
```

Recall is especially important when missing a positive case is costly.

Examples:

* Disease detection
* Fraud detection
* Security systems

---

# 23. F1-Score

F1-score combines **Precision and Recall**.

Formula:

```text
F1 = 2 × (Precision × Recall)
     --------------------------
       Precision + Recall
```

It is useful when we want a balance between precision and recall.

---

# 24. Regression Evaluation Metrics

Common regression metrics include:

* MAE
* MSE
* RMSE
* R² Score

---

## MAE — Mean Absolute Error

MAE calculates the average absolute difference between actual and predicted values.

```text
MAE = Average(|Actual - Predicted|)
```

Example:

```text
Actual      Predicted

100         90
200         220
300         290
```

MAE considers the magnitude of the errors without considering their direction.

---

## MSE — Mean Squared Error

MSE calculates the average squared error.

```text
MSE = Average((Actual - Predicted)²)
```

Because errors are squared, larger errors have a greater effect.

---

## RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

```text
RMSE = √MSE
```

RMSE is expressed in the same units as the target variable.

---

## R² Score

R² indicates how well the model explains the variation in the target variable.

A higher R² generally indicates that the model explains more of the variation in the target, although the appropriate metric depends on the problem.

---

# 25. ML vs Traditional Programming

## Traditional Programming

```text
Rules + Data
     │
     ▼
  Program
     │
     ▼
   Output
```

Example:

```text
IF marks >= 40
    → Pass
ELSE
    → Fail
```

The programmer explicitly defines the rules.

---

## Machine Learning

```text
Data + Answers
      │
      ▼
  ML Algorithm
      │
      ▼
   Learned Model
      │
      ▼
New Data → Prediction
```

The algorithm learns patterns from examples.

### Key Difference

> **Traditional programming explicitly defines the rules, while machine learning learns patterns or relationships from data.**

---

# 26. Complete ML Example

Suppose a bank wants to predict whether a customer will subscribe to a product.

## Step 1 — Collect Data

Example features:

```text
Age
Job
Balance
Education
Previous Campaign
```

Target:

```text
Subscribed
```

---

## Step 2 — Preprocess Data

Possible preprocessing steps:

```text
Missing Values
      ↓
Handle Missing Data

Categorical Data
      ↓
Encoding

Numerical Data
      ↓
Scaling if required
```

---

## Step 3 — Separate X and y

```text
X = Age
    Job
    Balance
    Education
    Previous Campaign

y = Subscribed
```

---

## Step 4 — Split Data

```text
                Dataset
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Training           Testing
          │                 │
          ▼                 │
     Train Model             │
          │                 │
          └────────┬────────┘
                   ▼
              Evaluate
```

---

## Step 5 — Train Model

For example, using Logistic Regression:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()

model.fit(X_train, y_train)
```

---

## Step 6 — Make Predictions

```python
predictions = model.predict(X_test)
```

---

## Step 7 — Evaluate

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print(accuracy)
```

---

# 27. Complete Machine Learning Pipeline

```text
                 RAW DATA
                     │
                     ▼
            Data Preprocessing
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Features              Target
          │                     │
          └──────────┬──────────┘
                     ▼
               Train/Test Split
                     │
             ┌───────┴────────┐
             ▼                ▼
         Training          Testing
             │                │
             ▼                │
         Train Model           │
             │                │
             └───────┬────────┘
                     ▼
                 Prediction
                     │
                     ▼
                 Evaluation
                     │
                     ▼
              Final ML Model
```

---

# 28. Important ML Algorithms

| Algorithm           | Main Use                    |
| ------------------- | --------------------------- |
| Linear Regression   | Regression                  |
| Logistic Regression | Classification              |
| Decision Tree       | Classification / Regression |
| Random Forest       | Classification / Regression |
| KNN                 | Classification / Regression |
| SVM                 | Classification / Regression |
| K-Means             | Clustering                  |
| Naive Bayes         | Classification              |
| Neural Networks     | Complex prediction tasks    |

---

# 29. Important Terms to Remember

| Term           | Meaning                                                   |
| -------------- | --------------------------------------------------------- |
| Dataset        | Collection of data                                        |
| Feature        | Input variable                                            |
| Target         | Output to predict                                         |
| Label          | Known target value                                        |
| Model          | Learned mathematical representation                       |
| Training       | Process of learning from data                             |
| Testing        | Evaluating on unseen data                                 |
| Prediction     | Model's output for new data                               |
| Loss           | Measure of prediction error                               |
| Overfitting    | Model performs well on training but poorly on unseen data |
| Underfitting   | Model is too simple and performs poorly                   |
| Scaling        | Bringing numerical features to comparable scales          |
| Encoding       | Converting categorical data into numerical form           |
| Classification | Predicting a category                                     |
| Regression     | Predicting a continuous numerical value                   |
| Clustering     | Grouping similar data points                              |
| Accuracy       | Proportion of correct predictions                         |
| Precision      | Correct positive predictions among predicted positives    |
| Recall         | Correct positive predictions among actual positives       |
| F1-score       | Balance between precision and recall                      |

---

# 30. Possible SME Questions

## Basic Questions

1. What is Machine Learning?
2. What is the difference between AI and ML?
3. How is ML different from traditional programming?
4. What are the types of Machine Learning?
5. What is supervised learning?
6. What is unsupervised learning?
7. What is reinforcement learning?

## Dataset Questions

8. What is a dataset?
9. What is a feature?
10. What is a target?
11. What is a label?
12. What is the difference between feature and target?
13. Why do we split data into training and testing sets?

## Supervised Learning

14. What is regression?
15. What is classification?
16. What is the difference between regression and classification?
17. Give examples of classification problems.
18. Give examples of regression problems.

## Unsupervised Learning

19. What is clustering?
20. What is K-Means?
21. How is supervised learning different from unsupervised learning?

## Model Training

22. What happens during model training?
23. What is a loss function?
24. Why do we minimize loss?
25. What are parameters?
26. What are hyperparameters?

## Model Performance

27. What is overfitting?
28. What is underfitting?
29. How can you reduce overfitting?
30. What is bias?
31. What is variance?
32. What is the bias-variance tradeoff?

## Preprocessing

33. Why is preprocessing required?
34. How do you handle missing values?
35. What is feature scaling?
36. What is standardization?
37. What is normalization?
38. What is categorical data?
39. What is one-hot encoding?
40. Why do we encode categorical variables?

## Evaluation

41. What is accuracy?
42. What is precision?
43. What is recall?
44. What is F1-score?
45. What is a confusion matrix?
46. What are TP, TN, FP and FN?
47. What are MAE, MSE and RMSE?
48. What is R² score?
49. When can accuracy be misleading?

---

# 31. Short Answers for an SME Meeting

## What is Machine Learning?

> **Machine Learning is a subset of Artificial Intelligence that enables computers to learn patterns from data and make predictions or decisions without explicitly programming every rule. A typical ML workflow involves collecting and preprocessing data, selecting features, splitting the data into training and testing sets, training a model, evaluating its performance, and using the trained model to make predictions on new data.**

## What are the types of Machine Learning?

> **The three major types are supervised learning, unsupervised learning, and reinforcement learning. Supervised learning uses labeled data and includes classification and regression. Unsupervised learning works with unlabeled data and is commonly used for clustering. Reinforcement learning involves an agent interacting with an environment and learning through rewards and penalties.**

## What is the difference between Classification and Regression?

> **Classification predicts a category or class, such as spam or not spam. Regression predicts a continuous numerical value, such as house price or temperature.**

## What is Overfitting?

> **Overfitting occurs when a model learns the training data too specifically, including noise, so it performs very well on training data but poorly on unseen data.**

## What is Underfitting?

> **Underfitting occurs when a model is too simple to learn the important patterns in the data, resulting in poor performance on both training and testing data.**

## What is a Feature?

> **A feature is an input variable used by an ML model to make a prediction. For example, in house-price prediction, area, number of rooms and location can be features.**

## What is a Target?

> **The target is the output variable that the model is trained to predict. For example, in house-price prediction, the house price is the target.**

## What is the difference between Training and Testing Data?

> **Training data is used to teach the model and learn patterns, while testing data is unseen data used to evaluate how well the trained model generalizes.**

## What is a Loss Function?

> **A loss function measures the difference between the model's predicted output and the actual output. During training, the model tries to minimize this loss.**

## What is Accuracy?

> **Accuracy is the proportion of correct predictions out of all predictions.**

```text
Accuracy = Correct Predictions / Total Predictions
```

## What is Precision?

> **Precision tells us, among all the samples predicted as positive, how many were actually positive.**

```text
Precision = TP / (TP + FP)
```

## What is Recall?

> **Recall tells us, among all the actual positive samples, how many were correctly identified by the model.**

```text
Recall = TP / (TP + FN)
```

## What is F1-Score?

> **F1-score is the harmonic mean of precision and recall and provides a balance between the two.**

```text
F1 = 2 × (Precision × Recall)
     --------------------------
       Precision + Recall
```

---

# 32. Quick Revision

```text
Machine Learning
│
├── Supervised Learning
│   │
│   ├── Classification
│   │   ├── Logistic Regression
│   │   ├── Decision Tree
│   │   ├── Random Forest
│   │   └── SVM
│   │
│   └── Regression
│       ├── Linear Regression
│       ├── Decision Tree Regression
│       └── Random Forest Regression
│
├── Unsupervised Learning
│   │
│   ├── Clustering
│   │   ├── K-Means
│   │   ├── Hierarchical Clustering
│   │   └── DBSCAN
│   │
│   └── Dimensionality Reduction
│       └── PCA
│
└── Reinforcement Learning
    │
    ├── Agent
    ├── Environment
    ├── State
    ├── Action
    └── Reward
```

### Remember These Core Concepts

```text
Data
 ↓
Preprocessing
 ↓
Features + Target
 ↓
Train/Test Split
 ↓
Model Training
 ↓
Prediction
 ↓
Evaluation
```

### Most Important Concepts to Study Next

1. Linear Regression
2. Logistic Regression
3. Decision Trees
4. Entropy
5. Information Gain
6. Gini Index
7. Random Forest
8. K-Means
9. Train/Test Split
10. Cross-Validation
11. Overfitting & Underfitting
12. Bias & Variance
13. Accuracy, Precision, Recall & F1-Score
14. MAE, MSE, RMSE & R²
15. Feature Scaling
16. Encoding
17. Hyperparameters
18. Model Tuning
