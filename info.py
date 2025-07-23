import re
from os import environ,getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
    
# Main
SESSION = environ.get('SESSION', 'anuj_session')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
PORT = environ.get('PORT', '8082')

# Owners 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5454951641 5513858070').split()]
OWNER_USERNAME = environ.get('OWNER_USERNAME', 'DOCTORXANUJ') # without @ or https://t.me/ 
USERNAME = environ.get('USERNAME', "@ANUJVIRUS") # ADMIN USERNAME

# Database Channel 
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '1002481896248').split()]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002796809199'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1002829933094'))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002717319391'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002717319391')) 
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002717319391'))

# MongoDB 
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "TNJDATABASE")

# Files index database url
FILES_DATABASE = environ.get('FILES_DATABASE', "")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TNJCOLLECTION')

# Other Channel's
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '7581094364'))
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','0'))
request_channel = environ.get('REQUEST_CHANNEL', '-1002796809199') 
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None
UPDATE_CHANNEL = int(environ.get('UPDATE_CHANNEL', '-1002779754485')) 

# Added Link Here Not Id 
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/TNJCENTERBOT')
GROUP_LINK = environ.get('GROUP_LINK', 'https://t.me/QuizTNJ')

# Verification
IS_VERIFY = is_enabled('IS_VERIFY', False)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://ibb.co/271MRHBP")
SHORTENER_API = environ.get("SHORTENER_API", "not now")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'no here now')
SHORTENER_API2 = environ.get("SHORTENER_API2", "not now")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'not now')
SHORTENER_API3 = environ.get("SHORTENER_API3", "not now")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'not now')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# Batch & Subject & Chapter & Lecture & Type
BATCH = ["1.0", "2.0", "3.0", "4.0", "5.0", "6.0"]
SUBJECT = ["PHYSICS", "PHYSICAL CHEM", "ZOOLOGY", "BOTANY", "ORGANIC CHEM", "INORGANIC CHEM"]
CHAPTER = ["CH-1", "CH-2", "CH-3", "CH-4", "CH-5", "CH-6", "CH-7", "CH-8", "CH-9", "CH-10", "CH-11", "CH-12", "CH-13", "CH-14", "CH-15", "CH-16", "CH-17"]
LECTURE = ["L-1", "L-2", "L-3", "L-4", "L-5", "L-6", "L-7", "L-8", "L-9", "L-10", "L-11", "L-12", "L-13", "L-14", "L-15", "L-16", "L-17", "L-18", "L-19", "L-20"]
TYPE = ["CLASSNOTES", "LECTURE", "DPP", "DPP QUIZ", "ASSIGNMENT", "HOMEWORK", "PLANNER", "SHORTS NOTES", "PYQS"]

# Pictures And Reaction
START_IMG = (environ.get('START_IMG', 'https://ibb.co/RpGvhpD2 https://ibb.co/4nfkX2yf')).split()
FORCESUB_IMG = environ.get('FORCESUB_IMG', 'https://i.ibb.co/ZNC1Hnb/ad3f2c88a8f2.jpg')
REFER_PICS = (environ.get("REFER_PICS", "https://ibb.co/nvTq5V8")).split() 
PAYPICS = (environ.get('PAYPICS', 'https://ibb.co/SXX4FJ8T')).split()
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://ibb.co/RTM0znRF'))
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡" "❤️", "🫶", "🌱", "🩺", "🇮🇳", "🧡", "🩷", "💛", "🍔", "🍨", "🎂", "🥼"]


#Other Funtions
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', False)
IS_SEND_MOVIE_UPDATE = is_enabled('IS_SEND_MOVIE_UPDATE', False) # Don't Change It ( If You Want To Turn It On Then Turn It On By Commands) We Suggest You To Make It Turn Off If You Are Indexing Files First Time.
MAX_BTN = int(environ.get('MAX_BTN', '10'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 1200))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
TMDB_API_KEY = environ.get("TMDB_API_KEY", "")

# Online Streaming And Download 
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or Flase

MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")

# Commands
admin_cmds = [
    "/add_premium - Add A User To Premium", 
    "/premium_users - View All Premium Users", 
    "/remove_premium - Remove A User's Premium Status", 
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trail", 
    "/set_muc - Set Lecture Update Channel", 
    "/pm_search_on - Enable PM Search", 
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements", 
    "/del_ads - Delete Advertisements", 
    "/setlist - Set Top Trending List", 
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID", 
    "/index - Index Files", 
    "/send - Send Message To A User", 
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User", 
    "/unban - Unban A User", 
    "/broadcast - Broadcast Message", 
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request", 
    "/channel - List Of Database Channels", 
    "/del_file - Delete A Specific File", 
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files", 
    "/deleteall - Delete All Files"
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "𝖦𝖾𝗍 𝖳𝗈𝗉 𝖳𝗋𝖾𝗇𝖽𝗂𝗇𝗀 𝖡𝗎𝗍𝗍𝗈𝗇 𝖫𝗂𝗌t"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Currunt Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"}
]

