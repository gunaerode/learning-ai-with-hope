# Python OOPS – Class vs Object Method Cheat Sheet
# [Python MCQ & Answer](https://drive.google.com/file/d/1BS8mf_Fqu_biE6A7F0u8cbY_C31HK1mD/view) / [Click here](./Python%20MCQ%20%26%20A.pdf) 🤓📚

This file is a **quick-reference guide** to understand **static methods, instance methods, and method binding in Python**. It is interview‑ready and beginner‑friendly.

---

## 🧠 Core Idea

> **Methods decide how they are called — not whether an object exists.**

Python behaves consistently once you understand how method binding works.

---

## 🔑 The 5 Golden Rules (Must Remember)

### 1️⃣ Static Method

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

✅ Correct usage:
```python
Calculator.add(2, 3)
```

⚠️ Works but bad style:
```python
calc = Calculator()
calc.add(2, 3)
```

📌 No `self`, no object required

---

### 2️⃣ Instance Method

```python
class Calculator:
    def subtract(self, a, b):
        return a - b
```

✅ Correct usage:
```python
calc = Calculator()
calc.subtract(5, 3)
```

❌ Wrong usage:
```python
Calculator.subtract(5, 3)
```

📌 Needs `self` → must be called via object

---

### 3️⃣ Creating an Object Does NOT Block Class Access

```python
calc = Calculator()
Calculator.add(3, 4)   # ✅ still valid
```

📌 Object existence is irrelevant for static methods

---

### 4️⃣ Method Without `self` and Without `@staticmethod` = BUG

```python
class Calculator:
    def multiply(a, b):
        return a * b
```

✔ Works accidentally:
```python
Calculator.multiply(3, 4)
```

❌ Fails:
```python
calc = Calculator()
calc.multiply(3, 4)
```

📌 Never rely on this behavior

---

### 5️⃣ Python Rewrites Method Calls (MOST IMPORTANT)

| You Write | Python Executes |
|----------|----------------|
| `obj.method(x)` | `Class.method(obj, x)` |
| `Class.method(x)` | `method(x)` |

📌 This explains **all behavior**

---

## ✅ Correct Calculator Design (Best Practice)

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

### Usage

```python
calc = Calculator()

Calculator.add(2, 3)        # ✅ static
Calculator.multiply(3, 4)   # ✅ static
calc.subtract(5, 2)         # ✅ instance
calc.divide(10, 2)          # ✅ instance
```

---

## 🔴 Summary Table

| Method Type | Uses `self` | Call via Class | Call via Object | Status |
|------------|------------|---------------|----------------|--------|
| Static | ❌ | ✅ | ⚠️ bad style | ✅ Correct |
| Instance | ✅ | ❌ | ✅ | ✅ Correct |
| Broken | ❌ | ⚠️ | ❌ | ❌ Bug |

---

## 🎯 Interview One‑Liners

- **Static methods belong to the class and do not receive `self`.**
- **Instance methods must be called via an object to receive `self`.**
- **A method without `self` is not static by default.**
- **Creating an object does not restrict calling static methods via the class.**

---

## 🧠 Final Mental Model

> **If Python needs `self`, you must use an object. If it does not, use the class.**

---

🚀 You now have a complete, clear understanding of **Python method binding and OOPS behavior**.

