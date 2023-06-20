#!/usr/bin/python3
import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

#파일 생성
opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

print("Location: index.py?id="+title)
print()