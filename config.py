
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', "5964317287:AAEeYJgeEOp4ZrLbokSn_IXBkTXFogjA2ro")
    APP_ID = os.environ.get('APP_ID', "8256203")
    API_HASH = os.environ.get('API_HASH', "45b3b561298ee72408e08a3c46d5f697")

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
