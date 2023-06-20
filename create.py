#!/usr/bin/python3
print("Content-Type: text/html\n")
import cgi, os

def getList():
  files = os.listdir('data')
  listStr = ''
  for item in files:
      listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
  return listStr

form = cgi.FieldStorage()
pageId = "Welcome"
description = 'Hello world!'
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()

print('''
<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
  {listStr}
  </ol>
  <a href="create.py">create</a>
  <form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId, description=description, listStr=getList()))