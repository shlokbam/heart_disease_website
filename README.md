## ❤️ HeartLens — Heart Disease Analysis Website

=======
[![Flask](https://img.shields.io/badge/Flask-3.0.0-black)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Tableau](https://img.shields.io/badge/Tableau-Public-orange)](https://public.tableau.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An interactive web platform for exploring heart disease risk factors through data visualization and analytics. Built as part of the SmartBridge Data Analytics with Tableau program, this project transforms raw health data into actionable insights using Tableau dashboards embedded in a modern Flask web application.

## 🎯 Project Overview

Heart disease remains one of the leading causes of mortality worldwide. This project analyzes a comprehensive dataset of 4,500+ patient records to uncover correlations between demographics, lifestyle habits, clinical indicators, and heart disease prevalence. The interactive Tableau dashboards enable healthcare professionals, researchers, and policymakers to make data-driven decisions for preventive care and public health initiatives.

### Key Features

- **📊 Interactive Tableau Dashboards**: 4 comprehensive dashboards exploring different aspects of heart disease data
- **📈 Real-time Statistics**: Live calculation of key metrics from the dataset
- **📋 Dataset Explorer**: Detailed column descriptions, data visualizations, and sample records
- **👥 Team Collaboration**: Multi-member development showcasing different skill sets
- **🎨 Modern UI**: Responsive design with dark theme optimized for data visualization
- **🔗 API Endpoints**: RESTful APIs for data access and statistics

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd heart_disease_website
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📊 Dataset Information

The project uses the **Heart Disease Dataset** containing **4,500+ patient records** with **18 health indicators**:

### Key Features
- **HeartDisease**: Target variable (Yes/No)
- **Demographics**: Age, Sex, Race
- **Lifestyle**: Smoking, Alcohol consumption, Physical activity
- **Clinical**: BMI, Diabetic status, Stroke history, General health
- **Comorbidities**: Asthma, Kidney disease, Skin cancer

### Data Insights
- **Heart Disease Prevalence**: ~9.3% across the dataset
- **Gender Distribution**: Higher prevalence in males
- **Age Correlation**: Strong positive correlation with age
- **Risk Factors**: Smoking, diabetes, and stroke show significant associations

## 🏗️ Project Structure

```
heart_disease_website/
├── app.py                    # Flask application backend
├── Heart_new2.csv           # Heart disease dataset (4,500+ records)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── templates/               # HTML templates
    ├── base.html           # Base layout with navigation
    ├── index.html          # Homepage with overview
    ├── dashboard.html      # Tableau dashboard embeds
    ├── dataset.html        # Dataset explorer
    └── team.html           # Team information
```

## 🖥️ Application Pages

### 🏠 Home (`/`)
- Project overview and key statistics
- Interactive stats bar with live data
- Feature highlights and use case scenarios
- Technology stack showcase

### 📊 Dashboard (`/dashboard`)
- **Dashboard 1**: Overview - Demographics and basic correlations
- **Dashboard 2**: Health & Activity - BMI, diabetes, physical activity
- **Dashboard 3**: BMI & Diabetes - Detailed analysis
- **Heart Disease Story**: Narrative-driven data storytelling

### 📋 Dataset (`/dataset`)
- Complete column descriptions and data types
- Interactive charts (gender distribution, health status, etc.)
- Sample data table (first 20 records)
- Data insights and visualizations

### 👥 Team (`/team`)
- Team member profiles and contributions
- Project progress tracking
- SmartBridge program information

## 🛠️ Technology Stack

### Backend
- **Flask 3.0.0**: Lightweight web framework
- **Python 3.8+**: Core programming language
- **CSV Module**: Data processing

### Frontend
- **HTML5/CSS3**: Modern responsive design
- **JavaScript**: Interactive features and API calls
- **Chart.js**: Data visualization library
- **Google Fonts**: Typography (Syne, DM Sans)

### Data Visualization
- **Tableau Public**: Interactive dashboards
- **Embedded API**: Seamless web integration

### Development Tools
- **Git**: Version control
- **VS Code**: Development environment
- **SmartBridge Program**: Project framework

## 📡 API Endpoints

The Flask backend provides RESTful APIs:

- `GET /api/stats` - Dataset statistics and aggregations
- `GET /api/sample` - Sample records (first 20 rows)

Example response from `/api/stats`:
```json
{
  "total": 4500,
  "heart_disease_yes": 418,
  "heart_disease_rate": 9.3,
  "smokers": 1410,
  "diabetic": 526,
  "stroke": 282,
  "female_hd": 144,
  "male_hd": 274,
  "races": {"White": 312, "Black": 67, "Hispanic": 25, ...},
  "gen_health": {"Excellent": 456, "Very Good": 987, ...}
}
```

## 👨‍💻 Team Members

### Anagh Navarkar (Team Lead)
Leading project coordination, Tableau dashboard development, and milestone management.

### Team Contributors
- **Prapti These**: Data preparation and visualization design
- **Rohit Patil**: Database operations and Tableau connectivity
- **Rutuj Bhandari**: Data analysis and performance optimization
- **Shlok Bam**: Flask web development and UI integration

## 🎓 SmartBridge Program

This project is developed as part of the **SmartBridge SkillWallet** program, focusing on:
- Data Analytics with Tableau
- Business Intelligence tools
- Web application development
- Team collaboration and project management

**Project Metrics:**
- 8 Epics completed
- 15 User stories implemented
- 5 team members
- 50% project completion

## 🤝 Contributing

This is a group project for the SmartBridge program. For contributions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **SmartBridge** for the Data Analytics with Tableau program
- **Tableau Public** for hosting our interactive dashboards
- **CDC** and health data contributors for the dataset
- **Flask** and **Chart.js** communities for excellent tools

---

**Built with ❤️ for better heart health through data-driven insights**

