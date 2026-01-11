# Email Routing Problem — Domain Analysis

## Problem Statement
An e-commerce company receives 1000+ customer emails daily regarding shipment, delivery, product quality, refunds, etc.  
All emails go to one inbox, but must be **automatically redirected** to the correct department.

---

## Input & Output

**Input:** Customer Email (Text)  
**Output:** Department Label (Shipment, Delivery, Quality, Refund, etc.)

This is a **Text Classification** problem.

---

## Correct 3 Stages of the Problem Domain

### Stage 1 — NLP
Because the input data is **TEXT**.

### Stage 2 — Supervised Learning
Because we train the model on **labeled emails**:
```
Email → Department
```

### Stage 3 — Classification
Because the output is a **category**, not a number.

---

## Final Answer

**Stage1: NLP**  
**Stage2: Supervised Learning**  
**Stage3: Classification**

---

## Example Dataset

| Email Text | Label |
|-----------|------|
My order hasn't arrived | Delivery |
Product quality is very poor | Quality |
My package is not shipped | Shipment |
I want my refund | Finance |

---

## Model Flow

```
Customer Email → NLP Processing → Supervised Model → Classification → Correct Department
```

---

## Conclusion

This problem is a **Supervised Text Classification problem under the NLP domain**.
