# Is There a Formula to Discover Patterns in AI/ML?

## Traditional (SLR approach)

In Simple Linear Regression (SLR), we **assume the form of the
equation**:

y = mx + c

We then use mathematical formulas to directly compute the values of
**m** and **c** from the data.

-   Fixed equation
-   Direct calculation
-   No iteration needed
-   Works for simple linear problems

------------------------------------------------------------------------

## AI / ML Approach (Pattern Discovery)

In AI/ML, we **do not assume the exact equation**.

Instead, the system **learns the best weights automatically** from data
using a learning rule.

There *is* a formula behind this learning.

------------------------------------------------------------------------

## The Universal Learning Formula

Most ML algorithms use this core idea:

New Weights = Old Weights − α × (∂Error / ∂Weights)

This is called **Gradient Descent**.

Where: - **Error** = difference between predicted and actual value -
**Weights** = parameters in the model - **α (alpha)** = learning rate

------------------------------------------------------------------------

## What This Formula Does

1.  Predict using current weights
2.  Measure error
3.  Calculate how error changes with respect to weights
4.  Adjust weights to reduce error
5.  Repeat thousands of times

This is how the model **discovers patterns**.

------------------------------------------------------------------------

## Comparison

  Traditional SLR           ML / AI
  ------------------------- ---------------------------
  Solve equation directly   Learn weights iteratively
  Fixed formula             Flexible model form
  Human derives math        Machine optimizes error
  Small/simple problems     Complex problems

------------------------------------------------------------------------

## One-Line Clarity

**SLR uses a math formula to find the line.**\
**ML uses a learning formula to discover any pattern.**
