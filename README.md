## Table of contents
- [Table of contents](#table-of-contents)
- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)

## General info
This project setups a bot you can text via [WhatsApp](https://www.whatsapp.com/) and recieve current stats about Covid-19.

## Technologies
This project primarmily makes use of:
* Flask
* Twilio
* Python 3.8.2

## Setup
To run this project you will need soemwhere to host this website,
this can be done locally via [Ngrok](https://ngrok.com/) or for free on [Heroku](https://heroku.com).

Also an account with [Twilio](https://www.twilio.com/) will be needed to use the WhatsApp api. 

Start by cloning this repository
```
git clone https://github.com/garinm90/whatsappbot.git
```

Then move into the directory
```
cd ./whatsappbot
```

Next you will need to setup your virtualenviroment. Using venv
```
python -m venv venv
source ./venv/bin/activate
```
or if you prefer pipenv
```
pipenv install
pipenv shell
```

After that you can either host with [ngrok](https://ngrok.com/docs#getting-started-expose).

If doing so you will need to setup some enviroment variables. There is a sample dotenv file included. 
```
mv .env_sample .env
Open .env and set the following two variables
ACCOUNT_SID=TWILIO_SID_GOES_HERE
AUTH_TOKEN=TWILIO_AUTH_KEY_GOES_HERE
```

These can be found on the twilio console..
