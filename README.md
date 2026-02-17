# 🛡️ Phishing URL Detection System

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-green?style=for-the-badge)
![Flask](https://img.shields.io/badge/Deployment-Flask%20API-red?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> An end-to-end machine learning system to detect phishing URLs in real time — trained on **11,430 URLs**, explained with **SHAP**, and deployed via **Flask + Docker**.

---

## 📌 Project Overview

Phishing attacks are one of the most dangerous cybersecurity threats today. This project builds a complete, production-ready **Phishing URL Detection System** using a **Random Forest classifier**, demonstrating through statistical analysis and visual evidence that **single-feature detection is insufficient** — and that multivariate ML models are the future of cybersecurity.

The system accepts a URL, analyzes its structure, and returns a real-time **"Legitimate" or "Phishing"** classification with a **confidence score**.

Developed during my **Data Science Internship at Code B Solutions Pvt Ltd**.

---

## 🎯 Key Highlights

- ✅ Analyzed **11,430 URLs** — perfectly balanced (5,715 phishing + 5,715 legitimate)
- ✅ Deep **EDA** with histograms, pair plots & correlation heatmaps
- ✅ **SHAP analysis** for full model explainability
- ✅ Engineered feature `special_char_ratio` — proved significant in detecting obfuscation
- ✅ Deployed as a **Flask REST API** with a real-time HTML interface
- ✅ **Dockerized** for portability — runs on any OS without dependency conflicts

---

## 🏗️ Architecture

```
User pastes URL → HTML Interface → Flask REST API (/predict)
                                        ↓
                              Feature Extraction (57 features)
                                        ↓
                         Random Forest Model (.pkl)
                                        ↓
                    "Legitimate" or "Phishing" + Confidence Score
```

---

## 📊 Dataset Overview

| Property | Details |
|---|---|
| Total URLs | 11,430 |
| Phishing URLs | 5,715 |
| Legitimate URLs | 5,715 |
| Class Balance | ✅ Perfectly balanced — no SMOTE needed |
| Longest URL | 1,641 characters |

---

## 🔬 Descriptive Statistics — `length_url`

| Statistic | Value |
|---|---|
| Mean | 61.1 |
| Median | 55.0 |
| Std Deviation | 55.3 |
| Max | 1,641 characters |

> **Insight:** Mean > Median → **right-skewed distribution**. Phishing URLs are chaotic and unpredictable in length, requiring specific preprocessing for model accuracy.

---

## 📈 Visual Analysis

### Histograms
- **Legitimate (Blue):** Clustered tightly at 20–100 characters
- **Phishing (Orange):** Wide spread, extending to 1,641+ characters to hide malicious parameters

### Pair Plots
- Legitimate sites cluster in the **bottom-left** (low `nb_dots`, low `length_url`)
- Phishing sites are **scattered** — no strict structural rule, defeating simple rule-based detection

### Correlation Heatmap

| Feature Pair | Correlation | Insight |
|---|---|---|
| `length_url` ↔ `nb_dots` | **+0.44** | Longer URLs have more subdomains |
| `length_url` ↔ `nb_hyphens` | **+0.40** | Longer URLs use more hyphens |
| `length_url` ↔ `ratio_digits_url` | **+0.45** | Longer URLs contain more digits |
| `ratio_digits_url` ↔ `nb_dots` | **+0.22** | Low → adds **unique information** |
| `ratio_digits_url` ↔ `nb_hyphens` | **+0.11** | Very low → strong **independent signal** |

---

## 🧠 Model Explainability — SHAP Analysis

We used **SHAP (SHapley Additive exPlanations)** to interpret the Random Forest model and understand which features drive predictions.

### Top Findings:

**1. `google_index` — Most Critical Feature**
> If a site is indexed by Google, it is almost certainly safe.

**2. `special_char_ratio` — Engineered Feature**
> Phishing URLs tend to use complex punctuation characters to obfuscate their true identity. This engineered feature proved highly significant in the SHAP analysis.

**3. Why Single Features Fail**
> No single feature can perfectly separate phishing from legitimate URLs. Random Forest combines all weak signals into one strong prediction — confirmed by both EDA and SHAP.

---

## 🚀 Deployment

### Method
Deployed using **Flask** REST API at `/predict` endpoint.

### User Interface
A **real-time HTML interface** where users paste a URL and instantly receive:
- **"Legitimate"** or **"Phishing"** classification
- **Confidence score** percentage
- Visual confidence bar

### Portability
Containerized using **Docker** — runs on any OS without dependency conflicts.

---

## 🏆 Model Results

| Metric | Score |
|---|---|
| Accuracy | **89.63%** |
| Precision | **89.32%** |
| Recall | **90.03%** |
| F1 Score | **89.67%** |

> Trained on 57 URL-extractable features using Random Forest (100 estimators).
> Tested on 20% holdout set (2,286 URLs) with stratified split.

---

## ⚙️ Setup & Usage

### Option 1: Run with Python

```bash
git clone https://github.com/Khiladi-786/Phishing_Deployment.git
cd Phishing_Deployment
pip install -r requirements.txt
python app.py
# Open http://localhost:5001
```

### Option 2: Run with Docker

```bash
git clone https://github.com/Khiladi-786/Phishing_Deployment.git
cd Phishing_Deployment
docker build -t phishing-detector .
docker run -p 5001:5001 phishing-detector
# Open http://localhost:5001
```

---

## 📁 Project Structure

```
Phishing_Deployment/
│
├── app.py                       # Flask app (REST API on port 5001)
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── refined_dataset.csv          # Feature column reference
├── README.md                    # Project documentation
│
├── model/
│   └── best_phishing_model.pkl  # Trained Random Forest model
│
└── templates/
    └── index.html               # HTML user interface
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core programming language |
| Pandas & NumPy | Data manipulation & analysis |
| Scikit-learn | Random Forest model |
| SHAP | Model explainability |
| Matplotlib & Seaborn | EDA visualizations |
| Flask | REST API deployment |
| Docker | Containerization & portability |
| HTML/CSS | User interface |

---

## 🔑 Key Insight

> **"Single-feature detection is insufficient for identifying phishing URLs. Multivariate ML models like Random Forest — interpreted through SHAP — are essential for accurate, explainable, real-world cybersecurity applications."**

---

## 👨‍💻 About the Author

**Nikhil More**
B.Tech CSE (AI/ML) — University of Mumbai (2023–2027)

- 🔗 [LinkedIn](https://www.linkedin.com/in/nikhil-moretech)
- 🐙 [GitHub](https://github.com/Khiladi-786)
- 📧 morenikhil7822@gmail.com

*C-DAC Campus Ambassador | Google Student Ambassador | GfG Campus Mantri*

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **If you found this project useful, please give it a star!**
