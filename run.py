from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    with open('front-end/home.html', 'r') as file:
        content = file.read()
    return content

if __name__ == '__main__':
    app.run(debug=True, port=5000)