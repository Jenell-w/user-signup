from flask import Flask, request, redirect, render_template
import cgi 
import os

app= Flask(__name__)
app.config['DEBUG'] = True

username_error = ''
password_error = ''
verify_password_error = ''
username = ''
password = ''
verify_password = ''
email = ''
email_error = ''

def validate_password_length(password):
  if password == '' or len(password) < 3 or len(password) > 20:
      return False
  return True

@app.route('/')
def display():
  return render_template('signup-no-errors.html', username=username, password=password, 
  verify_password=verify_password, email=email)

@app.route("/", methods = ['POST'])
def get_user_info():

  username = request.form['username']
  password = request.form['password']
  verify_password = request.form['verify_password']
  email = request.form['email']

  if username == '':
    username_error = "Please enter a username"
    username = ''
    return render_template('signup.html', username_error=username_error)
 
  if not validate_password_length(password):
      return render_template('signup.html', verify_password_error="Please enter a password between 3 and 20 characters.")
  
  if (password != verify_password):
    verify_password_error = "Passwords do not match, please try again"
    verify_password = ''
    return render_template('signup.html', verify_password_error=verify_password_error)
  
  if email == '':
    if not username_error and not password_error and not verify_password_error:
      return redirect('/welcome?username={0}'.format(username))
  else:
    return render_template('signup.html', username=username, email=email) 
  
  if "@" not in email or "." not in email:
    email_error = "Please enter a valid email address"
    if " " in email:
      email_error = "Please enter a valid email address"
      if len(email) < 3 or len(email) > 20:
        email_error = "Please enter a valid email address"
        email = ''
    return render_template('signup.html', email_error=email_error)

 

@app.route("/welcome")
def welcome():
    username = request.args.get("username")  
    print(username)
    return render_template('welcome.html', username=username)

app.run()
