#!/usr/bin/python3
import cgi, os

form = cgi.FieldStorage()
origin_title = form["origin_title"].value
title = form["title"].value
description = form["description"].value

#파일 생성
opened_file = open('data/'+origin_title, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+origin_title, 'data/'+title)

print("Location: index.py?id="+title)
print()