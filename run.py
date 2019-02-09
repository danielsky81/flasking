import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = []
    with open('data/surfers.json', 'r') as json_data:
        data = json.load(json_data)
    return render_template('index.html', page_title='Legendary Surfers', surfers=data)


@app.route('/about')
def about():
    return render_template('about.html', page_title='About')


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact')
