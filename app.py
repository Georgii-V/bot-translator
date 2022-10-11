import requests

from search import fill_matched_sentences, write_new_user, create_result_message, check_user
 
token = '5575207027:AAEy_tAw2p11W2lnSyz0rx1DFJhGEfGJ2Qk'
positive_codes = (200, 201, 202, 203, 204)

class Bot:
	root_url = 'https://api.telegram.org/bot'

	def __init__(self, token=None):
		self.token = token

	def get_updates(self):
		url = f"{self.root_url}{self.token}/getUpdates"
		res = requests.get(url)

		if res.status_code in positive_codes:
			updates = res.json()
			return updates

	def send_message(self, chat_id, message):
		url = f"{self.root_url}{self.token}/sendMessage"
		res = requests.post(url, data={'chat_id': chat_id, "text": message})
		if res.status_code in positive_codes:
			return True
		else:
			print(f"Request failed with status_code {res.status_code}")
			return False

	def process_message(self, message:str, user:dict)->str:
		if message == '/start':
			message = 'Please, let me know your English level.\nFor this use command:\n/level_?\n? = your level\nLevels:\n0 - Beginner\n1 - Intermediate\n2 - Advanced'
		
		elif '/level_' in message:
			level = message[-1]
			if int(level) in range(3):
				write_new_user(user, level)
				message = f'Great, your level is {level}, now send me your word'
			else:
				message = 'Incorrect level'

		elif '/*' in message:
			message = 'Command not found'
		else:
			matched_sentences = fill_matched_sentences(message, user)
			message = create_result_message(matched_sentences)
		
		return message

	def poolling(self):
		last_message_id = 0
		unlogged_users = []

		while True:
			updates = self.get_updates()
			messages = updates["result"]

			if len(messages) < 1:
				continue

			last_message = updates["result"][-1]
			user = last_message.get('message').get('from')
			is_user = check_user(user)
			message_id = last_message["message"]["message_id"]
			
			last_message_text = last_message["message"]["text"]
			chat_id = last_message["message"]["chat"]["id"]	


			if not is_user:
				if not user in unlogged_users:
					warning_text = 'WWW\nPlease, let me know your English level.\nFor this use command:\n/level_?\n? = your level\nLevels:\n0 - Beginner\n1 - Intermediate\n2 - Advanced'
					self.send_message(chat_id, warning_text)
					unlogged_users.append(user)


			if message_id > last_message_id:
				message_to_user = self.process_message(last_message_text, user)
				self.send_message(chat_id, message_to_user)
				last_message_id = message_id


bot = Bot(token)
bot.poolling()
