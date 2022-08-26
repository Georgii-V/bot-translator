users = [{
		   "user_id":777,
		   "username": "Freg",
		   "user_level":2},
		  {
			  "user_id":383,
		  	"username": "Oleg",
		 	"user_level":1},
		  {
		  	"user_id":918,
		  	"username": "Anna",
		  	"user_level":3
		  }]


sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]


req_from_server = {"user_id":777, "text":"in"}


def filter_by_lvl(level, raw_sentences):
	filtered_sentences = []
	for sentence in raw_sentences:
		if level == sentence.get("level"):
			filtered_sentences.append(sentence)
	return filtered_sentences 


def filter_by_word(word, raw_sentences):
	filtered_sentences = []
	for sentence in raw_sentences:
		if word in sentence.get("text"):
			filtered_sentences.append(sentence)
	return filtered_sentences 


def convert_sentences(filtered_sentences):
	converted_sentences = []
	for sentence in filtered_sentences:
		converted_sentences.append(sentence.get("text"))
	return converted_sentences

def prepare_message(sentences):
	if len(sentences) == 0 :
		return "result not found"
	else: 
		return "\n".join(sentences)
	

def search_user(id, users):
	for user in users:
		if id == user.get("user_id"):
			return user


def send_message(message):
	print(message)

id = req_from_server.get("user_id")
user = search_user(id, users)
user_lvl = user.get("user_level")

word = req_from_server.get("text")
filtered_by_words = filter_by_word(word, sentences)
matched_sentences = filter_by_lvl(user_lvl, filtered_by_words)
text_of_sentences = convert_sentences(matched_sentences)
message = prepare_message(text_of_sentences)

send_message(message)