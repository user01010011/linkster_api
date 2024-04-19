from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin 
import requests 
from dotenv import load_dotenv 
import os 

# Load environment variables 
load_dotenv()

# Initialize Flask app 
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello World! :)"

if __name__ == '__main__': 
    app.run(port=8081, debug=True)