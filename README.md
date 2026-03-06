# HeartLens — Heart Disease Analysis Website

A Flask-powered website for the SmartBridge Heart Disease Analysis project.

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open: http://localhost:5000

## Pages
- `/` — Home page with stats and project overview
- `/dashboard` — Embedded Tableau dashboards (all 3 dashboards + story)
- `/dataset` — Dataset info, column descriptions, charts, sample data
- `/team` — Team members and project info

## Files
- `app.py` — Flask backend
- `Heart_new2.csv` — Heart disease dataset
- `templates/` — HTML templates
  - `base.html` — Shared layout, nav, footer
  - `index.html` — Homepage
  - `dashboard.html` — Tableau embed page
  - `dataset.html` — Dataset explorer
  - `team.html` — Team members
