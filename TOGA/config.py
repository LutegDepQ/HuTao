import json
import os


def get_user_list(config, key):
    with open('{}/TOGA/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER=True
    URL=False
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="/HuTao"
    DEL_CMDS=False
    BAN_STICKER=""
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="mongodb://mongo:AGa15Ss8QAIMgnq3ZWGJ@containers-us-west-146.railway.app:7117"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot5909830565:AAG9iFyfJS48b28orh8s5eObylTQHs-mSpo/sendMessage?chat_id=<chat_id>&text=<Enter your text here>"
    #kacrmdi
    WOLVES=[]
    BOT_ID="5909830565" 
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:D5jeQ5St93M46hLVV0rx@containers-us-west-138.railway.app:6455/railway" 
    JOIN_LOGGER="" 
    API_HASH="08d2734295636f07a5ed6637116ea3ef" 
    INFOPIC=True
    TIGERS=[]
    API_ID="14472726"
    BL_CHATS=[1]
    DB_URL2="postgresql://postgres:D5jeQ5St93M46hLVV0rx@containers-us-west-138.railway.app:6455/railway" 
    TOKEN="5909830565:AAG9iFyfJS48b28orh8s5eObylTQHs-mSpo"
    DEV_USERS=[luteg_glh]
    DRAGONS=[]
    SPAMWATCH_API=""
    WALL_API=""
    DEMONS=[]
    SUPPORT_CHAT="mirror_gan"
    OWNER_USERNAME="luteg_glh"
    DONATION_LINK="https://saweria.co/Dare"
    EVENT_LOGS="" 
    OWNER_ID="716100216" 
    TIME_API_KEY=""
    ERROR_LOGS="" 
    BOT_NAME="胡桃"
    STRICT_GBAN=True
    REDIS_URL="redis://default:9s3Ewr3encHBCosBdGsj@containers-us-west-125.railway.app:6647"
    UPDATE_CHANNEL="mirror_gan_kanal"
    MONGO_DB_URI="mongodb://mongo:AGa15Ss8QAIMgnq3ZWGJ@containers-us-west-146.railway.app:7117"
    BOT_USERNAME="ltg_HuTao_bot"
    REM_BG_API_KEY=""
    CASH_API_KEY=""
    AI_API_KEY=""
    SPAMWATCH_SUPPORT_CHAT="SpamWatchSupport"
    OPENWEATHERMAP_ID=""
    LOG_GROUP_ID=""
    STRICT_GMUTE=False
    AFKVID=""
    GROUP_ALIVE_PIC=""
    SPAMWATCH_API=""
    OWNER_NAME = "Dare"
    BANCODES = ""
    REPOSITORY = "https://github.com/LutegDepQ/HuTao"
    RED7_TOKEN = ""

class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
