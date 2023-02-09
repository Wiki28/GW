import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "8529843")) #optional
API_HASH = getenv("API_HASH", "6e06fb8f7b42fb33821f272597321bc1") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "8529843")
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
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB3Nclg2VkxewrlSHy33jxQ6RrXrpJeQCbiz9bVkvNjeXeVMWmBVSS8pPnsKJBJfasPJetwrPz98vAUJ6yAwbdNHUrRtiMhhNY-MjwV0V38169dVtooHuGoc6hhw-VVFYdaMiZnymHsNTlaTcpR5EHt9h7c_Sn4E5UFZKMJFoWtrsEWfh0a6Dbh-2ZZN-1mpwKY-xQ0x55eoVSVEIfnwiwao3XUN6T28Or0lcQxb7ZfeG8TnfECJUra-G4HfGdoz_HREmhjns_M0naIYjTQVA9FZG9cljd_u3mj13WqM4dNZkPMUye1UuLK2ICGx3hID8yiyBD03e243gJApQEOFEQyfymgRgA")
STRING_SESSION2 = getenv("STRING_SESSION2", "BQA_l0Dyk6skulbHhf_ufg05F58Pkf6jes6rxdO3wSniuUC8dLTwc96bzzuCxqXCJ0GmWso_U6NWE0ds-1M9lIsX0fSMjLAtEQc_qO9VeAuqolILqV0cCPmS6APBPlCtaOn1IS7bUl0gf9JthvMlz8EEDU1M3bP8JlTu8hw1w3CGP0ZPZnzlOdnQuIPi4Am21lqcpr24N-S_5qMvaPcdxuqBxbNQqXnrecnM7z3nhBdbkC5jEkxoUUw8eyqac-K9WpaZ-Lb6eC7Hd-oWPgmD4utZBz8iDClcDXfWJoJYI7sn6wWsmCj44sjFGm7cFb-yqjPYQUrfL41n2aq5bIqKzG4FdgzYWwA")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
