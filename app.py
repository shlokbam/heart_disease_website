from flask import Flask, render_template, jsonify
import csv
import os

app = Flask(__name__)

def load_heart_data():
    data = []
    csv_path = os.path.join(os.path.dirname(__file__), 'Heart_new2.csv')
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/api/stats')
def stats():
    data = load_heart_data()
    total = len(data)
    heart_disease_yes = sum(1 for r in data if r['HeartDisease'] == 'Yes')
    smokers = sum(1 for r in data if r['Smoking'] == 'Yes')
    diabetic = sum(1 for r in data if r['Diabetic'] == 'Yes')
    stroke = sum(1 for r in data if r['Stroke'] == 'Yes')
    
    # Gender breakdown
    female_hd = sum(1 for r in data if r['Sex'] == 'Female' and r['HeartDisease'] == 'Yes')
    male_hd = sum(1 for r in data if r['Sex'] == 'Male' and r['HeartDisease'] == 'Yes')
    
    # Race breakdown
    races = {}
    for r in data:
        if r['HeartDisease'] == 'Yes':
            race = r['Race']
            races[race] = races.get(race, 0) + 1
    
    # GenHealth
    gen_health = {}
    for r in data:
        gh = r['GenHealth']
        gen_health[gh] = gen_health.get(gh, 0) + 1
    
    return jsonify({
        'total': total,
        'heart_disease_yes': heart_disease_yes,
        'heart_disease_rate': round(heart_disease_yes / total * 100, 1),
        'smokers': smokers,
        'diabetic': diabetic,
        'stroke': stroke,
        'female_hd': female_hd,
        'male_hd': male_hd,
        'races': races,
        'gen_health': gen_health
    })

@app.route('/api/sample')
def sample():
    data = load_heart_data()
    return jsonify(data[:20])

if __name__ == '__main__':
    app.run(debug=True)
