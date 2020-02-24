from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def hello():
    if request.method == 'GET':
        return render_template('page1.html')
    else:
        return data

@app.route('/blog')
def blog():
    books = ['asdad','hi','by']
    return jsonify(books)

@app.route('/<user>')
def hello_user(user):
    return render_template('user.html', user = user)

@app.route('/admin/<user>/<int:id>')
def hello_admin(user,id):
    return render_template('admin.html', user = user, id = id)
