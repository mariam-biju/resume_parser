from flask import Flask, render_template, request, redirect, url_for
from parser import ResumeParser
from analytics import ResumeAnalytics
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

@app.route('/')
def index():
    analyzer = ResumeAnalytics()
    try:
        # Get plot images as base64
        skills_plot = analyzer.get_skills_distribution()
        exp_plot = analyzer.experience_distribution()
        
        # Get raw data for tables if needed
        skills_data = analyzer.get_skills_data()
        exp_data = analyzer.get_experience_data()
        
        return render_template(
            'dashboard.html',
            skills_plot=skills_plot,
            exp_plot=exp_plot,
            skills_data=skills_data,
            exp_data=exp_data
        )
    except Exception as e:
        print(f"Error generating analytics: {e}")
        return render_template('error.html', error=str(e))
    finally:
        analyzer.close()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return redirect(request.url)
    
    file = request.files['resume']
    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.pdf'):
        try:
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            parser = ResumeParser()
            text = parser.extract_text(filepath)
            if text:
                data = parser.parse_resume(text)
                if data:
                    parser.save_to_db(data)
            parser.close()
            
            return redirect(url_for('index'))
        except Exception as e:
            return render_template('error.html', error=str(e))
    
    return "Invalid file format", 400

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)