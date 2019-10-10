from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True     

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/", methods=['POST'])
def validate():    
    username = request.form["username"]
    password = request.form["password"]
    verify_password = request.form["verify_password"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username = ''
        username_error = 'Username invalid'
    else:
        username = username

    #password cannot be blank and has to be between 3 and 20 characters
    if len(password) < 3 or len(password) > 20:
        password = ''
        password_error = 'Password invalid'
    else:
        password = password
    
    #verify password cannot be blank and has to match password
    if password != verify_password:
        password = password
        verify_password = verify_password
        password_verify = ''
        password_error = 'Passwords do not match'
    
    #email parameters
    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email=email
        else:
            email = ''
            email_error = 'Email Error'
    else:
        email = ''

    #if username == "":
        #username_error = 'Username Error'
    #if password == "":
        #password_error = 'Password Error'
    #if verify_password == "":
        #verify_password_error = 'Enter a password to match the one above'

    
    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template('/welcomepage.html', username = username)
    else:
        return render_template('/form.html', username = username, username_error = username_error, password_error = password_error, verify_password_error = verify_password_error, email = email, email_error = email_error) 

@app.route("/welcomepage")
def welcome():
    username = request.args.get("username")
    return render_template("welcomepage.html", username = username)





app.run()
