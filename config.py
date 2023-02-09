import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "8529843")) #optional
API_HASH = getenv("API_HASH", "6e06fb8f7b42fb33821f272597321bc1") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://not:not@cluster0.8rcyhkd.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5955445604:AAHfetV9cxbp9s9YCCJU3GxKgYLwuZ2lvb8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "-1001667983274")
OPENAI_API = getenv("OPENAI_API", "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")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/Wiki28/GW")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ",") 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
