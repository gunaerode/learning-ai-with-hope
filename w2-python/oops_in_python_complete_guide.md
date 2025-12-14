# 🧠 Object Oriented Programming (OOPS) in Python

This document explains **OOPS concepts in Python** with a **real‑world Bank Account example**, **simple diagrams**, and **interview questions**.

---

## 🔷 What is OOPS?
**OOPS (Object‑Oriented Programming System)** is a programming paradigm that models real‑world entities using **classes** and **objects**.

### 🔹 Why OOPS?
- Code reusability
- Better organization
- Security (data hiding)
- Easy maintenance

---

## 🔷 Core OOPS Concepts
1. Class & Object
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Abstraction

We will explain **all concepts using ONE real‑world example: Bank Account 🏦**

---

# 🏦 Real‑World Example: Bank Account System

---

## 1️⃣ Class & Object

### 🔹 Class
A **class** is a blueprint or template.

```python
class BankAccount:
    pass
```

### 🔹 Object
An **object** is a real instance of a class.

```python
account1 = BankAccount()
account2 = BankAccount()
```

### 🖼️ Simple Diagram
```
Class (Blueprint)
   |
   v
Object (Real Instance)
```

---

## 2️⃣ Encapsulation (Data Hiding)

Encapsulation means **binding data and methods together** and **restricting direct access**.

### 🔹 Real World Example
You cannot directly change your bank balance.
You must use **deposit** or **withdraw**.

### 🔹 Python Example

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance
```

```python
account = BankAccount("Guna", 5000)
account.deposit(2000)
account.withdraw(1000)
print(account.get_balance())
```

### 🖼️ Diagram
```
User → Methods → Private Data
```

---

## 3️⃣ Inheritance (Parent → Child)

Inheritance allows a child class to **reuse parent class features**.

### 🔹 Real World Example
Savings Account and Current Account are types of Bank Accounts.

### 🔹 Python Example

```python
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self.get_balance() * 0.05
        self.deposit(interest)
```

```python
savings = SavingsAccount("Guna", 10000)
savings.add_interest()
print(savings.get_balance())
```

### 🖼️ Diagram
```
BankAccount
     |
SavingsAccount
```

---

## 4️⃣ Polymorphism (Many Forms)

Polymorphism means **same method name but different behavior**.

### 🔹 Real World Example
Withdraw rules differ for Savings and Current accounts.

### 🔹 Python Example

```python
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        self._BankAccount__balance -= amount
        print(f"Withdrawn ₹{amount} (Overdraft allowed)")
```

```python
current = CurrentAccount("Guna", 2000)
current.withdraw(5000)
print(current.get_balance())
```

### 🖼️ Diagram
```
withdraw()
  |-- SavingsAccount
  |-- CurrentAccount
```

---

## 5️⃣ Abstraction (Hide Implementation)

Abstraction shows **what to do** and hides **how it is done**.

### 🔹 Real World Example
ATM machine

### 🔹 Python Example

```python
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass
```

```python
class DemoAccount(Account):
    def withdraw(self, amount):
        print(f"Withdrawing ₹{amount}")
```

---

## 🔶 OOPS Summary Table

| Concept | Purpose | Example |
|-------|--------|--------|
| Class | Blueprint | BankAccount |
| Object | Instance | Guna's account |
| Encapsulation | Data security | Private balance |
| Inheritance | Code reuse | SavingsAccount |
| Polymorphism | Flexibility | withdraw() |
| Abstraction | Hide logic | ATM |

---

# 🎯 OOPS Interview Questions (Python)

### Beginner
1. What is OOPS?
2. Difference between class and object?
3. What is `__init__` method?
4. What is encapsulation?

### Intermediate
5. Difference between inheritance and composition?
6. What is method overriding?
7. What is polymorphism with example?
8. What are access modifiers in Python?

### Advanced
9. What is abstraction? Why use `abc` module?
10. Difference between abstraction and encapsulation?
11. What is multiple inheritance? Is it supported in Python?
12. Explain Method Resolution Order (MRO).

---

## ✅ One‑Line Explanation
> OOPS helps us model real‑world problems into reusable, secure, and maintainable code using classes and objects.

---

📌 **Recommended Practice:**
- Student Management System
- Employee Payroll System
- ATM Simulation

---

Happy Learning 🚀

## ---

# 🧠 OOPS Interview Questions – Python

Short, **interview‑ready answers** with **small Python examples**.

---

## 🔰 Beginner Level

### 1️⃣ What is OOPS?

**OOPS (Object Oriented Programming System)** is a programming approach that models real‑world entities using **classes and objects**.

```python
class Car:
    pass
```

---

### 2️⃣ Difference between Class and Object

| Class                | Object           |
| -------------------- | ---------------- |
| Blueprint            | Real instance    |
| No memory allocation | Memory allocated |

```python
class Student:
    pass

s1 = Student()  # object
```

---

### 3️⃣ What is `__init__` method?

`__init__` is a **constructor** used to initialize object data.

```python
class User:
    def __init__(self, name):
        self.name = name
```

---

### 4️⃣ What is Encapsulation?

Encapsulation means **hiding internal data** and accessing it via methods.

```python
class Account:
    def __init__(self):
        self.__balance = 1000  # private
```

---

## ⚙️ Intermediate Level

### 5️⃣ Difference between Inheritance and Composition

| Inheritance       | Composition        |
| ----------------- | ------------------ |
| IS‑A relationship | HAS‑A relationship |
| Tight coupling    | Loose coupling     |

```python
# Inheritance
class Animal:
    pass
class Dog(Animal):
    pass

# Composition
class Engine:
    pass
class Car:
    def __init__(self):
        self.engine = Engine()
```

---

### 6️⃣ What is Method Overriding?

When a child class **redefines a parent method**.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

---

### 7️⃣ What is Polymorphism with example?

Same method name, **different behavior**.

```python
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")
```

---

### 8️⃣ What are Access Modifiers in Python?

| Modifier  | Syntax | Scope                |
| --------- | ------ | -------------------- |
| Public    | name   | Everywhere           |
| Protected | _name  | Within class & child |
| Private   | __name | Within class         |

```python
class Demo:
    def __init__(self):
        self.public = 1
        self._protected = 2
        self.__private = 3
```

---

## 🚀 Advanced Level

### 9️⃣ What is Abstraction? Why use `abc` module?

Abstraction hides implementation and enforces method rules.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

---

### 🔟 Difference between Abstraction and Encapsulation

| Abstraction  | Encapsulation        |
| ------------ | -------------------- |
| Hide logic   | Hide data            |
| Design level | Implementation level |

---

### 1️⃣1️⃣ What is Multiple Inheritance? Is it supported in Python?

Yes, Python supports **multiple inheritance**.

```python
class A:
    pass
class B:
    pass
class C(A, B):
    pass
```

---

### 1️⃣2️⃣ Explain Method Resolution Order (MRO)

MRO decides the **order in which methods are searched** in inheritance.

```python
class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(C.mro())
```

---

## ✅ One‑Line Explanation

> OOPS helps us model real‑world problems into reusable, secure, and maintainable code using classes and objects.

---

📌 **Interview Tip:**
Always explain OOPS answers using **real‑world examples** like Bank, Car, Student, or Employee.

Happy Interview Preparation 🚀
