# Assignment 1 — Employee Resignation Prediction

## A) How will you achieve this in AI?

We will build a predictive AI system that analyzes historical employee data to predict whether an employee is likely to resign this month or next month.  
This allows the company to take preventive action and avoid project delays.

---

## B) 3 Stages of Problem Identification

### Stage 1 — Machine Learning
Because the data is structured (employee records, performance, salary, etc.).

### Stage 2 — Supervised Learning
We have labeled historical data:
Employee details → Will Resign / Will Stay

### Stage 3 — Classification
The output is categorical:
Will Resign / Will Stay

---

## C) Project Name

**Employee Attrition Prediction System**

---

## D) Dummy Dataset

| EmployeeID | Age | Experience | Salary | Performance | WorkHours | JobSatisfaction | LastPromotion(yrs) | Status |
|-----------|-----|-----------|--------|------------|-----------|---------------|------------------|---------|
E001 | 26 | 2 | 30000 | 3 | 9 | 2 | 2 | Will Resign |
E002 | 35 | 10 | 80000 | 4 | 8 | 4 | 1 | Will Stay |
E003 | 29 | 4 | 45000 | 2 | 10 | 1 | 3 | Will Resign |
E004 | 42 | 15 | 100000 | 5 | 7 | 5 | 0 | Will Stay |

---

## Model Flow

Employee Data → Supervised ML Model → Classification → Will Resign / Will Stay

---

## Conclusion

This problem is a Supervised Machine Learning Classification problem focused on predicting employee attrition.
