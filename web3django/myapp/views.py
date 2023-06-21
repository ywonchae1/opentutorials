from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
'''
def index(request):
    return HttpResponse('<h1>Random</h1>'+str(random.random()))
'''

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is...'},
    {'id':2, 'title':'view', 'body':'View is...'},
    {'id':3, 'title':'model', 'body':'Model is...'}
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
        <li>
            <form action="/delete/" method="post">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
        </li>
        <li><a href="/update/{id}">update</a></li>
        '''
    
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
        <html>
        <body>
            <h1><a href="/">Django</a></h1>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
        </body>
        </html>
        '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'''
            <h2>{topic["title"]}</h2>
            {topic["body"]}
            '''
    
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    if request.method == "GET":
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        newTopic = {'id':len(topics)+1, 'title':title, 'body':description}
        topics.append(newTopic)
        url = '/read/'+str(len(topics))
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopic = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopic.append(topic)
        topics = newTopic
        return redirect('/')

@csrf_exempt
def update(request, id):
    global topics
    topic = ''
    title = ''
    description = ''

    topic = topics[int(id)-1]
    title = topic['title']
    description = topic['body']
    if request.method == 'GET':
        article = f'''
        <form action="/update/{id}/" method="post">
            <p><input type="text" name="title" value={title}></p>
            <p><textarea rows="4" name="description">{description}</textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        if topic != '':
            topic['title'] = request.POST['title']
            topic['body'] = request.POST['description']
        url = f'/read/{id}'
        return redirect(url)