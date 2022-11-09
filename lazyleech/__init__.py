import os
import logging
import aiohttp
from io import BytesIO, StringIO
from pyrogram import Client

API_ID = os.environ.get('8978848')
API_HASH = os.environ.get('24ce3cff2d32cf529df1c0018e28d6cf')
BOT_TOKEN = os.environ.get('5078575505:AAGoXfcYLrtZVGDvQox2AT1SvMtL4pGhdlo')
TESTMODE = os.environ.get('TESTMODE')
TESTMODE = TESTMODE and TESTMODE != '0'
DB_URL = os.environ.get('mongodb+srv://batvps:Vps336mirror15botMongodb@batvps.a7gnvvx.mongodb.net/?retryWrites=true&w=majority')

EVERYONE_CHATS = os.environ.get('-1001816242004')
EVERYONE_CHATS = list(map(int, EVERYONE_CHATS.split(' '))) if EVERYONE_CHATS else []
ADMIN_CHATS = os.environ.get('-1001816242004')
ADMIN_CHATS = list(map(int, ADMIN_CHATS.split(' '))) if ADMIN_CHATS else []
ALL_CHATS = EVERYONE_CHATS + ADMIN_CHATS
# LICHER_* variables are for @animebatchstash and similar, not required
LICHER_CHAT = os.environ.get('LICHER_CHAT', '')
try:
    LICHER_CHAT = int(LICHER_CHAT)
except ValueError:
    pass
LICHER_STICKER = os.environ.get('LICHER_STICKER')
LICHER_FOOTER = os.environ.get('LICHER_FOOTER', '').encode().decode('unicode_escape')
LICHER_PARSE_EPISODE = os.environ.get('LICHER_PARSE_EPISODE')
LICHER_PARSE_EPISODE = LICHER_PARSE_EPISODE and LICHER_PARSE_EPISODE != '0'

PROGRESS_UPDATE_DELAY = int(os.environ.get('PROGRESS_UPDATE_DELAY', 5))
MAGNET_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 60))
LEECH_TIMEOUT = int(os.environ.get('LEECH_TIMEOUT', 300))
ARIA2_SECRET = os.environ.get('ARIA2_SECRET', '')

logging.basicConfig(level=logging.INFO)
app = Client('lazyleech', API_ID, API_HASH, plugins={'root': os.path.join(__package__, 'plugins')}, bot_token=BOT_TOKEN, test_mode=TESTMODE, parse_mode='html', sleep_threshold=30, ipv6=True)
session = aiohttp.ClientSession()
help_dict = dict()
preserved_logs = []

class SendAsZipFlag:
    pass

class ForceDocumentFlag:
    pass

def memory_file(name=None, contents=None, *, bytes=True):
    if isinstance(contents, str) and bytes:
        contents = contents.encode()
    file = BytesIO() if bytes else StringIO()
    if name:
        file.name = name
    if contents:
        file.write(contents)
        file.seek(0)
    return file
