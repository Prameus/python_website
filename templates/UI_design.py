
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

# days = ["monday", 'tuesday', 'thursday', 'wednesday', 'friday']
# @app.route('/home')


@app.route("/")
def home():
    return render_template("home.html")


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
    return render_template("users.html", name=name)
if __name__ == '__main__':
    app.run(debug=True)
