#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()

print("Content-Type: text/html\n")
# print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
print(os.environ)
