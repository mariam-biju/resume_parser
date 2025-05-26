import re
import sqlite3
from PyPDF2 import PdfReader
import spacy
from datetime import datetime

nlp = spacy.load("en_core_web_sm")

class ResumeParser:
    def __init__(self, db_path="resumes.db"):
        """Initialize the parser with database connection"""
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
        self._initialize_database()
        
    def _initialize_database(self):
        """Create database tables if they don't exist"""
        cursor = self.conn.cursor()
        
        # Candidates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT UNIQUE,
                phone TEXT,
                skills TEXT,
                education TEXT,
                experience INTEGER,  -- in years
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Job matches table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_matches (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidate_id INTEGER,
                job_title TEXT,
                match_score REAL,
                FOREIGN KEY (candidate_id) REFERENCES candidates (id)
            )
        """)
        
        self.conn.commit()
    
    def extract_text(self, pdf_path):
        """Extract text from PDF resume"""
        try:
            reader = PdfReader(pdf_path)
            return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""
    
    def parse_resume(self, text):
        """Parse resume text and extract structured data"""
        if not text.strip():
            return None
            
        doc = nlp(text)
        
        # Extract name (first capitalized person name)
        name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), "Unknown")
        
        # Extract email
        email = re.search(r'[\w\.-]+@[\w\.-]+', text)
        email = email.group(0) if email else None
        
        # Extract phone (international format support)
        phone = re.search(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)
        phone = phone.group(0) if phone else None
        
        # Extract skills (expanded list)
        skills_keywords = [
            'python', 'sql', 'machine learning', 'flask', 'django', 
            'aws', 'java', 'c++', 'javascript', 'html', 'css',
            'tensorflow', 'pytorch', 'pandas', 'numpy', 'git'
        ]
        skills = [token.text.lower() for token in doc if token.text.lower() in skills_keywords]
        
        # Extract education
        education = []
        for sent in doc.sents:
            if any(word in sent.text.lower() for word in ['university', 'college', 'institute', 'school']):
                education.append(sent.text.strip())
        
        # Extract experience (improved pattern matching)
        exp_pattern = re.compile(r'(\d+)\+?\s*(?:years?|yrs?|year\'s?|years\'?)(?:\s.*?experience)?', re.IGNORECASE)
        experience = exp_pattern.search(text)
        experience = int(experience.group(1)) if experience else 0
        
        return {
            'name': name,
            'email': email,
            'phone': phone,
            'skills': ', '.join(set(skills)),
            'education': ' | '.join(education[:3]),  # Limit to 3 entries
            'experience': experience
        }
    
    def save_to_db(self, data):
        """Save parsed resume data to database"""
        if not data:
            return None
            
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO candidates (name, email, phone, skills, education, experience)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (data['name'], data['email'], data['phone'], 
                  data['skills'], data['education'], data['experience']))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                print(f"Duplicate resume found for email: {data['email']}")
            return None
    
    def close(self):
        """Close database connection"""
        self.conn.close()

# Example usage with error handling
if __name__ == "__main__":
    parser = None
    try:
        parser = ResumeParser()
        text = parser.extract_text("sample_resume.pdf")  # Replace with your file
        if text:
            data = parser.parse_resume(text)
            if data:
                candidate_id = parser.save_to_db(data)
                if candidate_id:
                    print(f"Successfully saved resume with ID: {candidate_id}")
                else:
                    print("Resume already exists in database")
            else:
                print("Failed to parse resume data")
        else:
            print("Failed to extract text from PDF")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if parser:
            parser.close()