import requests

token = '5575207027:AAEy_tAw2p11W2lnSyz0rx1DFJhGEfGJ2Qk'
root_url = 'https://api.telegram.org/bot'
positive_codes = (200, 201, 202, 203, 204)


def get_update(root_url: str, token: str):
	url = f'{root_url}{token}/getUpdates'
	res = requests.get(url)
	if res.status_code in positive_codes:
		return res.json()
	else:
		print(f'bad request {res.status_code}')


def get_data():
	response = get_update(root_url, token)
	message_id = response.get('result')[-1].get('message').get('message_id')
	last_messages = response.get('result')[-1].get('message').get('text')
	chat_id = response.get('result')[-1].get('message').get('chat').get('id')
	data = {'chat_id': chat_id, 'text': last_messages}
	return data, message_id


def send_message(root_url: str, token: str, data: dict):
	url = f'{root_url}{token}/sendMessage'
	send_message = requests.post(url, data)
	if send_message.status_code in positive_codes:
		return True
	else:
		print(f'bad request {send_message.status_code}')


last_message_id = 0

while True:
	data, message_id = get_data()

	if message_id > last_message_id:
		send_message(root_url, token, data)
		last_message_id = message_id






