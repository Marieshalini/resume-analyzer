# 🧠 AI Resume Screening & Job Match Analyzer

An AI-powered web application that analyzes resumes and evaluates their suitability for different job roles using **NLP-based skill extraction and hybrid scoring**.

---

## 📌 Project Overview

Recruiters often spend significant time manually screening resumes.
This project automates the **initial resume screening process** by:

* Extracting skills from resumes (PDF or text)
* Matching them against predefined job roles
* Calculating a job match score
* Identifying missing skills and learning gaps

The system provides **explainable and realistic job-fit insights**, similar to real ATS (Applicant Tracking Systems).

---

## ✨ Key Features

* 📄 Upload resume as **PDF** or paste resume **text**
* 🎯 Select predefined **job roles**
* 🧠 NLP-based **skill extraction**
* 📊 **Hybrid job match scoring**
* ❌ Missing skill identification
* ✅ Matched skill visualization
* 🌐 Clean Flask-based web interface

---

## 🧠 AI & NLP Concepts Used

* Natural Language Processing (NLP)
* Rule-based skill extraction
* TF-IDF Vectorization
* Cosine Similarity
* Hybrid scoring logic (skills + contextual relevance)
* Explainable AI outputs

---

## 🧮 How the Job Match Score is Calculated

The final job match score is a **hybrid score**:

* 75% Skill Match Score
* 25% Contextual Similarity (TF-IDF)

### Skill Match Score

Skill Score = (Matched Skills / Total Job Skills) *100


### Final Score

Final Score = (0.75 x Skill Score) + (0.25 x TF-IDF Score)

This approach ensures:

* Required skills determine eligibility
* Contextual relevance prevents keyword stuffing

---

## 🛠 Tech Stack

Python
Flask
Scikit-learn
NLTK / Regex
PyPDF2
HTML, CSS

---

## 📁 Project Structure

```
resume-analyzer/
│
├── app.py
├── requirements.txt
│
├── ai_engine/
│   ├── matcher.py
│   ├── skills.py
│
├── resume_parser/
│   ├── pdf_reader.py
│   ├── text_cleaner.py
│
├── data/
│   └── jobs.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── uploads/
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install flask scikit-learn pandas nltk PyPDF2
```

### 2️⃣ Run the application

```bash
py app.py
```

### 3️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧪 Example Use Case

* Upload a resume (PDF or text)
* Select **Web Developer**
* View:

  * Job match percentage
  * Matched skills
  * Missing skills
  * Skill gap insights

---


## 👩‍💻 Author

Marie Shalini S