from flask import Flask, render_template, request, jsonify, make_response, redirect
from os import popen
PWD = popen("pwd").read().replace('\n', '')
app = Flask(__name__, template_folder=PWD)

@app.route('/')
def index():
    if request.method=='GET':
        return render_template('index.html')
app.run(host='::', port=5000)
