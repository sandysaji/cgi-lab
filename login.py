#!/usr/bin/env python3
import cgi
import os
import secret
from templates import login_page, secret_page, after_login_incorrect
import cgitb
from http.cookies import SimpleCookie

cgitb.enable()

print("Content-Type: text/html")


# q4
# print(cgi.FieldStorage())
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_ok = username==secret.username and password==secret.password

c = SimpleCookie(os.environ["HTTP_COOKIE"])
c_username = None
c_password = None
if c.get("username"):
    c_username = c.get("username").value 
if c.get("password"):
    c_username = c.get("password").value 

cookie_ok = c_username == secret.password and c_password ==secret.password
if cookie_ok:
    username=c_username
    password=c_password



if form_ok: 
    print("Set-Cookie: username=", secret.username)
    print("Set-Cookie: password=", secret.password)
print()

if not username and not password: 
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())