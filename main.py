from flask import Flask, request, redirect, render_template
import cgi 
import os
# import jinja2

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), 
# autoescape= True)

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
  # template = jinja_env.get_template('signup.html')
  # return template.render() 
  return render_template('signup.html')

def is_email(email):
    if "@" and "." in email:
        if len(email) > 3 and len(email) < 20:
            return True
    if email == "":
        pass

@app.route("/", methods = ['POST'])
def get_user_info():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']
    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

    if username == "":
      username_error = "Please enter a username"
    if password == "":
      password_error = "Please enter a password"
    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a password between 3 and 20 characters" 
    if verify_password == "":
      verify_password_error = "Please verify your password"
    if verify_password != password:
        verify_password_error = "Passwords do not match"
    if not is_email(email):
        email_error = "Please enter a valid email"

    if not username_error and not password_error and not verify_password_error:
        # username = request.args.get("username")
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username=username, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")  
    print(username)
    return render_template('welcome.html', username=username)

app.run()