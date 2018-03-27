from flask import Flask, request, render_template, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return 'Method used %s' % request.method


@app.route('/about')
def about():
    return '<h2> Tuna is awesome as balls </h2>'


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)


@app.route('/user/<username>')
def user(username):
    return 'hey %s ' % username


@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
    return 'hey %s ' % request.method


if __name__ == '__main__':
    app.run(debug=True)
