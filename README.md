Read Me

This Python script uses the Flask library to create a basic web application that serves different HTML pages and performs login, registration, and password reset functionalities.

The main script creates a Flask instance and defines different routes for handling requests:

    index(): This route handles the home page request and returns an HTML template rendered using the Jinja2 template engine.

    login(): This route handles the login page request and returns an HTML template rendered using the Jinja2 template engine.

    login_user(): This route handles the login form submission, retrieves the user's input, performs authentication and validation, and returns an HTML template rendered using the Jinja2 template engine.

    login_get_register(): This route handles the registration page request and returns an HTML template rendered using the Jinja2 template engine.

    login_register(): This route handles the registration form submission and returns an HTML template rendered using the Jinja2 template engine.

    forgot_GET(): This route handles the password reset page request and returns an HTML template rendered using the Jinja2 template engine.

    forgot_POST(): This route handles the password reset form submission.

    signup_GET(): This route handles the sign-up page request and returns an HTML template rendered using the Jinja2 template engine.

    profile(): This route handles the user profile page request and returns an HTML template rendered using the Jinja2 template engine.

The if __name__ == '__main__': block is executed when the script is run from the command line. It starts the Flask web application on a local server.
