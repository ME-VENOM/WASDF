import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAB4pDbVlunrDmu5o1yWYvhjto1f-w6oC9QiYXgzTxAphPnuh3_3wbkbjCM4K-0s5kR_JYavfUq6aeAE_7yhzceVHnRQCItqTPl9oCnuxqIIV8ndR7b2-0g89uZVLCt-MQmhNaiYX_oifXHWNmAwisAllluDUo9MclssMf7jsyS8CmWWFf6YCPU_RWHsC4toHu5NjS4YmQKNNzJ5a5taardUxSSpPAbK7G3JwQj3-hv4svbsJN5_TFvwtDcgOcQslYS-33YznHcrin6CneWrurXTHEoxLItB55fnx9LAgI3k5IG-slXcw0JSfFiV5vbD-fOBHRKi1HRmfUeFAPY8aET5btE_FQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5291289945:AAGUiZ_CA6drdWbr5tdl6UYpwhDrPJKZ12M")
BOT_NAME = getenv("BOT_NAME", "RREWQYUBOT")
API_ID = int(getenv("API_ID", "17320595"))
API_HASH = getenv("API_HASH", "bb0fbf90e7c8f09160608d1962200221")
OWNER_NAME = getenv("OWNER_NAME", "QABNADLIB")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
ALIVE_NAME = getenv("ALIVE_NAME", "")
BOT_USERNAME = getenv("BOT_USERNAME", "RREWQYUBOT")
OWNER_ID = getenv("OWNER_ID")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "faqek")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "VFF35")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1939538780").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/8951a422fad655259d86a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ERTWF/WASDF")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/880f7e9706591af8d0bfa.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/324399325cf48ff25a494.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/e53f65a49c4ee5553fab9.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a79d792baacc982ff57bd.jpg")
