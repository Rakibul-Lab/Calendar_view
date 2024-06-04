from flask import Flask, render_template, request
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar', methods=['POST'])
def show_calendar():
    year = int(request.form['year'])
    month = int(request.form['month'])
    cal = calendar.month(year, month)
    return render_template('calendar.html', cal=cal)

if __name__ == '__main__':
    app.run(debug=True)
