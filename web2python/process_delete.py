#!/usr/bin/python3
import cgi, os

form = cgi.FieldStorage()
title = form["pageId"].value

os.remove("data/"+title)

print("Location: index.py")
print()