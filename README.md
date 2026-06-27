# 🩺 Medical Disease Prediction System

A Machine Learning based web application that predicts the possible disease of a patient using health-related information such as Age, BMI, Blood Pressure, Glucose Level, Cholesterol, Heart Rate, Smoking habits, Alcohol consumption, Physical Activity, and Family History.

The project is developed using **Python**, **Flask**, **HTML**, **CSS**, **Pandas**, and **Scikit-learn**.

---

## 📌 Features

- Predicts disease using Machine Learning
- Simple and user-friendly interface
- Responsive web design
- Fast prediction results
- Flask backend
- Trained Random Forest Classifier model
- Input validation using HTML forms

---

## 📷 Project Preview

### Home Page
- Modern landing page
- Disease prediction overview
- Navigation bar
- Responsive design

### Prediction Page
- Patient Details Form
- Disease Prediction
- Easy-to-use dropdown menus
- Responsive layout

---

## 🧠 Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

The model predicts diseases based on multiple health parameters.

---

## 📊 Input Features

| Feature | Description |
|----------|-------------|
| Age | Patient Age |
| Gender | Male / Female |
| BMI | Body Mass Index |
| Blood Pressure | Blood Pressure Value |
| Glucose Level | Blood Sugar Level |
| Cholesterol | Cholesterol Level |
| Heart Rate | Heart Beats Per Minute |
| Smoking | Yes / No |
| Alcohol | Yes / No |
| Physical Activity | Low / Medium / High |
| Family History | Yes / No |

---

## 🎯 Output

The application predicts one of the following diseases:

- Healthy
- Diabetes
- Pre-Diabetes
- Hypertension
- Heart Disease

---

## 🛠 Technologies Used

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📂 Project Structure

```
Medical-Disease-Prediction/
│
├── Data/
│   └── medical_disease.csv
│
├── Model/
│   └── RandomForestClassifier.lb
│
├── Static/
│   ├── css/
│   │    └── style.css
│   │
│   └── images/
│
├── Templates/
│   ├── index.html
│   ├── project.html
│   ├── about.html
│   ├── contact.html
│   └── history.html
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## ⚙ Installation

### 1 Clone Repository

```bash
git clone https://github.com/yourusername/Medical-Disease-Prediction.git
```

### 2 Move to Project Folder

```bash
cd Medical-Disease-Prediction
```

### 3 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

### 4 Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5 Run Application

```bash
python app.py
```

---

### 6 Open Browser

```
http://127.0.0.1:5000
```

---

## 📦 Required Libraries

```
Flask
pandas
numpy
scikit-learn
joblib
```

Install all at once:

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## 📈 Future Improvements

- More diseases
- Better prediction accuracy
- Doctor recommendation
- Medicine suggestions
- PDF report generation
- User login system
- Prediction history
- Database integration

---

## 👨‍💻 Author

**Krishan Kumar Saini**

Computer Science Engineering Student

Interested in:

- Machine Learning
- Data Science
- Artificial Intelligence

GitHub:
https://github.com/KrishanSaini01

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.

---

## 📄 License

This project is developed for educational and learning purposes.
