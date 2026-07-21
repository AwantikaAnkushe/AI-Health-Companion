# AI Health Companion

# 🩺 MediMate AI – Intelligent Personal Health Companion

## 📖 About the Project

Hi! 👋

I built **MediMate AI** as a full-stack health companion application to help users manage their day-to-day health in one place. The idea behind this project came from a simple problem: people often forget to take medicines, lose their medical reports, or ignore symptoms until they become serious.

My goal was to create an application where users can securely store their health information, track symptoms, manage medications, upload medical reports, and receive AI-powered health insights—all from a single app.

> **Note:** MediMate AI does **not** diagnose diseases or prescribe medicines. It only provides educational insights based on the symptoms entered by the user and always recommends consulting a qualified healthcare professional.

---

# 🎯 Project Objective

The objective of this project is to build a modern health management application using a microservices architecture while integrating multiple technologies such as Flutter, Node.js, MySQL, and Python.

Through this project, I wanted to demonstrate my skills in:

* Flutter Mobile Development
* REST API Development
* Database Design
* Authentication & Security
* AI Integration
* File Upload Handling
* Data Visualization
* Full-Stack Development

---

# 🚀 Features

### 🔐 Authentication

* User Registration
* Secure Login
* JWT Authentication
* Password Encryption

### 👤 User Profile

After logging in, users can create their health profile by entering:

* Age
* Gender
* Height
* Weight
* Blood Group
* Existing Medical Conditions
* Allergies

---

### 🏠 Dashboard

The dashboard gives users a quick overview of their health information, including:

* Health Score
* Today's Medicines
* Recent Symptoms
* Uploaded Reports
* Upcoming Medication Reminders

---

### 🤒 Symptom Tracker

Users can record symptoms such as:

* Fever
* Headache
* Cough
* Fatigue

They can also add:

* Severity Level
* Duration
* Personal Notes

This information is stored in the database and later analyzed by the AI service.

---

### 🤖 AI Health Analysis

When a user submits their symptoms, the application sends the data to a Python-based AI service.

The AI analyzes the symptoms and returns:

* Possible Health Conditions
* Confidence Score
* General Health Recommendations

The AI is designed only for educational purposes and never replaces professional medical advice.

---

### 💊 Medicine Tracker

Users can add medicines prescribed by their doctor and schedule reminder notifications.

Each medicine stores:

* Medicine Name
* Dosage
* Time
* Reminder Status

---

### 📄 Medical Report Upload

Users can upload:

* Blood Reports
* MRI Reports
* X-Rays
* Prescriptions

The reports are securely stored, allowing users to access them anytime.

---

### 📊 Health Analytics

The application also provides graphical visualizations such as:

* Symptom Frequency
* Weight Progress
* Blood Pressure Trends
* Medication Adherence

These charts help users better understand their overall health.

---

# 🛠️ Tech Stack

### Frontend

* Flutter
* Dart

### Backend

* Node.js
* Express.js

### Database

* MySQL

### AI Service

* Python
* FastAPI
* Pandas
* NumPy
* Scikit-learn

### Authentication

* JWT
* bcrypt

### Other Tools

* Multer
* Flutter Local Notifications
* fl_chart

---

# 🏗️ Project Architecture

```text
Flutter Application
        │
REST API Requests
        │
Node.js Backend
   │            │
MySQL      Python FastAPI
   │            │
Health Data   AI Analysis
        │
   Response to Flutter
```

---

# 📂 Project Structure

```text
MediMate-AI/

flutter_app/
node_backend/
python_ai/
database/
README.md
```

---

# 💡 What I Learned

While building this project, I learned how to:

* Design a full-stack application from scratch
* Build REST APIs using Node.js
* Connect Flutter with backend services
* Design and manage relational databases using MySQL
* Integrate Python AI services with a Node.js backend
* Implement secure authentication using JWT
* Handle file uploads and data visualization
* Build scalable application architecture

---

# 🔮 Future Improvements

In the future, I plan to add:

* OCR for Blood Reports
* AI Health Chatbot
* Google Fit Integration
* Smartwatch Support
* Appointment Scheduling
* Cloud Storage
* Multi-language Support

---

# ⚠️ Disclaimer

This project is developed for educational and learning purposes.

The AI-generated suggestions are not medical diagnoses and should not be considered professional healthcare advice. Users are always encouraged to consult a qualified healthcare professional regarding any medical concerns.

---



---

This style reads naturally, as if you're personally introducing your project to recruiters or anyone visiting your GitHub repository. It's professional, easy to read, and explains **why** you built the project—not just what technologies you used.
