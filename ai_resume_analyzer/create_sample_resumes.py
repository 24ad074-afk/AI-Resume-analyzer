"""
create_sample_resumes.py
PURPOSE: Generate sample PDF and DOCX resume files for testing
         the AI Resume Analyzer. Run this once before starting the app.

Usage:
    python create_sample_resumes.py
"""

from fpdf import FPDF
import docx as python_docx
import os

OUTPUT_DIR = "sample_resumes"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ── Helper to add styled text ──────────────────────────────────
def add_section(pdf, title):
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_fill_color(240, 240, 255)
    pdf.set_text_color(60, 60, 150)
    pdf.cell(0, 8, title, ln=True, fill=True)
    pdf.set_text_color(30, 30, 30)
    pdf.set_font("Helvetica", "", 10)


def add_line(pdf, text, bold=False):
    pdf.set_font("Helvetica", "B" if bold else "", 10)
    pdf.multi_cell(0, 6, text)


# ═══════════════════════════════════════════════════════════════
# Sample 1: Data Scientist Resume (PDF)
# ═══════════════════════════════════════════════════════════════
def create_data_scientist_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(18, 18, 18)

    # Name
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(60, 60, 150)
    pdf.cell(0, 10, "ARJUN MEHTA", ln=True, align="C")

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, "arjun.mehta@email.com | +91 98765 43210 | linkedin.com/in/arjunmehta | github.com/arjunmehta", ln=True, align="C")
    pdf.ln(3)

    add_section(pdf, "SUMMARY")
    add_line(pdf, "Motivated Computer Science student with strong Python programming skills and experience in machine learning and data analysis. Skilled in building predictive models, exploratory data analysis, and data visualization. Seeking a Data Scientist role.")
    pdf.ln(2)

    add_section(pdf, "EDUCATION")
    add_line(pdf, "B.E. Computer Science Engineering | PSG College of Technology, Coimbatore | 2021-2025", bold=True)
    add_line(pdf, "CGPA: 8.6/10 | Coursework: Machine Learning, Statistics, Data Structures, DBMS")
    pdf.ln(2)

    add_section(pdf, "SKILLS")
    add_line(pdf, "Programming: Python, SQL, R")
    add_line(pdf, "Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras, XGBoost")
    add_line(pdf, "Tools: Jupyter Notebook, Git, GitHub, Tableau, Power BI")
    add_line(pdf, "Databases: MySQL, MongoDB, PostgreSQL")
    add_line(pdf, "Cloud: AWS, Google Cloud Platform (GCP)")
    add_line(pdf, "Concepts: Machine Learning, Deep Learning, EDA, Statistics, Hypothesis Testing, Time Series, NLP")
    pdf.ln(2)

    add_section(pdf, "EXPERIENCE")
    add_line(pdf, "Data Science Intern | IntelliSoft Analytics, Coimbatore | Jun 2024 - Aug 2024", bold=True)
    add_line(pdf, "- Analyzed sales datasets of 500,000+ records using Pandas and NumPy to uncover business trends")
    add_line(pdf, "- Built customer churn prediction model using Random Forest achieving 87% accuracy")
    add_line(pdf, "- Designed interactive Tableau dashboards adopted by the analytics team")
    add_line(pdf, "- Collaborated with senior data scientists to implement feature engineering pipelines")
    pdf.ln(1)
    add_line(pdf, "Machine Learning Intern | TechVenture Labs | Dec 2023 - Feb 2024", bold=True)
    add_line(pdf, "- Developed sentiment analysis pipeline using NLP for 10,000+ product reviews")
    add_line(pdf, "- Implemented classification algorithms (Logistic Regression, SVM, Decision Tree)")
    add_line(pdf, "- Automated data cleaning scripts reducing preprocessing time by 35%")
    pdf.ln(2)

    add_section(pdf, "PROJECTS")
    add_line(pdf, "1. House Price Prediction | Python, Scikit-learn, Pandas, Flask", bold=True)
    add_line(pdf, "   Built end-to-end regression model with 92% R2 score. Deployed as REST API on AWS EC2.")
    add_line(pdf, "2. Customer Churn Dashboard | Python, Streamlit, Plotly, XGBoost", bold=True)
    add_line(pdf, "   Interactive web dashboard for telecom churn analysis. 89% model accuracy.")
    add_line(pdf, "3. Image Classification with CNN | TensorFlow, Keras", bold=True)
    add_line(pdf, "   CNN on CIFAR-10 dataset achieving 91% accuracy. Applied transfer learning with VGG16.")
    pdf.ln(2)

    add_section(pdf, "CERTIFICATIONS")
    add_line(pdf, "- IBM Data Science Professional Certificate | Coursera | 2024")
    add_line(pdf, "- Machine Learning Specialization | Andrew Ng, Coursera | 2023")
    add_line(pdf, "- AWS Cloud Practitioner Essentials | Amazon Web Services | 2024")
    pdf.ln(2)

    add_section(pdf, "ACHIEVEMENTS")
    add_line(pdf, "- Top 5% rank in Kaggle House Price Prediction competition (2,000+ participants)")
    add_line(pdf, "- Winner - Smart India Hackathon 2023 (AI track)")
    add_line(pdf, "- Published paper on ML-based Crop Disease Detection at International Conference 2024")

    pdf.output(f"{OUTPUT_DIR}/sample_data_scientist.pdf")
    print(f"Created: {OUTPUT_DIR}/sample_data_scientist.pdf")


# ═══════════════════════════════════════════════════════════════
# Sample 2: Full Stack Developer Resume (PDF)
# ═══════════════════════════════════════════════════════════════
def create_fullstack_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(18, 18, 18)

    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(20, 120, 80)
    pdf.cell(0, 10, "PRIYA KRISHNAMURTHY", ln=True, align="C")
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 6, "priya.k@email.com | +91 90876 54321 | github.com/priyak | Chennai, India", ln=True, align="C")
    pdf.ln(3)

    add_section(pdf, "SUMMARY")
    add_line(pdf, "Full Stack Developer with 2 years experience building scalable web applications using React, Node.js, and cloud technologies. Passionate about clean code, system design, and delivering user-centric products.")
    pdf.ln(2)

    add_section(pdf, "SKILLS")
    add_line(pdf, "Frontend: HTML5, CSS3, JavaScript, TypeScript, React, Next.js, Tailwind, Bootstrap")
    add_line(pdf, "Backend: Node.js, Express, Python, Django, REST API, GraphQL, Microservices")
    add_line(pdf, "Databases: MySQL, PostgreSQL, MongoDB, Redis, Firebase")
    add_line(pdf, "DevOps: Docker, Kubernetes, AWS, CI/CD, GitHub Actions, Nginx, Linux")
    add_line(pdf, "Testing: Jest, Pytest, Selenium, TDD, Unit Testing")
    add_line(pdf, "Tools: Git, GitHub, Agile, Scrum, VS Code, Postman")
    pdf.ln(2)

    add_section(pdf, "EXPERIENCE")
    add_line(pdf, "Junior Full Stack Developer | Zoho Corporation, Chennai | Jul 2023 - Present", bold=True)
    add_line(pdf, "- Built and deployed 3 customer-facing features in React + Node.js serving 50,000 users")
    add_line(pdf, "- Implemented CI/CD pipeline using GitHub Actions, reducing deployment time by 40%")
    add_line(pdf, "- Led migration of legacy PHP modules to modern Node.js microservices")
    add_line(pdf, "- Optimized PostgreSQL queries reducing average response time by 55%")
    pdf.ln(2)

    add_section(pdf, "PROJECTS")
    add_line(pdf, "1. E-Commerce Platform | React, Node.js, MongoDB, AWS", bold=True)
    add_line(pdf, "   Full stack e-commerce app with payment integration, deployed on AWS EC2.")
    add_line(pdf, "2. Task Management App | Next.js, TypeScript, PostgreSQL, Docker", bold=True)
    add_line(pdf, "   Real-time task board with WebSocket, Docker containerization and Kubernetes deployment.")
    pdf.ln(2)

    add_section(pdf, "EDUCATION")
    add_line(pdf, "B.Tech IT | Anna University | 2019-2023 | CGPA: 8.2/10", bold=True)
    pdf.ln(2)

    add_section(pdf, "CERTIFICATIONS")
    add_line(pdf, "- AWS Solutions Architect Associate | 2024")
    add_line(pdf, "- Meta Front-End Developer Professional Certificate | Coursera | 2023")

    pdf.output(f"{OUTPUT_DIR}/sample_fullstack_developer.pdf")
    print(f"Created: {OUTPUT_DIR}/sample_fullstack_developer.pdf")


# ═══════════════════════════════════════════════════════════════
# Sample 3: Python Developer (DOCX)
# ═══════════════════════════════════════════════════════════════
def create_python_dev_docx():
    doc = python_docx.Document()

    # Title
    title = doc.add_heading("RAHUL SHARMA", level=1)
    title.alignment = 1  # Center
    doc.add_paragraph("rahul.sharma@email.com | Bengaluru, India | github.com/rahulsharma")

    doc.add_heading("SUMMARY", level=2)
    doc.add_paragraph(
        "Python Developer with 1 year of experience building REST APIs, automation scripts, "
        "and data processing tools. Proficient in Django, FastAPI, and PostgreSQL. "
        "Strong foundation in OOP, data structures, and software design patterns."
    )

    doc.add_heading("SKILLS", level=2)
    doc.add_paragraph("Core Python: Python, OOP, Asyncio, Decorators, Generators, Type Hints")
    doc.add_paragraph("Web Frameworks: Django, Flask, FastAPI, REST API, GraphQL")
    doc.add_paragraph("Data: Pandas, NumPy, SQL, CSV, JSON, Web Scraping, BeautifulSoup")
    doc.add_paragraph("Databases: PostgreSQL, MySQL, MongoDB, Redis, SQLAlchemy, ORM")
    doc.add_paragraph("Testing: Pytest, Unittest, TDD, Code Review, PEP8, Linting")
    doc.add_paragraph("DevOps: Docker, Git, Linux, Bash, CI/CD, AWS, Virtualenv, Pip")

    doc.add_heading("EXPERIENCE", level=2)
    doc.add_paragraph("Python Developer | StartupX, Bengaluru | Jan 2024 - Present").bold = True
    doc.add_paragraph("- Developed and maintained 5 REST API endpoints using FastAPI serving 20,000 users")
    doc.add_paragraph("- Built automation scripts reducing manual data entry by 70%")
    doc.add_paragraph("- Implemented ORM-based database layer using SQLAlchemy with PostgreSQL")
    doc.add_paragraph("- Wrote comprehensive Pytest test suite achieving 85% code coverage")

    doc.add_heading("PROJECTS", level=2)
    doc.add_paragraph("1. Blog Platform API | Django, PostgreSQL, Docker").bold = True
    doc.add_paragraph("   RESTful API with JWT authentication, deployed with Docker and CI/CD via GitHub Actions.")
    doc.add_paragraph("2. Data Scraper Tool | Python, BeautifulSoup, Scrapy, Pandas").bold = True
    doc.add_paragraph("   Scraped and analyzed 100,000+ e-commerce listings with automated reporting.")

    doc.add_heading("EDUCATION", level=2)
    doc.add_paragraph("B.E. Computer Science | RV College of Engineering, Bengaluru | 2019-2023")

    doc.add_heading("CERTIFICATIONS", level=2)
    doc.add_paragraph("- Python Professional Certificate | PCEP, Python Institute | 2023")
    doc.add_paragraph("- Django REST Framework | Udemy | 2024")

    doc.save(f"{OUTPUT_DIR}/sample_python_developer.docx")
    print(f"Created: {OUTPUT_DIR}/sample_python_developer.docx")


# ── Run all ────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Creating sample resumes…")
    create_data_scientist_pdf()
    create_fullstack_pdf()
    create_python_dev_docx()
    print("\nAll sample resumes created in:", OUTPUT_DIR)
    print("Upload them to the app to test different job roles!")
