import sqlite3
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg to avoid GUI threading issues
import matplotlib.pyplot as plt
from io import BytesIO
import base64

class ResumeAnalytics:
    def __init__(self, db_path="resumes.db"):
        self.conn = sqlite3.connect(db_path)
    
    def get_skills_distribution(self):
        """Generate skills distribution plot as base64 encoded image"""
        df = pd.read_sql("""
            SELECT value as skill, COUNT(*) as count 
            FROM candidates, json_each('["' || replace(skills, ', ', '","') || '"]')
            GROUP BY skill
            ORDER BY count DESC
            LIMIT 10
        """, self.conn)
        
        plt.figure(figsize=(10,6))
        df.plot(kind='bar', x='skill', y='count')
        plt.title("Top Skills in Resumes")
        plt.tight_layout()
        
        # Save plot to bytes buffer
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        plt.close()
        img_buffer.seek(0)
        return base64.b64encode(img_buffer.read()).decode('utf-8')
    
    def experience_distribution(self):
        """Generate experience distribution plot as base64 encoded image"""
        df = pd.read_sql("SELECT experience FROM candidates", self.conn)
        
        plt.figure(figsize=(10,6))
        df['experience'].plot(kind='hist', bins=10)
        plt.title("Years of Experience Distribution")
        plt.xlabel("Years")
        
        # Save plot to bytes buffer
        img_buffer = BytesIO()
        plt.savefig(img_buffer, format='png')
        plt.close()
        img_buffer.seek(0)
        return base64.b64encode(img_buffer.read()).decode('utf-8')
    
    def get_skills_data(self):
        """Get skills data as a list of dictionaries"""
        df = pd.read_sql("""
            SELECT value as skill, COUNT(*) as count 
            FROM candidates, json_each('["' || replace(skills, ', ', '","') || '"]')
            GROUP BY skill
            ORDER BY count DESC
            LIMIT 10
        """, self.conn)
        return df.to_dict('records')
    
    def get_experience_data(self):
        """Get experience data as a list"""
        df = pd.read_sql("SELECT experience FROM candidates", self.conn)
        return df['experience'].tolist()
    
    def close(self):
        self.conn.close()