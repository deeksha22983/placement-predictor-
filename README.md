# 🎓 Student Placement Prediction System (Dockerized)

An end-to-end Machine Learning web application that predicts a student's campus placement outcome based on academic features. The entire system architecture—including automated data pipeline fetching, classification logic, and the web microkernel—is encapsulated natively within an isolated Docker container for robust deployment.

---

## 👤 Developer Profile
* **Name:** Akshat Garg
* **Registration Number:** 23BCE10641
* **Course:** B.Tech Computer Science and Engineering
* **Institution:** VIT Bhopal University

---

## 🔗 Project Links
* **Live Dockerized Web Application:** [Insert Your New Render Live URL Here]
* **GitHub Repository:** [Insert Your New GitHub Repository URL Here]

---

## 🛠️ Tech Stack & Container Ecosystem
* **Core Language:** Python 3.10
* **Containerization Engine:** Docker
* **Machine Learning & Data Processing:** Scikit-learn, Pandas, NumPy
* **Backend Web Framework:** Flask
* **Production Web Server:** Gunicorn (WSGI)
* **Model Serialization:** Pickle
* **Cloud Infrastructure Gateway:** Render (Docker Runtime Container Service)

---

## 📂 Production Directory Architecture
This project completely replaces platform-specific web infrastructure dependencies (such as `Procfile` or `runtime.txt`) by defining immutable compilation rules inside a single `Dockerfile`:

```text
📁 Student-Placement-Docker/
│
├── 📁 static/
│   └── 📄 style.css            # Custom corporate blue user interface theme
│
├── 📁 templates/
│   └── 📄 index.html           # Core frontend interactive web form
│
├── 📄 app.py                   # Production Flask application backend logic
├── 📄 train.py                 # Automated pipeline dataset download & ML trainer
├── 📄 placement_model.pkl      # Serialized Random Forest Classifier binary
├── 📄 requirements.txt         # Plaintext manifest mapping third-party libraries
├── 📄 Dockerfile               # Core Docker container environment configuration
└── 📄 .gitignore               # Excludes runtime caches and raw dataset packages

```

---

## 📊 Dataset & Feature Alignment

The machine learning classifier parses a structured student placement dataset sourced dynamically from Kaggle. Predictions are computed mathematically through a trained `RandomForestClassifier` with zero hardcoded fallback conditions. The inputs consist entirely of numeric vectors:

| Feature Name | Type | Description / Value Space |
| --- | --- | --- |
| **CGPA** | Continuous | Cumulative Grade Point Average |
| **Placement Exam Marks** | Continuous | Total score earned on the mock placement qualification exam |

### Target Variable (Output)

* **`0`**: Not Placed 😔
* **`1`**: Placed 🎉

---

## ⚙️ How to Setup and Run Locally

### Option A: Standard Local Execution

1. **Initialize Your Workspace Environment:**
```bash
conda activate placement
pip install -r requirements.txt

```


2. **Train and Serialize the Model:**
```bash
python train.py

```


3. **Launch the Flask Development Server:**
```bash
python app.py

```


Navigate to `http://127.0.0.1:5000` inside your web browser.

### Option B: Local Container Testing (Requires Docker Desktop)

To evaluate the absolute container runtime state before deploying it to production, build and run the image sandbox:

```bash
# 1. Compile the Docker image from your blueprint configuration
docker build -t student-placement-app .

# 2. Spin up the container sandbox and expose the target gateway port
docker run -p 10000:10000 student-placement-app

```

Navigate to `http://localhost:10000` inside your browser.

---

## 🚀 Live Cloud Deployment via Docker

The system relies on continuous delivery directly connected to **Render**:

* Render evaluates the root `Dockerfile` to pull a minimal, secure `python:3.10-slim` runtime base image.
* Dependencies are safely cached and deployed in structural abstraction layers.
* Gunicorn web processes are bound straight to port `10000`, bypassing standard server stack setup configurations completely.
