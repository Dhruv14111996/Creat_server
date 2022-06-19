from flask import Flask, render_template
app = Flask(__name__)

# If i need to run html file then i can run using this same method but for that we need to call render_templetes


@app.route('/index/<username>/<float:post_id>')
def index(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/index/about')
def about():
    return render_template('about.html')


@app.route('/index/about/blog')
def blog():
    return 'Hello, These are my blogs thoughts.!'


@app.route('/index/about/blog/2022/dogs')
def blog2():
    return 'Hello, These are my Dogs.!'
