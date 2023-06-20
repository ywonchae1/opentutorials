#!/usr/bin/python3
print("Content-Type: text/html\n")
import cgi, os, view

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
  <form action="process_update.py" method="post">
    <p><input type="hidden" name="origin_title" placeholder="title" value={title}></p>
    <p><input type="text" name="title" placeholder="title" value={form_default_title}></p>
    <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></p>
    <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(title=pageId,
description=description,
listStr=view.getList(),
form_default_title=pageId,
form_default_description=description))