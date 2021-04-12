'''
pip install  flask

### running in windows

open cmd-> move to the project folder
cmd: set FLASK_APP=name_of_file.py
cmd: flask run

'''

from flask import Flask, render_template, request

app =Flask(__name__)

@app.route('/')
def helloWorld():
    return "<h1>helloWorld</h1>"

@app.route('/predict',methods=["GET","POST"])
def predict():
    data= {"success":False}
    request.json


if __name__=="__main__":
    app.run(debug=True)
