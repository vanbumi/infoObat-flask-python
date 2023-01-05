from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@localhost/obat'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favobat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(30))
    description = db.Column(db.String(2000))

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