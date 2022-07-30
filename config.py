import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BAAZhTdlu00Mi1_R4ZpxfXehGuy7vBF5k1mtTj-kJb1sC69UGeCyxJtNcdnHMi1IW61CQ-lqVChZdHEP7nlmQCxXyNPnmk6WGcCAzmLvblLFUx641vRGZeIkoTmUFsBfg5fAPDtzqRUDYr3sGOSzJi1AMk1OSzkTuEKyHpoC26pGmSQQgNVnw56nyq2PNeEYRjDNBuNE6QXqFNOrJepgNLdV7qKJ1UBo-as4uNbB80ZWsZVNUh7RWo67Tf-8ljDSp1ZLKbf1EphOajjJT47RS4BazkRHqSzBGgzxRcdZcHCLiCWPPvkkfC4nfObQtQEATzPjxdiz7qVcbjPY3MSjnzJoAAAAAT1HYPoA")
BOT_TOKEN = getenv("5596139909:AAFfRbufask48at29S9ZBso0SqJM9RMkboU")
BOT_NAME = getenv("BOT_NAME", "music jano")
API_ID = int(getenv("11464236"))
API_HASH = getenv("2b556f89fc1efce6b7489570d21ce474")
OWNER_NAME = getenv("OWNER_NAME", "jano")
ALIVE_NAME = getenv("ALIVE_NAME", "jano")
BOT_USERNAME = getenv("BOT_USERNAME", "MUSIC_Jl_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "جانو")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "akd444s")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "akd444s")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "ف ب غ س ك و م ا ت / ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/aa0ad3671257edd1ddace.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/VamBIR/free")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/aa0ad3671257edd1ddace.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/aa0ad3671257edd1ddace.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/aa0ad3671257edd1ddace.jpg")
