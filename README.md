# 📄 Resume Parser with NLP & Analytics Dashboard

A Python-based tool that extracts and analyzes resume data using **Natural Language Processing (spaCy)**, stores it in **SQLite**, and visualizes insights through a **Flask-based web dashboard**.

---

## 📌 Features

- ✅ **PDF Resume Parsing** – Extracts name, email, skills, education, and experience  
- ✅ **NLP-Powered Analysis** – Uses `spaCy` for named entity recognition (NER)  
- ✅ **SQL Database** – Stores parsed data in `SQLite` (can be upgraded to PostgreSQL)  
- ✅ **Interactive Dashboard** – Flask app with visual analytics using Matplotlib  
- ✅ **Easy Upload Interface** – Simple UI to upload and process multiple resumes  

---

## 🛠 Tech Stack

- 🐍 Python  
- 🧠 spaCy (NLP)  
- 🌐 Flask (Web Framework)  
- 🗃️ SQLite (Database)  
- 📊 Matplotlib (Visualizations)  
- 📄 PyPDF2 (PDF Text Extraction)

---

## 🚀 Quick Setup

### 🔁 Clone the Repository

```
git clone https://github.com/yourusername/resume-parser.git  
cd resume-parser
```

### 🧪 Set Up Virtual Environment

```
python -m venv venv

# For Linux/macOS:
source venv/bin/activate

# For Windows:
venv\Scripts\activate
```

### 📦 Install Dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### ▶️ Run the App

```
python app.py
```

Then open your browser:

```
http://localhost:5000
```

---

## 📂 Project Structure

```
resume-parser/
├── app.py              # Flask app and route handling
├── parser.py           # NLP resume parser logic (spaCy + PyPDF2)
├── analytics.py        # Visualization logic (matplotlib)
├── schema.sql          # SQLite schema
├── templates/
│   └── dashboard.html  # Dashboard template
├── uploads/            # Uploaded resume files
├── resumes.db          # SQLite database (auto-generated)
└── requirements.txt    # Python dependencies
```

---

## 📊 Sample Output

Parsed Resume Example:

```
Name       : John Doe  
Email      : john@example.com  
Skills     : Python, SQL, Machine Learning  
Experience : 3 years
```

Dashboard includes:
- 📈 Skill frequency distribution  
- ⏳ Experience vs skill correlation  
- 🧑 Candidate summaries  

---

## 📈 Future Improvements

- 🔐 Add user authentication using Flask-Login  
- ☁️ Deploy to cloud (Render, Heroku, or Railway)  
- 🧠 Improve NLP accuracy using custom-trained spaCy models  
- 📎 Add support for DOCX and JSON resume formats  

---

