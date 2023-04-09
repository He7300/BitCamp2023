from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/download/style.css')
def download_style():
    return send_file('static/css/style.css', as_attachment=True)

@app.route('/download/js.js')
def download_javascript():
    return send_file('static/js/script.js', as_attachment=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    # Perform login validation and authentication here
    return render_template('loginsf.html', username=username, password=password)

@app.route('/register/')
def login_get_register():
    return render_template('register.html')

@app.route('/register/', methods=['POST'])
def login_register():
    return render_template('register.html')

@app.route('/forgotpass/')
def forgot_GET():
    return render_template('forgot.html')

@app.route('/forgotpass/')
def forgot_POST():
    pass

@app.route('/myprofile/')
def profile():
    return render_template('register.html')

@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    number = request.form['number']
    purpose = request.form['purpose']
    appointment_type = request.form['appointment-type']
    name = request.form['name']
    date = request.form['date']
    convenience = request.form['convenience']
    return f"Appointment submitted for {name} on {date} at {convenience} convenience. We will contact you at {number} regarding your {appointment_type} appointment to schedule a {purpose}."

if __name__ == '__main__':
    app.run(debug=True)
