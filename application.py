from flask import Flask, render_template
application = Flask(__name__, static_url_path='/static')

@application.route("/")
def index():
    return render_template('index.html')

@application.route("/team/")
def team():
    return render_template('team.html')

@application.route("/demo1/")
def demo1():
    return render_template('demo1.html')

@application.route("/demo2/")
def demo2():
    return render_template('demo2.html')

@application.route("/demo3/")
def demo3():
    return render_template('demo3.html')

if __name__ == '__main__':
    application.run(debug=True)
