❤️ HeartLens — Heart Disease Analysis Website

A full-stack data analytics web application that visualizes and analyzes heart disease data using interactive dashboards and real-time statistics.

Built as part of the SmartBridge Data Analytics project, this platform transforms raw healthcare data into meaningful insights for better understanding of heart disease risk factors.

🌐 Live Overview

HeartLens provides:

📊 Interactive dashboards (Tableau embedded)

📁 Dataset exploration with structured insights

📈 Real-time statistical analysis via API

👥 Project and team showcase

🎯 Project Objective

Heart disease is one of the leading causes of death globally. This project aims to:

Analyze healthcare data with multiple risk factors

Identify patterns in demographics and lifestyle

Provide interactive and visual insights

Enable data-driven understanding for healthcare awareness

As described in the project documentation, the system integrates demographics, lifestyle, and clinical indicators to generate meaningful insights for decision-making .

⚙️ Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS (Custom UI)

Data Handling: CSV + Python

Visualization: Tableau Public (Embedded Dashboards)

API: REST endpoints for analytics

🧠 Core Features
📊 1. Interactive Dashboard

Embedded Tableau dashboards

Multi-level analysis:

Demographics (Age, Gender, Race)

Lifestyle (Smoking, Alcohol, Activity)

Clinical factors (Diabetes, Stroke, BMI)

👉 Implemented in: dashboard.html

📁 2. Dataset Explorer

Detailed feature descriptions

Visual charts and structured data display

Sample dataset preview

👉 Dataset contains 4500+ records with 18 features

📈 3. Real-Time Statistics API

Flask backend computes:

Total patients

Heart disease rate

Smokers, diabetic, stroke cases

Gender-based analysis

Race distribution

General health insights

👉 API endpoint:

/api/stats

👉 Implemented in backend: app.py

🧾 4. Clean UI & UX

Modern dark-themed design

Responsive layout

Smooth navigation across pages

👉 Base layout: base.html

👥 5. Team & Project Info

Displays contributors and roles

Academic project details

👉 Page: team.html

📂 Project Structure
HeartLens/
│
├── app.py                # Flask backend
├── Heart_new2.csv       # Dataset
├── requirements.txt     # Dependencies
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── dataset.html
│   └── team.html
│
└── README.md
▶️ How to Run Locally
# Clone the repo
git clone https://github.com/shlokbam/heart_disease_website.git

# Go to project folder
cd heart_disease_website

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py

Now open:

👉 http://localhost:5000

🔌 API Endpoints
Endpoint	Description
/	Homepage
/dashboard	Tableau dashboards
/dataset	Dataset exploration
/team	Team information
/api/stats	Analytics summary (JSON)
/api/sample	Sample dataset records
📊 Key Insights from Analysis

Based on your project documentation:

Age is the strongest risk factor

Diabetes significantly increases risk

Physical inactivity is a major contributor

Smoking compounds risk but is not dominant alone

Self-reported health strongly correlates with diagnosis

🚧 Future Improvements

Add machine learning prediction model

User input-based risk prediction

Authentication system

Deploy on cloud (AWS / Render / Vercel)

Convert to full React + FastAPI architecture

⚠️ Disclaimer

This project is for educational and analytical purposes only and should not be used for medical diagnosis.

👨‍💻 Contributors

Shlok Bam

Anagh Navarkar

Prapti These

Rohit Patil

Rutuj Bhandari

⭐ If you like this project

Give it a ⭐ on GitHub — it helps!
