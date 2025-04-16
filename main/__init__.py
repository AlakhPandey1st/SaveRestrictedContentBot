#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 15578503
API_HASH = "de14eccfa6fa8d7c2eee9656cc2bdc69"
BOT_TOKEN = "7385687851:AAFPTClb1UY-CV6C4rJCd3_uwZ8ej9MfkTw"
SESSION = "BQDttYcAVKFp93K0a8JridkrZh0jUB81wtdpsi98IoV7cU-rhyLD2gOU2f0zT0SQ8ilgjF8CB8o5WM08ftIxh2ifNjukZ_8j3q_WWctRCaV6ZuB0V6xsrdip_rzWw9RdxqAhUgMM8E_bx8mtIM7RHCp7WN0gqrdzFl4rDyixAJO3DceOizwJui4JaagIhznokC1IyoKm7EvQiDaXc8S4UU9UdN6kBnYQd1fSquidulMe-9I8daBqzs_-RABy8-bZs7kDvklGKnJTR01933e0lev7ws8VtvtcgGK9Ppd3IqwIfW6v5tvM6D9vXDZa4kWSP7VRrxQaiel3tjylzZv1srrzHZ8bMwAAAAFJWkbdAA"
FORCESUB = "DroneBots"
AUTH = 5525620445

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
