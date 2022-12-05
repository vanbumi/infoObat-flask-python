from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    cars = ["Toyota", "Honda", "Mitsubishi"]
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>Hello dok ! From about page</h1>'

@app.route('/addobat')
def quotes():
    return render_template('infobat.html')

@app.route('/process', methods=['POST'])
def process():
    namaobat = request.form('namaobat')
    description = request.form('description')
    
    return redirect(url_for('index.html'))