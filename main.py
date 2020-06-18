import instabot

f = open("message.txt", "r")
response = f.read()
bot = instabot.Bot(message_delay=0)
bot.login()
bot.api.get_inbox_v2()
data = bot.last_json["inbox"]["threads"]
for item in data:
	user_id = str(item["inviter"]["pk"])
	bot.send_message(response, user_id)
