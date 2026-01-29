# Simple Linear Regression (SLR) --- From Dataset to Deployment

## Problem

Predict **Salary** based on **Years of Experience**.

------------------------------------------------------------------------

## Step 1 --- Full Dataset

  YearsExperience (X)   Salary (Y)
  --------------------- ------------
  1                     30000
  2                     35000
  3                     40000
  4                     45000
  5                     50000
  6                     55000

------------------------------------------------------------------------

## Step 2 --- Split into Train & Test

### Training Dataset

  X   Y
  --- -------
  1   30000
  2   35000
  3   40000
  4   45000

### Test Dataset

  X   Y
  --- -------
  5   50000
  6   55000

------------------------------------------------------------------------

## Step 3 --- Training Phase (Build Model)

Simple Linear Regression formula:

Y = mX + c

Where: - m = slope - c = intercept

From training data, the model becomes:

Salary = 5000 × Experience + 25000

------------------------------------------------------------------------

## Step 4 --- Testing Phase

For X = 5: 5000 × 5 + 25000 = 50000 ✅

For X = 6: 5000 × 6 + 25000 = 55000 ✅

------------------------------------------------------------------------

## Step 5 --- Deployment

If a user enters: \> 7 years experience

Prediction: 5000 × 7 + 25000 = 60000

------------------------------------------------------------------------

# How 5000 and 25000 are Calculated

## Training Data Used

  X   Y       XY       X²
  --- ------- -------- ----
  1   30000   30000    1
  2   35000   70000    4
  3   40000   120000   9
  4   45000   180000   16

### Sums

ΣX = 10\
ΣY = 150000\
ΣXY = 400000\
ΣX² = 30\
n = 4

------------------------------------------------------------------------

## Slope Formula (m)

m = \[ nΣXY − (ΣX)(ΣY) \] / \[ nΣX² − (ΣX)² \]

m = \[4×400000 − (10×150000)\] / \[4×30 − 100\]\
m = 100000 / 20\
m = **5000**

------------------------------------------------------------------------

## Intercept Formula (c)

c = (ΣY − mΣX) / n

c = (150000 − 5000×10) / 4\
c = 100000 / 4\
c = **25000**

------------------------------------------------------------------------

## Final Model

**Salary = 5000 × Experience + 25000**

-   5000 → Salary increase per year
-   25000 → Base salary at 0 experience

------------------------------------------------------------------------

## Complete Flow

Collect Data → Split Train/Test → Train Model → Test Model → Deploy →
Predict


---

### Why ΣX² = 30 ?

Training X values:

1, 2, 3, 4

#### Step 1 — Square each X (X²)

| X | X² |
|---|----|
| 1 | 1 × 1 = 1 |
| 2 | 2 × 2 = 4 |
| 3 | 3 × 3 = 9 |
| 4 | 4 × 4 = 16 |

#### Step 2 — Add all squared values

ΣX² = 1 + 4 + 9 + 16  
ΣX² = 30

---

### Important Note

- ΣX  = 1 + 2 + 3 + 4 = 10
- (ΣX)² = 10² = 100 ❌ (This is NOT ΣX²)
- Σ(X²) = 30 ✅
