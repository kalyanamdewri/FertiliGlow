from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class User:
    def __init__(self, name, cycle_length, last_period):
        self.name = name
        self.cycle_length = cycle_length
        self.last_period = last_period
        self.progress = {}

    def log_daily_data(self, mood, temperature, notes=""):
        day = (datetime.datetime.now() - datetime.datetime.strptime(self.last_period, "%Y-%m-%d")).days
        self.progress[day] = {
            "mood": mood,
            "temperature": temperature,
            "notes": notes
        }

# Initialize a dummy user for demonstration purposes
user = User("Jane Doe", 28, "2024-08-01")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    fertility_window = calculate_fertility_window(user.cycle_length)
    today = (datetime.datetime.now() - datetime.datetime.strptime(user.last_period, "%Y-%m-%d")).days
    in_fertility_window = today in fertility_window
    return render_template('dashboard.html', user=user, in_fertility_window=in_fertility_window)

@app.route('/log_data', methods=['GET', 'POST'])
def log_data():
    if request.method == 'POST':
        mood = request.form['mood']
        temperature = float(request.form['temperature'])
        notes = request.form.get('notes', '')
        user.log_daily_data(mood, temperature, notes)
        return redirect(url_for('dashboard'))
    return render_template('log_data.html')

def calculate_fertility_window(cycle_length):
    ovulation_day = cycle_length // 2
    return range(ovulation_day - 3, ovulation_day + 2)

if __name__ == '__main__':
    app.run(debug=True)
