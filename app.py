from typing import Counter
import requests
from flask import Flask, request, jsonify
from werkzeug.exceptions import abort
from twilio.twiml.messaging_response import MessagingResponse, Body, Message
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
    response = MessagingResponse()
    message = Message()
    if request.method == 'POST':
        try:
            country = pycountry.countries.lookup(body)
            r = requests.get(covid_status_by_country + country.alpha_2)
            json_data = r.json()
            message.body(f' In the {country.name} there are\
                            \n Total cases: {json_data["cases"]} \
                            \n Total deaths: {json_data["deaths"]} \
                            \n Total recovered: {json_data["recovered"]} ')
            response.append(message)
            return str(response)
        except LookupError:
            message.body('Please send a valid 2 digit country i.e. US')
            response.append(message)
            return str(response)
    if request.method == 'GET':
        return abort(404)


if __name__ == '__main__':
    app.run(port=5000)
