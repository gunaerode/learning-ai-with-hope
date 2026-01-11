# Fraud Detection Problem Analysis

## Problem Statement

XYZ Bank is facing issues of fraudulent transactions.  
The goal is to **detect and prevent fraud before the transaction is completed**.

### Options Given
A) Supervised – Regression  
B) Supervised – Classification  
C) Unsupervised – Clustering  
D) Semi-Supervised  

---

## Best Solution: **B) Supervised – Classification**

### Why Classification?

Fraud detection is a **binary decision problem**:
- Fraud
- Not Fraud

Since the output is a **category (label)**, this is a **classification problem**.

Regression is not suitable because it predicts numeric values, not labels.

---

## Dataset Explanation

Typical dataset contains:

| Feature | Example |
|-------|---------|
Transaction Amount | 4500 |
Location | Chennai |
Device ID | Mobile |
Time | 10:45 PM |
User History | High risk |

Target Label:
- `1 = Fraud`
- `0 = Normal`

This is **labeled historical data**, making it perfect for **supervised learning**.

---

## Model Workflow

```
Transaction Data → Classification Model → Fraud / Not Fraud
```

### Models Used
- Logistic Regression
- Random Forest
- XGBoost
- Neural Networks

---

## Call to Action (System Response)

If prediction = **Fraud**
- Block transaction
- Trigger OTP verification
- Alert fraud team
- Notify customer

If prediction = **Not Fraud**
- Approve transaction

---

## Why Other Options Are Not Ideal

| Option | Reason |
|------|--------|
Supervised–Regression | Outputs numbers, not fraud labels |
Unsupervised–Clustering | Groups transactions but does not directly classify fraud |
Semi-Supervised | Useful when few labels exist, but banks usually have labeled fraud data |

---

## Final Conclusion

**Correct Answer: B) Supervised – Classification**

Because the problem requires predicting a categorical outcome (Fraud / Not Fraud) using labeled data, which is exactly the goal of supervised classification.

# Sample Fraud Detection Dataset

| Transaction_Amount | Location | Device | Hour | Is_Fraud |
|-------------------|----------|--------|------|---------|
| 1200 | Chennai | Mobile | 10 | 0 |
| 45000 | Mumbai | Web | 2 | 1 |
| 500 | Delhi | Mobile | 14 | 0 |
| 78000 | Kolkata | ATM | 23 | 1 |
| 3000 | Chennai | Mobile | 9 | 0 |

### Label Meaning
- **Is_Fraud = 1 → Fraud**
- **Is_Fraud = 0 → Normal**

