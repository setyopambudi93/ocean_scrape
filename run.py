import requests
from bs4 import BeautifulSoup
from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"







if __name__== '__main__':
    app.run(debug=True)