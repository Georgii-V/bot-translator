import requests

# arg = Receive word
from search import search_sentence, check_user, write_new_user


root_url = 'https://api.telegram.org/bot'
token = '5575207027:AAEy_tAw2p11W2lnSyz0rx1DFJhGEfGJ2Qk'
positive_codes = (200, 201, 202, 203, 204)


def get_update(root_url: str, token: str):
    url = f'{root_url}{token}/getUpdates'
    res = requests.get(url)
    if res.status_code in positive_codes:
        return res.json()
    else:
        print(f'bad request {res.status_code}')


def get_message_data(update_dict: dict):
	last_message = update_dict.get('result')[-1]
	user_data = last_message.get('message').get('from') # USER
	chat_id = last_message.get('message').get('chat').get('id')
	message_id = last_message.get('message').get('message_id')
	last_text = last_message.get('message').get('text')
	return user_data, chat_id, message_id, last_text


def search_word(text: str, user: dict):
	id = user.get('id')
	found = search_sentence(text, id)
	return found


def send_message(root_url: str, token: str, chat_id: int, found_text: list):
	prepared_res = '\n'.join(found_text)
	to_send = requests.post(f'{root_url}{token}/sendMessage', data = {'chat_id': chat_id, 'text': prepared_res})
	return to_send


def send_lvl_req(root_url: str, token: str, chat_id: int):
	to_send = requests.post(f'{root_url}{token}/sendMessage', data = {'chat_id': chat_id, 'text': 'Enter your level'})
	return to_send


def get_level(old_message_id):
	new_message_id = old_message_id

	while old_message_id == new_message_id:
		new_data = get_update(root_url, token) 
		user_data, chat_id, message_id, last_text = get_message_data(new_data)

		new_message_id = message_id
		if new_message_id > old_message_id:
			return int(last_text)



last_message_id = 0
print(last_message_id)


while True:
	new_data = get_update(root_url, token) 
	user_data, chat_id, message_id, last_text = get_message_data(new_data)
	cheked_user = check_user(user_data)


	if not cheked_user:
		send_lvl_req(root_url, token, chat_id)
		added_user_lvl = get_level(message_id)
		write_new_user(user_data, added_user_lvl)

	else:
		if message_id > last_message_id:
			found_sentence = search_word(last_text, user_data)
			send_message(root_url, token, chat_id, found_sentence)
			last_message_id = message_id



# print(found_sentence)