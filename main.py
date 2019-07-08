from flask import Flask, request, redirect, render_template
import cgi 
import os

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup():
  return render_template('signup.html')

# def is_email():
#   for char in email:
#     if "@" in email and if "." in email and if " " not in email:
#       pass
#     if email == "":
#       pass

@app.route("/", methods = ['POST'])
username_error = ''
password_error = ''
verify_password_error = ''

def get_user_info():
  username = request.form['username']
  username_error = "Please enter a username"
  return render_template('signup.html', username=username, username_error=username_error)

def get_password():  
  password = request.form['password']  
  password_error = "Please enter a password"
  password_error2 = "Please enter a password between 3 and 20 characters" 

  verify_password = request.form['verify-password']
  verify_password_error = "Passwords do not match, please try again"
  
  return render_template('signup.html', password=password, password_error=password_error, 
  password_error2=password_error2, verify_password=verify_password, verify_password_error=verify_password_error)


if not username_error and not password_error and not verify_password_error:
  return redirect('/welcome?username={0}'.format(username))
else:
  return render_template('signup.html', username=username, email=email)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")  
    print(username)
    return render_template('welcome.html', username=username)

app.run()