# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = 7392881
    API_HASH = "8c6390da22f0b6a34ee95ab5bf4ddd9f"
    BOT_TOKEN = "1412992512:AAHb8GUexB17g_v9O990SLRWM4OPf64QhnU"
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(-559454773)    
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    HAS_SSL = getenv('HAS_SSL', True)
    HAS_SSL = True
    # OWNER_ID = int(getenv('OWNER_ID')) #TODO
    NO_PORT = getenv('NO_PORT', False)
    NO_PORT = False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = 'route0'
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    if ON_HEROKU:
        URL = f"https://{FQDN}/"     
    else:
        URL = "http{}://{}{}/".format('s' if HAS_SSL else '', FQDN, '' if NO_PORT else ':'+ str(PORT))
