from flask import Flask, render_template, request, session
from resume_parser.pdf_reader import extract_text_from_pdf
from resume_parser.text_cleaner import clean_text
from ai_engine.skills import extract_skills
from data.jobs import JOBS
from ai_engine.matcher import (
    skill_match_score,
    tfidf_similarity,
    final_match_score
)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = "resume_analyzer_secret"

@app.route('/', methods=['GET', 'POST'])
def index():
    match_score = None
    resume_skills = []
    job_skills = []
    matched_skills = []
    missing_skills = []
    job_role = None   # ✅ FIX 1: define early

    if request.method == 'POST':
        job_role = request.form.get('job_role')

        if not job_role or job_role not in JOBS:
            return render_template('index.html')

        job_text = JOBS[job_role]

        # ===== RESUME HANDLING =====
        if 'resume_pdf' in request.files and request.files['resume_pdf'].filename != "":
            pdf = request.files['resume_pdf']
            pdf_path = f"{app.config['UPLOAD_FOLDER']}/{pdf.filename}"
            pdf.save(pdf_path)

            resume_text = extract_text_from_pdf(pdf_path)
            resume_text = clean_text(resume_text)
            session['resume_text'] = resume_text

        elif 'resume_text' in session:
            resume_text = session['resume_text']

        else:
            resume_text = clean_text(request.form.get('resume_text', ""))
            session['resume_text'] = resume_text

        # ===== AI LOGIC =====
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_text)

        skill_score = skill_match_score(resume_skills, job_skills)
        tfidf_score = tfidf_similarity(resume_text, job_text)
        match_score = final_match_score(skill_score, tfidf_score)

        matched_skills = sorted(set(resume_skills) & set(job_skills))
        missing_skills = sorted(set(job_skills) - set(resume_skills))

    return render_template(
        'index.html',
        score=match_score,
        matched=matched_skills,
        missing=missing_skills,
        job_role=job_role
    )


if __name__ == '__main__':
    app.run(debug=True)
