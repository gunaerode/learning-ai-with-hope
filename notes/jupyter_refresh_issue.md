# Jupyter Notebook Static Method Issue – Root Cause & Solution

## 📌 Problem Statement

Even after adding `@staticmethod` to a method in `calculator.py`, calling it like:

```python
Calculator.multiply(3, 4)
```

still throws the error:

```text
TypeError: Calculator.multiply() missing 1 required positional argument
```

This happens **only in Jupyter Notebook**, while the same code works correctly in `.py` files.

---

## 🧩 Example Code

### `calculator.py`

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
```

### `main.py` or Notebook Cell

```python
from calculator import Calculator

print(Calculator.multiply(3, 4))  # Expected output: 12
```

---

## ❌ Why the Error Occurs

### Root Cause: **Jupyter Kernel Caching**

Jupyter Notebook:
- Keeps imported modules **in memory**
- Does **not reload `.py` files automatically**
- Continues using the **old class definition**
- Ignores changes like adding `@staticmethod`

So even after fixing `calculator.py`, Jupyter still runs the **previous version** of the class.

---

## ✅ Why It Works in `.py` Files

When running:

```bash
python main.py
```

Python:
- Starts a **fresh process**
- Loads the **latest file**
- Has **no caching issues**

That’s why the same code works correctly in terminal execution.

---

## ✅ Solutions (Choose One)

### 🔁 Solution 1: Restart Jupyter Kernel (Recommended)

In Jupyter menu:

```
Kernel → Restart Kernel → Restart & Run All
```

This clears memory and reloads everything.

---

### 🔁 Solution 2: Force Reload the Module

```python
import importlib
import calculator

importlib.reload(calculator)
from calculator import Calculator
```

---

### 🔁 Solution 3: Enable Auto Reload (Best for Learning)

Add this at the **top of the notebook**:

```python
%load_ext autoreload
%autoreload 2
```

Now Jupyter automatically reloads modified `.py` files.

---

## 🧠 Important Clarifications

| Item | Is it the problem? |
|----|----|
File name (`main.py` vs `main-sample.py`) | ❌ No |
Using `@staticmethod` correctly | ✅ Yes |
Jupyter kernel caching | ✅ YES (main issue) |
Not restarting kernel | ✅ YES |
Python logic error | ❌ No |

---

## 🎯 Key Takeaway

> Jupyter Notebook caches imported modules.  
> Any change in a `.py` file requires a kernel restart or module reload.

---

## 💡 Interview-Ready One-Liner

> Jupyter notebooks keep modules in memory, so class changes are not reflected unless the kernel is restarted or autoreload is enabled.

---

## ✅ Final Working Call

```python
print(Calculator.multiply(3, 4))  # 12
```

