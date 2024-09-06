import os
import sys
from flask import Flask, render_template

sys.path.insert(0, os.path.dirname(__file__))
JSON_FILE_PATH = 'products.json'

# Create a Flask app
app = Flask(__name__)



# Define a route
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
