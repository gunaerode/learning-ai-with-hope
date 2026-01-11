# AI Domains and Learning Types

## 1. Machine Learning

**Common Data:** Numbers, Structured data

| Type | Usage | Example |
|------|------|---------|
| Supervised | Very Common | House price prediction, Spam detection |
| Semi-Supervised | Common | Customer classification with few labels |
| Unsupervised | Common | Customer clustering, Market segmentation |

---

## 2. Deep Learning

**Common Data:** Images, Audio, Video, Numbers

| Type | Usage | Example |
|------|------|---------|
| Supervised | Very Common | Image classification, Face recognition |
| Semi-Supervised | Common | Medical imaging with few labels |
| Unsupervised | Rare | Autoencoders, Feature extraction |

---

## 3. Natural Language Processing (NLP)

**Common Data:** Text

| Type | Usage | Example |
|------|------|---------|
| Supervised | Very Common | Sentiment analysis, Translation |
| Semi-Supervised | Common | Text classification with limited labels |
| Unsupervised | Rare | Topic modeling, Word clustering |

---

## 4. Time Series Analysis

**Common Data:** Date, Time-based data

| Type | Usage | Example |
|------|------|---------|
| Supervised | Very Common | Sales forecasting |
| Semi-Supervised | Common | Failure prediction |
| Unsupervised | Common | Anomaly detection |

---

## Quick Summary

| Domain | Supervised | Semi-Supervised | Unsupervised |
|------|-----------|---------------|-------------|
| Machine Learning | ✅ | ✅ | ✅ |
| Deep Learning | ✅ | ✅ | ⚠️ Rare |
| NLP | ✅ | ✅ | ⚠️ Rare |
| Time Series | ✅ | ✅ | ✅ |


# Time Series Learning Summary

## Core Idea
Time Series problems **mostly use Regression** because the output is numeric.

### Examples
- Sales → 1200 units
- Stock Price → ₹1450
- Temperature → 31.8°C

---

## Learning Types in Time Series

| Task | Learning Type | Output |
|-----|-------------|--------|
Forecasting | Supervised | Number (Regression) |
Anomaly Detection | Unsupervised | Pattern / Outlier |
Trend Discovery | Unsupervised | Pattern |

---

## Final Rule
**Time Series = Mostly Regression + Some Unsupervised for pattern detection**
