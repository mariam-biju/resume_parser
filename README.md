# Resume Parser with NLP & Analytics Dashboard
A Python-based tool that extracts and analyzes resume data using NLP (spaCy), stores it in SQLite, and visualizes insights via a Flask web dashboard.

# 📌 Features
✔ PDF Resume Parsing - Extracts name, email, skills, education, and experience

✔ NLP-Powered Analysis - Uses spaCy for entity recognition

✔ SQL Database - Stores parsed data in SQLite (can be upgraded to PostgreSQL)

✔ Interactive Dashboard - Flask web app with Matplotlib visualizations

✔ Easy Upload - Simple UI to upload and process resumes


# 🛠 Tech Stack

Python (Backend Logic)

spaCy (NLP Processing)

Flask (Web Framework)

SQLite (Database)

Matplotlib (Data Visualization)

PyPDF2 (PDF Text Extraction)

# 🚀 Quick Setup

1. Clone the Repository

bash

git clone https://github.com/yourusername/resume-parser.git

cd resume-parser

2. Set Up a Virtual Environment
   
bash

python -m venv venv

source venv/bin/activate  # Linux/Mac

venv\Scripts\activate     # Windows

3. Install Dependencies
   
bash

pip install -r requirements.txt

python -m spacy download en_core_web_sm

4. Run the Application
   
bash

python app.py

➡ Open http://localhost:5000 in your browser.

# 📂 Project Structure

resume-parser/  
├── app.py                # Flask web server  
├── parser.py             # Resume parsing logic  
├── analytics.py          # Data visualization  
├── schema.sql            # Database schema  
├── templates/            # HTML templates  
│   └── dashboard.html    # Dashboard UI  
├── uploads/              # Stores uploaded resumes  
├── resumes.db            # SQLite database (auto-generated)  
└── requirements.txt      # Dependencies  

# 📊 Sample Outputs

1. Parsed Resume Data (SQLite)
   
Name	    Email	            Skills	                      Experience (Years)

John Doe	john@example.com	Python, SQL, Machine Learning	 3

2. Dashboard Screenshot
   
Dashboard Preview (Screenshot 2025-05-26 115243.png)

# 📈 Future Improvements

🔹 Add user authentication (Flask-Login)

🔹 Deploy on cloud (Heroku / Render)

🔹 Improve NLP accuracy (Custom spaCy model)

🔹 Support DOCX/JSON resumes

