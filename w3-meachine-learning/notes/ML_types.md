# 🧠 Machine Learning Types

---

## 🔵 Supervised Learning

**Requirement:** Labeled data  
**Input:** Known  
**Output:** Known  

### 2D Representation
```
Class A:  ● ● ● ●
Class B:  ▲ ▲ ▲ ▲
```

**Goal:** Learn the mapping  
```
New point ● → Class A
```
`Input → Output`

**Example:**  
Email → Spam / Not Spam

---

## 🟢 Unsupervised Learning

**Requirement:** Only raw data (no labels)  
**Input:** Known  
**Output:** Unknown  

### 2D Representation
```
● ● ● ●      ▲ ▲ ▲ ▲
● ● ●        ▲ ▲ ▲
```

Model discovers:
```
Cluster 1      Cluster 2
```

**Goal:** Find patterns and clusters  

**Example:**  
Customer segmentation

---

## 🟡 Semi-Supervised Learning

**Requirement:** Few labeled data + many unlabeled data  
**Input:** Known  
**Output:** Partially known  

### 2D Representation
```
● ● Labeled        ▲ ▲ Labeled
● ● ● ● ? ?        ▲ ▲ ▲ ? ?
```

**Goal:** Use small labeled data to guide learning on large unlabeled data

---

## ✨ Quick Summary

| Type | Input Known | Output Known | Main Purpose |
|------|-------------|--------------|--------------|
| Supervised | ✅ | ✅ | Prediction |
| Unsupervised | ✅ | ❌ | Pattern discovery |
| Semi-Supervised | ✅ | 🟡 | Learning with limited labels |

---

### 🧠 In One Line
- **Supervised:** Learn with teacher  
- **Unsupervised:** Learn by observing  
- **Semi-Supervised:** Learn with little help and much observation
