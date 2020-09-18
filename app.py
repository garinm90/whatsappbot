from typing import Counter
import requests
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import pycountry
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


covid_status_by_country = 'https://covid19-api.org/api/status/'


@app.route('/', methods=['GET', 'POST'])
def index():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if request.method == 'POST':
        try:
            country = pycountry.countries.lookup(body)
        except LookupError:
            msg = resp.message(
                'Please enter a valid two character country code.')
            return str(msg)
    else:
        return '<h1>Please specify a country</h1>'


if __name__ == '__main__':
    app.run(port=5000)
