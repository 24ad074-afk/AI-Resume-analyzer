# ============================================================
# job_roles.py - Skills database for each supported job role
# PURPOSE: Defines required skills for every job role that
#          the app can analyze against. Add new roles here!
# ============================================================

# Each role maps to a dict of skill categories and their keywords.
# The ATS engine searches the resume text for these keywords.

JOB_ROLES = {

    # ── Data Scientist ──────────────────────────────────────
    "Data Scientist": {
        "Core Programming": [
            "python", "r", "sql", "scala", "julia"
        ],
        "Machine Learning": [
            "machine learning", "supervised learning", "unsupervised learning",
            "regression", "classification", "clustering", "random forest",
            "xgboost", "gradient boosting", "svm", "support vector machine",
            "decision tree", "naive bayes", "knn", "k-nearest neighbor"
        ],
        "Deep Learning & AI": [
            "deep learning", "neural network", "cnn", "rnn", "lstm",
            "transformer", "bert", "gpt", "tensorflow", "keras", "pytorch"
        ],
        "Data Manipulation": [
            "pandas", "numpy", "scipy", "data wrangling", "data cleaning",
            "feature engineering", "eda", "exploratory data analysis"
        ],
        "Visualization": [
            "matplotlib", "seaborn", "plotly", "tableau", "power bi",
            "data visualization", "dashboard"
        ],
        "Statistics": [
            "statistics", "probability", "hypothesis testing", "a/b testing",
            "bayesian", "time series", "forecasting", "regression analysis"
        ],
        "Big Data & Cloud": [
            "spark", "hadoop", "hive", "aws", "azure", "gcp",
            "bigquery", "databricks", "airflow", "etl"
        ],
        "Databases": [
            "mysql", "postgresql", "mongodb", "sql server", "sqlite",
            "nosql", "database"
        ],
        "Soft Skills": [
            "communication", "problem solving", "critical thinking",
            "collaboration", "presentation"
        ],
    },

    # ── AI / ML Engineer ────────────────────────────────────
    "AI Engineer": {
        "Core Programming": [
            "python", "c++", "java", "rust", "golang"
        ],
        "AI Frameworks": [
            "tensorflow", "pytorch", "keras", "jax", "hugging face",
            "transformers", "langchain", "llm", "large language model",
            "openai", "anthropic", "gemini"
        ],
        "MLOps & Deployment": [
            "mlops", "mlflow", "kubeflow", "airflow", "docker",
            "kubernetes", "ci/cd", "model deployment", "model serving",
            "fastapi", "flask", "rest api", "grpc"
        ],
        "Cloud Platforms": [
            "aws", "azure", "gcp", "sagemaker", "vertex ai",
            "azure ml", "lambda", "ec2", "s3"
        ],
        "Data Engineering": [
            "spark", "kafka", "airflow", "etl", "data pipeline",
            "dbt", "snowflake", "databricks"
        ],
        "Machine Learning": [
            "machine learning", "deep learning", "reinforcement learning",
            "fine-tuning", "transfer learning", "rag",
            "retrieval augmented generation", "embedding", "vector database",
            "faiss", "pinecone", "chromadb"
        ],
        "Version Control & Tools": [
            "git", "github", "gitlab", "dvc", "weights & biases", "wandb"
        ],
        "Soft Skills": [
            "research", "problem solving", "documentation",
            "system design", "architecture"
        ],
    },

    # ── Full Stack Developer ─────────────────────────────────
    "Full Stack Developer": {
        "Frontend": [
            "html", "css", "javascript", "typescript", "react", "next.js",
            "vue", "angular", "tailwind", "bootstrap", "sass", "webpack",
            "responsive design", "ui/ux"
        ],
        "Backend": [
            "node.js", "express", "python", "django", "flask", "fastapi",
            "java", "spring boot", "ruby on rails", "php", "laravel",
            "rest api", "graphql", "microservices"
        ],
        "Databases": [
            "mysql", "postgresql", "mongodb", "redis", "firebase",
            "sqlite", "sql", "nosql", "orm", "prisma", "sequelize"
        ],
        "DevOps & Cloud": [
            "docker", "kubernetes", "aws", "azure", "gcp", "ci/cd",
            "nginx", "linux", "bash", "jenkins", "github actions"
        ],
        "Version Control": [
            "git", "github", "gitlab", "bitbucket"
        ],
        "Testing": [
            "jest", "pytest", "unit testing", "integration testing",
            "selenium", "cypress", "tdd"
        ],
        "Soft Skills": [
            "agile", "scrum", "communication", "teamwork",
            "problem solving", "system design"
        ],
    },

    # ── Python Developer ────────────────────────────────────
    "Python Developer": {
        "Core Python": [
            "python", "oop", "object oriented", "functional programming",
            "asyncio", "multithreading", "multiprocessing",
            "decorators", "generators", "comprehensions"
        ],
        "Web Frameworks": [
            "django", "flask", "fastapi", "tornado", "aiohttp",
            "rest api", "graphql", "websocket"
        ],
        "Data & Scripting": [
            "pandas", "numpy", "csv", "json", "xml",
            "web scraping", "beautifulsoup", "selenium", "scrapy",
            "automation", "scripting"
        ],
        "Databases": [
            "sql", "mysql", "postgresql", "mongodb", "redis",
            "sqlite", "sqlalchemy", "orm"
        ],
        "Testing & Quality": [
            "pytest", "unittest", "tdd", "bdd", "code review",
            "pep8", "linting", "type hints", "mypy"
        ],
        "DevOps": [
            "docker", "git", "linux", "bash", "ci/cd",
            "aws", "azure", "gcp", "virtualenv", "pip"
        ],
        "Soft Skills": [
            "problem solving", "debugging", "documentation",
            "agile", "communication"
        ],
    },

    # ── Frontend Developer ──────────────────────────────────
    "Frontend Developer": {
        "Core Web": [
            "html", "html5", "css", "css3", "javascript", "es6",
            "typescript", "dom", "browser api"
        ],
        "Frameworks & Libraries": [
            "react", "next.js", "vue", "nuxt", "angular",
            "svelte", "jquery", "redux", "zustand", "mobx"
        ],
        "Styling": [
            "tailwind", "bootstrap", "sass", "scss", "less",
            "styled components", "css modules", "material ui", "chakra ui"
        ],
        "Build Tools": [
            "webpack", "vite", "parcel", "babel", "npm", "yarn",
            "pnpm", "eslint", "prettier"
        ],
        "Testing": [
            "jest", "react testing library", "cypress", "playwright",
            "unit testing", "e2e testing"
        ],
        "Performance & SEO": [
            "seo", "web performance", "lighthouse", "core web vitals",
            "lazy loading", "code splitting", "pwa", "accessibility"
        ],
        "Version Control": [
            "git", "github", "gitlab", "agile", "scrum"
        ],
    },

    # ── DevOps Engineer ─────────────────────────────────────
    "DevOps Engineer": {
        "Containerization": [
            "docker", "kubernetes", "helm", "podman",
            "container", "microservices"
        ],
        "CI/CD": [
            "jenkins", "github actions", "gitlab ci", "circleci",
            "travis ci", "argocd", "ci/cd", "pipeline"
        ],
        "Cloud": [
            "aws", "azure", "gcp", "terraform", "cloudformation",
            "ansible", "puppet", "chef", "infrastructure as code", "iac"
        ],
        "Monitoring": [
            "prometheus", "grafana", "elk", "datadog", "splunk",
            "new relic", "monitoring", "alerting", "logging"
        ],
        "Networking & Security": [
            "linux", "bash", "networking", "tcp/ip", "dns",
            "ssl", "tls", "firewall", "vpn", "security"
        ],
        "Version Control": [
            "git", "github", "gitlab", "branching strategy"
        ],
        "Soft Skills": [
            "problem solving", "documentation", "collaboration",
            "on-call", "incident management"
        ],
    },
}

# ── Skill importance weights (used in ATS scoring) ──────────
# Higher weight = more critical for the role
SKILL_WEIGHTS = {
    "Data Scientist": {
        "Core Programming": 0.20,
        "Machine Learning": 0.25,
        "Deep Learning & AI": 0.15,
        "Data Manipulation": 0.15,
        "Visualization": 0.08,
        "Statistics": 0.07,
        "Big Data & Cloud": 0.05,
        "Databases": 0.03,
        "Soft Skills": 0.02,
    },
    "AI Engineer": {
        "Core Programming": 0.15,
        "AI Frameworks": 0.25,
        "MLOps & Deployment": 0.20,
        "Cloud Platforms": 0.12,
        "Data Engineering": 0.10,
        "Machine Learning": 0.10,
        "Version Control & Tools": 0.05,
        "Soft Skills": 0.03,
    },
    "Full Stack Developer": {
        "Frontend": 0.22,
        "Backend": 0.25,
        "Databases": 0.15,
        "DevOps & Cloud": 0.12,
        "Version Control": 0.08,
        "Testing": 0.10,
        "Soft Skills": 0.08,
    },
    "Python Developer": {
        "Core Python": 0.30,
        "Web Frameworks": 0.20,
        "Data & Scripting": 0.15,
        "Databases": 0.12,
        "Testing & Quality": 0.10,
        "DevOps": 0.08,
        "Soft Skills": 0.05,
    },
    "Frontend Developer": {
        "Core Web": 0.25,
        "Frameworks & Libraries": 0.25,
        "Styling": 0.15,
        "Build Tools": 0.10,
        "Testing": 0.10,
        "Performance & SEO": 0.10,
        "Version Control": 0.05,
    },
    "DevOps Engineer": {
        "Containerization": 0.20,
        "CI/CD": 0.20,
        "Cloud": 0.22,
        "Monitoring": 0.13,
        "Networking & Security": 0.12,
        "Version Control": 0.08,
        "Soft Skills": 0.05,
    },
}

# ── Resume section keywords (for structural checks) ─────────
RESUME_SECTIONS = [
    "education", "experience", "skills", "projects",
    "certifications", "achievements", "summary", "objective",
    "publications", "awards", "languages", "interests"
]

# ── Action verbs that boost resume quality score ────────────
ACTION_VERBS = [
    "achieved", "built", "created", "designed", "developed",
    "engineered", "implemented", "improved", "increased", "led",
    "managed", "optimized", "reduced", "resolved", "spearheaded",
    "trained", "deployed", "automated", "analyzed", "collaborated",
    "delivered", "established", "launched", "maintained", "mentored"
]
