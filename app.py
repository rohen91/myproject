from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my first application!! "


@app.route('/sub')
def welcome1():
    return "Welcome to the next page!! "


if __name__=='__main__':
    app.run(debug=True)
