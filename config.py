# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23476439"))
API_HASH = getenv("API_HASH", "1626e884119a29dbccbb78e39b48128f")
BOT_TOKEN = getenv("BOT_TOKEN", "7214405015:AAHeKGw4aIlpZpyqTV1owUypwkeY50vqQLs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5993556795").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn")
LOG_GROUP = getenv("LOG_GROUP", "-1002175816545")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002207508831"))
