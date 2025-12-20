# Calculator Method Binding Explained (Python OOPS)

This document explains **all execution scenarios** for the given `Calculator` code and clarifies **why some calls work, some fail, and some are bad design**.

---

## 📌 Current Code

```python

# calculator.py
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# main.py 
from calculator import Calculator

calc = Calculator()

print(f"Subtract: {calc.subtract(3, 4)}")          # ✅ correct
print("Addition: ", Calculator.add(3, 4))         # ✅ correct


# NOTE:
# Calculator.subtract(3, 4)    # ❌ wrong (instance method)
# Calculator().add(3, 4)       # ❌ design-wise wrong (static method via object)

calc.multiply(3, 4)
```

---

## 1️⃣ `add` → Static Method

```python
@staticmethod
def add(a, b):
    return a + b
```

### ✅ Correct usage

```python
Calculator.add(3, 4)
```

### 🔍 Why it works

- No `self`
- No object required
- Pure utility logic

### ❌ Bad design (but works)

```python
Calculator().add(3, 4)
```

This works but **should not be used**, because:

- Static methods belong to the class
- Creating an object is unnecessary

---

## 2️⃣ `subtract` → Proper Instance Method

```python
def subtract(self, a, b):
    return a - b
```

### ✅ Correct usage

```python
calc = Calculator()
calc.subtract(3, 4)
```

### 🔍 Internal Python behavior

```python
Calculator.subtract(calc, 3, 4)
```

### ❌ Wrong usage

```python
Calculator.subtract(3, 4)
```

❌ Error:

```
TypeError: subtract() missing 1 required positional argument: 'b'
```

Reason: Python does **not** auto-create an object when calling via class.

---

## 3️⃣ `multiply` → ❌ Broken Method (Important)

```python
def multiply(a, b):
    return a * b
```

### ❌ What this is

- NOT static
- NOT instance
- Accidentally broken method

---

### Case 1️⃣ Works (but accidentally)

```python
Calculator.multiply(3, 4)
```

✔ Output: `12`

Reason:

- Called via class
- No object binding happens

---

### Case 2️⃣ ❌ Fails (your code)

```python
calc.multiply(3, 4)
```

Python internally rewrites:

```python
Calculator.multiply(calc, 3, 4)
```

❌ Error:

```
TypeError: multiply() takes 2 positional arguments but 3 were given
```

---

### ✅ Correct Fix (choose ONE)

#### Option A: Make it static

```python
@staticmethod
def multiply(a, b):
    return a * b
```

Usage:

```python
Calculator.multiply(3, 4)
```

#### Option B: Make it instance-based

```python
def multiply(self, a, b):
    return a * b
```

Usage:

```python
Calculator().multiply(3, 4)
```

---

## 4️⃣ `divide` → Proper Instance Method

```python
def divide(self, a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
```

### ✅ Correct usage

```python
calc.divide(10, 2)
```

---

## 🔴 Summary Table

| Method   | Definition      | Class Call | Object Call  | Status    |
| -------- | --------------- | ---------- | ------------ | --------- |
| add      | `@staticmethod` | ✅          | ⚠️ bad style | ✅ Correct |
| subtract | `self`          | ❌          | ✅            | ✅ Correct |
| multiply | no self         | ✅          | ❌            | ❌ Broken  |
| divide   | `self`          | ❌          | ✅            | ✅ Correct |

---

## 🔑 Golden Rules (Must Remember)

1. **Static method** → no `self`, call via `Class.method()`
2. **Instance method** → must have `self`, call via `object.method()`
3. **Method without **``** and without **``** is always a bug**
4. Python does NOT make methods static by default

---

## 🧠 Interview One‑Liner

> A method without `self` is not static by default. It only works when called via the class and breaks when accessed through an instance due to automatic binding.

---

## ✅ Final Recommended Version

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

---

🚀 You now fully understand **method binding, self, static methods, and Python OOPS behavior**.

