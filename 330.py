from flask import Flask

app = Flask(__name__)

topics = [
  {"id":1, "title":"html", "body":"html is ...."},
  {"id":2, "title":"css", "body":"css is ...."}
]

@app.route("/")
def index():
  liTags =''
  for topic in topics:
     liTags = liTags + f'<li>{topic["title"]}</li>'
  return f'''
  <html>
   <body>
    <h1><a href="/">WEB<a></h1>
    <ol>
     {liTags}
    </ol>
    <h2>Welcome</h2>
    Hello,WEB!
   </body>
  </html>
  '''

@app.route('/create/')
def creat():
  return 'Create'

app.run()