from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'Nathaniel Senje'
    skills = ['Web Development', 'Programming', 'Machine Learning', 'AI']

    return render_template('index.html', title=name, skills=skills, name=name)


if __name__ == '__main__':
    app.run(debug=True)
