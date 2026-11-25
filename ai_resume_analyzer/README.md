# 🎯 AI Resume Analyzer

> **An intelligent, NLP-powered Resume Analysis tool built with Python and Streamlit.**
> Get your ATS score, find skill gaps, and receive actionable improvement tips — in seconds.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.20-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📸 Features

| Feature | Description |
|---|---|
| 📄 **Resume Upload** | Upload PDF or DOCX resumes |
| 🔍 **Text Extraction** | Automatic text extraction using PyPDF2 & python-docx |
| 🧠 **Skill Analysis** | NLP-based skill matching across 6 job roles |
| 📊 **ATS Score** | Weighted ATS score out of 100 with breakdown |
| 🎯 **Job Role Matching** | Compare skills against 6 tech roles |
| ❌ **Missing Skills** | See exactly what skills to add per category |
| 💡 **AI Suggestions** | Personalised improvement recommendations |
| 📈 **Charts** | Gauge meter, radar chart, bar chart, donut chart |
| 💪 **Strengths & Weaknesses** | Automated SWOT-style analysis |
| 📥 **PDF Report** | Download full analysis as a styled PDF |

---

## 🗂️ Project Structure

```
ai_resume_analyzer/
│
├── app.py                      # Main Streamlit application (run this)
├── job_roles.py                # Skills database for all job roles
├── requirements.txt            # Python dependencies
├── create_sample_resumes.py    # Generate sample resumes for testing
│
├── utils/
│   ├── __init__.py             # Package marker
│   ├── text_extractor.py       # PDF/DOCX text extraction
│   ├── skills_analyzer.py      # Core analysis engine + ATS scoring
│   ├── charts.py               # Plotly chart generators
│   └── pdf_report.py           # Downloadable PDF report generator
│
└── sample_resumes/
    ├── sample_data_scientist.pdf
    ├── sample_fullstack_developer.pdf
    ├── sample_python_developer.docx
    └── sample_data_scientist_resume.txt   # Reference text
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### Step 2 — Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Create Sample Resumes (Optional)

```bash
python create_sample_resumes.py
```
This generates 3 sample resumes in the `sample_resumes/` folder for testing.

### Step 5 — Run the Application

```bash
streamlit run app.py
```

The app opens automatically at **http://localhost:8501**

---

## 🎯 Supported Job Roles

| Role | Key Skills Evaluated |
|---|---|
| 🔬 **Data Scientist** | Python, ML, Deep Learning, Statistics, SQL, Visualization |
| 🤖 **AI Engineer** | LLMs, MLOps, PyTorch, FastAPI, Docker, RAG |
| 🌐 **Full Stack Developer** | React, Node.js, SQL, Docker, AWS, CI/CD |
| 🐍 **Python Developer** | Django, FastAPI, OOP, Pytest, PostgreSQL |
| 🎨 **Frontend Developer** | HTML/CSS, React, TypeScript, Tailwind, Testing |
| ⚙️ **DevOps Engineer** | Docker, Kubernetes, Terraform, CI/CD, Monitoring |

---

## 📊 ATS Score Breakdown

The ATS score is calculated using 4 weighted components:

```
ATS Score (out of 100)
├── Skill Match        → 60 points  (weighted by category importance)
├── Resume Structure   → 15 points  (sections: summary, skills, projects, etc.)
├── Action Verbs       → 15 points  (built, led, optimized, deployed, etc.)
└── Keyword Density    → 10 points  (skill mentions per 100 words)
```

| Score Range | Rating |
|---|---|
| 80 – 100 | 🟢 Excellent |
| 60 – 79  | 🔵 Good |
| 40 – 59  | 🟡 Average |
| 0 – 39   | 🔴 Needs Work |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python 3.10+** | Core programming language |
| **Streamlit** | Web UI framework |
| **PyPDF2** | PDF text extraction |
| **python-docx** | DOCX text extraction |
| **Plotly** | Interactive charts (gauge, radar, bar, donut) |
| **FPDF2** | PDF report generation |
| **Pandas** | Data handling |
| **Regex (re)** | Skill keyword matching |

---

## 📚 How It Works (For Beginners)

```
User uploads resume (PDF/DOCX)
          ↓
text_extractor.py → Reads the file, extracts plain text
          ↓
skills_analyzer.py → Compares text against job role skill database
          ↓
          ├── analyze_skills()     → Which skills match / are missing?
          ├── calculate_ats_score() → Weighted score out of 100
          ├── generate_suggestions() → Personalised tips
          └── get_strengths_weaknesses() → SWOT summary
          ↓
charts.py → Generate Plotly visualizations
          ↓
app.py → Display everything in Streamlit UI
          ↓
pdf_report.py → User downloads PDF report
```

---

## 📝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

Built with ❤️ as a portfolio project demonstrating Python, NLP, Streamlit, and Data Visualization skills.

*If this project helped you, please give it a ⭐ on GitHub!*
