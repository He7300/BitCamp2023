from flask import Flask, render_template, request, send_file

api = 'http://127.0.0.1:8000'

app = Flask(__name__)

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

@app.route('/signup/')
def signup_GET():
    return render_template('signup.html')

@app.route('/myprofile/')
def profile():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
