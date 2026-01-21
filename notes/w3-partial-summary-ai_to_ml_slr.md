# Artificial Intelligence – Learning Summary

---

## 1. What is Artificial Intelligence?

Artificial Intelligence (AI) is:

- The ability of machines to mimic human intelligence  
- Not only copying human physical structure  
- Mainly copying human thinking and decision-making ability  

### Traditional Programming vs AI Model

| Traditional Approach | AI Approach |
|---------------------|------------|
| Logic is written manually | Logic is learned from data |
| Rule based systems | Data driven systems |
| Fixed behavior | Improves through learning |
| Programmer defines steps | Model discovers patterns |

---

## 2. AI Domains

Different domains of AI based on data type:

| Domain | Data Type |
|------|---------|
| Machine Learning (ML) | Numerical data |
| Deep Learning (DL) | Images, numbers |
| Natural Language Processing (NLP) | Text data |
| Time Series | Date and time-based data |
| Data Science (DS) | Data analysis and insights |

---

## 3. Core Elements of AI

Main components required for AI:

- Data  
- Algorithms  
- Model  
- Training process  
- Evaluation metrics  

---

## 4. Types of Machine Learning

### Supervised Learning (SL)

- Data has input and output labels  
- Model learns mapping between input and output  

Types:

- Regression  
- Classification  

---

### Unsupervised Learning (USL)

- Data has no labels  
- Model finds hidden patterns  

Examples:

- Clustering  
- Dimensionality reduction  

---

### Semi-Supervised Learning (SSL)

- Combination of labeled and unlabeled data  

---

### Reinforcement Learning (RL)

- Learning by trial and error  
- Reward and punishment based learning  
- Not included in basic supervised/unsupervised categories  

---

## 5. Mapping Domains with Learning Types

| Domain | Learning Type |
|------|-------------|
| ML | SL, SSL, USL |
| DL | SL, SSL (USL is rare) |
| NLP | SL, SSL (USL is rare) |
| Time Series | Mainly SL (Regression only) |

---

## 6. AI Problem Solving Flow

General flow of AI system:

Input Data → Model → Prediction → Action

### Example Problems

- Email spam detection  
- Fertilizer detection from images  
- House price prediction  

---

## 7. Two Phases of AI

### Phase 1 – Model Creation

Steps:

1. Data Collection  
2. Data Preprocessing  
3. Splitting Data  
   - Training Data  
   - Test Data  
4. Training Model  
5. Testing Model  
6. Evaluation Metrics  

Flow:

Data → Preprocessing → Training → Model → Testing → Evaluation

---

### Phase 2 – Deployment

Flow:

Trained Model → User Input → Prediction → Output / Action

---

## 8. What is a Model?

For understanding:

- A model is like a formula or tool  
- Without input it does nothing  
- When input is given → prediction happens  
- Output leads to decision or action  

---

## 9. Machine Learning Algorithms

### Algorithms used for BOTH Regression and Classification

- Support Vector Machine (SVM)  
- Decision Tree  
- Random Forest  

---

### Regression Only Algorithms

- Simple Linear Regression  
- Multiple Linear Regression  
- Polynomial Regression  

Prerequisite knowledge needed:

- Basic Algebra  
- Terms  
- Expressions  
- Equations  
- Understanding of:  
  - y = mx + c  
  - y = wx + b  

---

### Classification Only Algorithms

- Logistic Regression  
- Naïve Bayes  
- K-Nearest Neighbors (KNN)  

---

## 10. Simple Linear Regression (SLR)

### Model Creation

Equation:

y = mx + c

Where:

- y = predicted output  
- x = input  
- m = slope  
- c = intercept  

---

### Deployment Example

- Train model using dataset  
- Test with unseen data  
- Predict new values  

---

## 11. Validation Parameters for SLR

### Sum of Squared Error (SSE or RSS)

Formula:

SSE = Σ(yi – ŷi)²

Interpretation:

- Higher SSE → Poor prediction  
- Lower SSE → Good prediction  

---

### Sum of Squares Regression (SSR or ESS)

Formula:

SSR = Σ(ŷi – ȳ)²

Interpretation:

- Higher SSR → Better model performance  

---

### Sum of Squares Total (SST)

Formula:

SST = SSR + SSE

Meaning:

- Total variation in data  
- Fixed for dataset  

---

## 12. R-Square (R²)

Formula:

R² = SSR / SST  
R² = 1 – (SSE / SST)

Interpretation:

| R² Value | Meaning |
|-------|--------|
| 0 | Model explains nothing |
| 1 | Perfect model |
| Closer to 1 | Better model |

---

## 13. Adjusted R-Square

Used in multiple regression to avoid misleading R².

Formula:

Adjusted R² = 1 – [ (1 – R²) (n – 1) / (n – p – 1) ]

Where:

- n = number of observations  
- p = number of predictors  

### Difference

| R-Square | Adjusted R-Square |
|--------|----------------|
| Always increases with variables | Increases only if useful |
| Can mislead | More reliable |
| No penalty for complexity | Penalizes extra variables |

---

## Final Understanding

- AI learns from data  
- Model is created through training  
- Predictions are made after deployment  
- Simple Linear Regression is the foundation of ML  
- Evaluation metrics validate model performance  

---

### Current Learning Focus

- Understanding algebra basics  
- Understanding y = mx + c  
- Learning how models learn  
- Understanding evaluation metrics  
- Building intuition for regression  
