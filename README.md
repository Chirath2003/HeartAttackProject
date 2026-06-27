# ❤️ Heart Attack Prediction System

A Machine Learning-powered healthcare web application that predicts the risk of heart attacks using patient health and lifestyle data. The system combines predictive analytics, patient management, secure authentication, and a web-based dashboard to assist healthcare professionals in identifying potential heart attack risks.

---

## 📌 Project Overview

The Heart Attack Prediction System uses Machine Learning algorithms to analyse patient health records and predict the likelihood of a heart attack.

The application provides:

* Patient registration and management
* Secure user authentication
* Password hashing for enhanced security
* Heart attack risk prediction
* Prediction history tracking
* Healthcare dashboard for monitoring records
* Machine Learning model integration

---

## ✨ Features

### 🔐 Authentication & Security

* Secure login system
* Password hashing using bcrypt
* Protected access to patient data
* Session-based authentication

### 👨‍⚕️ Patient Management

* Add new patients
* View patient records
* Manage patient information
* Store healthcare data securely

### 🤖 Machine Learning Prediction

* Predict heart attack risk using trained models
* Generate prediction results instantly
* Display risk classifications
* Model retraining support

### 📊 Monitoring & Reporting

* Prediction history logs
* Dashboard overview
* Patient statistics
* Data analysis and visualisation

---

## 📂 Dataset

Dataset used:

**heart_attack_prediction_indonesia.csv**

The dataset contains medical and lifestyle-related information including:

* Age
* Gender
* Blood Pressure
* Cholesterol Level
* BMI
* Heart Rate
* Smoking Status
* Diabetes Status
* Physical Activity
* Medical History
* Other clinical indicators

### Target Variable

| Value | Meaning              |
| ----- | -------------------- |
| 0     | No Heart Attack Risk |
| 1     | Heart Attack Risk    |

---

## 🛠 Technologies Used

### Programming Language

* Python 3.12

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Visualisation

* Matplotlib
* Seaborn

### Web Application

* Flask
* HTML5
* Jinja2 Templates

### Database

* SQLite

### Development Tools

* VS Code
* Git
* GitHub
* Jupyter Notebook

---

## 📁 Project Structure

```text
HeartAttackProject/
│
├── .gitignore
├── dataset_analysis.py
├── hash_passwords.py
├── model_training.py
├── random_forest_model.py
├── retrain_model.py
├── save_model.py
├── README.md
│
├── App/
│   │
│   ├── app.py
│   │
│   ├── database/
│   │   ├── database_setup.py
│   │   └── ehr.db
│   │
|   ├── static/
|   |   ├── style.css
|   |
│   └── templates/
│       ├── add_patient.html
│       ├── dashboard.html
│       ├── login.html
│       ├── logs.html
│       ├── patients.html
│       ├── prediction.html
│       └── prediction_result.html
│
├── Dataset/
│   └── heart_attack_prediction_indonesia.csv
│
├── Models/
│   └── heart_attack_model.pkl
│
└── Notebooks/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Chirath2003/HeartAttackProject.git
```

### 2. Navigate to the Project Folder

```bash
cd HeartAttackProject
```

### 3. Install Required Packages

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask bcrypt
```

---

## 🚀 Running the Application

### Start the Flask Application

```bash
cd App
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the URL in your web browser to access the system.

---

## 🔐 Authentication

The system implements secure authentication using password hashing.

### Login Features

* User authentication
* Secure password storage
* Session management
* Protected routes

Passwords are hashed before being stored in the database to improve security.

---

## 🤖 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Data Preprocessing
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Model Saving
11. Prediction Generation

---

## 📊 Exploratory Data Analysis

The project includes:

* Dataset shape analysis
* Missing value analysis
* Statistical summaries
* Class distribution analysis
* Correlation analysis
* Data visualisation
* Feature relationship analysis

Run:

```bash
python dataset_analysis.py
```

---

## 🧠 Model Training

Train the Machine Learning model:

```bash
python model_training.py
```

Alternative Random Forest training:

```bash
python random_forest_model.py
```

Save the trained model:

```bash
python save_model.py
```

Retrain the model:

```bash
python retrain_model.py
```

---

## 🗄 Database

The system uses SQLite for storing:

* User accounts
* Hashed passwords
* Patient records
* Prediction history
* System logs

Database file:

```text
App/database/ehr.db
```

---

## 📋 Application Pages

### Login Page

Allows authorised users to access the system securely.

### Dashboard

Displays patient and prediction summaries.

### Add Patient

Create new patient records.

### Patients

View and manage patient information.

### Prediction

Generate heart attack risk predictions.

### Prediction Results

Displays model prediction outcomes.

### Logs

View system activity and prediction history.

---

## 🔒 Security Features

* Password hashing
* Session-based authentication
* Secure database storage
* Protected healthcare records

---

## 📈 Future Improvements

* Deep Learning models
* Multiple model comparison
* Prediction confidence scores
* REST API integration
* React frontend
* Cloud deployment
* Docker support
* Role-based access control
* Email notifications
* Real-time patient monitoring

---

## 🎯 Learning Outcomes

This project demonstrates:

* Machine Learning model development
* Data preprocessing techniques
* Healthcare data analysis
* Flask web application development
* SQLite database integration
* Authentication and security practices
* Full-stack project implementation
* Software engineering best practices

---

## 🔒 Note

Large Machine Learning model files are excluded from GitHub using `.gitignore` because GitHub limits individual file uploads to 100 MB.

---

## 👨‍💻 Author

**Chirath**

Software Development Student | Machine Learning Enthusiast

GitHub: https://github.com/Chirath2003

---

⭐ If you found this project useful, consider giving the repository a star.
