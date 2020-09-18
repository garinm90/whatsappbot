import requests
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


covid_status_by_country = 'https://covid19-api.org/api/status/'


@app.route('/', methods=['GET'])
def index():
    country = request.args.get('country')
    r = requests.get(covid_status_by_country+country)
    return jsonify(r.json())


if __name__ == '__main__':
    app.run(port=5000)
