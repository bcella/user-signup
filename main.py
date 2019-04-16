from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config[ 'DEBUG' ] = True

@app.route("/validation", methods=['GET','POST'])
def validation():
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    username = request.form['username']
    password = request.form['password']
    verifypassword = request.form['verifypassword']
    email = request.form['email']

    if username == "":
        username_error = "Please submit a valid username."
    elif len(username) < 3 or len(username) > 20:
        username_error = "Please submit a username between 3 - 20 characters."
    elif username.count(' ') >0:
        username_error = "Invalid username. Cannot contain spaces."

    if password == "":
        password_error = "Please submit a valid password."
    elif len(password) < 3 or len(username) > 20:
        password_error = "Please submit a password between 3 - 20 characters."
    elif password.count(' ') > 0:
        password_error = "Passwords cannot contain spaces."

    if verifypassword == "":
        verify_error = "Please verify your password."
    
    if password != verifypassword:
        password_error = "Your passwords do not match."
        verify_error = "Your passwords do not match"
        username = request.form['username']
        password = ""
        verifypassword = ""
        

    if not email=="":
        if len(email) < 3 or len(email) > 20:
            email_error = "Please submit an email address that is between 3 - 20 characters"
        elif email.count('@') > 1:
            email_error = "Not a valid email."
        elif email.count(' ') > 0:
            email_error = "Email address cannot contain spaces."
        elif not email.count('.') == 1:
            email_error = "Not a valid email."
        
        


    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('index.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)


@app.route("/")
def index():
    return render_template('index.html')


app.run()