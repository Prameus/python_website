
from flask import Flask, abort, render_template

app = Flask(__name__, template_folder='.')

# days = ["monday", 'tuesday', 'thursday', 'wednesday', 'friday']
# @app.route('/home')

#? niye sitede fotograflar gozukmuyor?

@app.route("/")
def home():
    return render_template("home.html")


userss = ['leluch', 'trevize', 'hannibal', 'guard']

# @app.route('/user/<series>')
# def user(series):
#     return render_template("series.html", series=series, days=days)


@app.route('/series')
def user():
    return render_template("series.html",)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/users/<name>')
def users(name):
    for i in userss:
        if i == name:
            return render_template("users.html", name=name)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
