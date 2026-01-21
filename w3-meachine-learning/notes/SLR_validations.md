# Simple Linear Regression (SLR) – Model Validation

Validating parameters in Simple Linear Regression means checking how well the model works and how accurate its predictions are.

This validation is done using statistical measures:

- SSE – Sum of Squared Errors  
- SSR – Sum of Squares Regression  
- SST – Sum of Squares Total  
- R² – Coefficient of Determination  

---

## 1. Error Definition

Error in regression is defined as:

Error = Actual value (yi) – Predicted value (ŷi)

Where:

- yi = actual observed value  
- ŷi = predicted value  
- i = observation index  
- n = total number of observations  

---

## 2. Sum of Squares Error (SSE)

Formula:

SSE = Σ(yi – ŷi)²

Meaning:

- Measures total prediction error  
- Difference between actual and predicted values  

Interpretation:

- Higher SSE → Poor prediction  
- Lower SSE → Good prediction  

Goal:

Minimize SSE for better model performance.

---

## 3. Sum of Squares Regression (SSR)  
Also called Explained Sum of Squares (ESS)

Formula:

SSR = Σ(ŷi – ȳ)²

Where:

- ȳ = mean of actual values  

Meaning:

- Measures how much variation in data is explained by the model  

Interpretation:

- Higher SSR → Better model performance  
- Lower SSR → Poor model performance  

Goal:

Maximize SSR.

---

## 4. Sum of Squares Total (SST)

Formula:

SST = Σ(yi – ȳ)²

Meaning:

- Total variation present in the dataset  
- Independent of the model  

Important Relationship:

SST = SSR + SSE

Interpretation:

- SST is constant for a given dataset  
- It is NOT a direct performance measure  

---

## 5. Why Regression Means Low Error

Regression aims to minimize prediction error.

Error formula:

Error = yi – ŷi

If predicted values are close to actual values:

- Error becomes small  
- SSE becomes small  
- Model becomes better  

Therefore:

Lower error → Better regression model.

---

## 6. R-Squared (Model Accuracy Measure)

Formula:

R² = SSR / SST  
or  
R² = 1 – (SSE / SST)

Interpretation:

- R² close to 1 → Very good model  
- R² around 0.7 → Good model  
- R² around 0.5 → Moderate model  
- R² below 0.3 → Poor model  

---

## 7. Final Summary

| Metric | Full Form | Goal |
|------|---------|-----|
| SSE | Sum of Squared Errors | Lower is Better |
| SSR | Sum of Squares Regression | Higher is Better |
| SST | Sum of Squares Total | Constant for dataset |
| R² | Coefficient of Determination | Closer to 1 is Better |

---

### Final Notes

- SSE measures error → should be minimized  
- SSR measures explained variance → should be maximized  
- SST is fixed for dataset  
- R² summarizes overall model quality  

# R-Square and Adjusted R-Square Explanation

These are two important metrics used to evaluate the performance of regression models.

---

## 1. What is R-Square (R²)?

R-Square measures:

“How much of the variation in the target variable is explained by the regression model.”

---

### Formula

R² = SSR / SST  
R² = 1 – (SSE / SST)

Where:

- SSR = Sum of Squares Regression  
- SSE = Sum of Squares Error  
- SST = Sum of Squares Total  

---

### Interpretation

| R² Value | Meaning |
|-------|--------|
| 0 | Model explains nothing |
| 0.5 | Model explains 50% of variation |
| 0.8 | Model explains 80% of variation |
| 1 | Perfect model |

Higher R² means better model fit.

---

## 2. Intuition Using x and x²

Suppose we are predicting y.

### Model 1 – Using only x

y = b0 + b1 x

This gives some R² value.

Example:

R² = 0.65

---

### Model 2 – Using x and x²

y = b0 + b1 x + b2 x²

Now R² might increase.

Example:

R² = 0.75

---

### Important Behavior of R²

Whenever we add more variables:

- R² always increases or stays the same  
- Even if the new variable is useless  
- Even if the model becomes unnecessarily complex  

---

## 3. Problem with R-Square

R-Square has a major limitation:

It never decreases when new variables are added.

Example:

| Model | Variables | R² |
|------|---------|----|
| Model 1 | x | 0.65 |
| Model 2 | x, x² | 0.75 |
| Model 3 | x, x², x³ | 0.76 |
| Model 4 | x, x², x³, random noise | 0.761 |

According to R²:

Model 4 looks best.

But in reality:

- Model 4 is overfitting  
- Extra variables are unnecessary  

So R² alone can be misleading.

---

## 4. Solution – Adjusted R-Square

To solve this issue, we use Adjusted R-Square.

Adjusted R² improves upon R² by:

- Penalizing unnecessary variables  
- Considering both accuracy and model complexity  

---

### Formula

Adjusted R² = 1 – [ (1 – R²) (n – 1) / (n – p – 1) ]

Where:

- n = number of observations  
- p = number of predictors  

---

## 5. Key Differences

| R-Square | Adjusted R-Square |
|---------|------------------|
| Always increases with more variables | Increases only if variable is useful |
| Can be misleading | More reliable |
| No penalty for complexity | Penalizes extra variables |
| Good for simple models | Better for multiple regression |

---

## 6. Practical Example

Assume:

n = 100 observations

---

### Model 1 – Only x

- Predictors: 1  
- R² = 0.70  
- Adjusted R² = 0.69  

---

### Model 2 – x and x²

- Predictors: 2  
- R² = 0.72  
- Adjusted R² = 0.71  

Adjusted R² increased.

This means:

New variable is useful.

---

### Model 3 – x, x², random noise

- Predictors: 3  
- R² = 0.725  
- Adjusted R² = 0.70  

Adjusted R² decreased.

This means:

New variable is NOT useful.

---

## 7. Final Intuition

R-Square answers:

“How well does the model fit the data?”

Adjusted R-Square answers:

“Is the model really better, or just more complex?”

---

## 8. When to Use Which Metric

| Situation | Recommended Metric |
|--------|-------------------|
| Simple Linear Regression | R² is fine |
| Multiple Regression | Prefer Adjusted R² |
| Feature comparison | Adjusted R² |
| Model selection | Adjusted R² |

---

## Final Summary

- R² measures goodness of fit  
- Higher R² generally means better model  
- But R² alone can be misleading  

Therefore:

In real-world regression analysis:

Always prefer Adjusted R-Square over R-Square.
