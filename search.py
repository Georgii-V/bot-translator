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
    {"text": "I learned very early the difference between knowing the name of something and knowing something.",
     "level": 2}
]


users = []


def find_user_lvl(new_user):
    new_user_id = new_user.get('id')
    for user in users:
        if new_user_id == user.get('id'):
            return user.get('lvl')


def fill_matched_sentences(message, user, sentences = sentences)->list:
    matched_sentences = []

    for sentence in sentences:
        user_lvl = find_user_lvl(user)
        sentences_lvl = sentence.get("level")
        sentences_txt = sentence.get("text")

        if  sentences_lvl == user_lvl:
            if message.lower() in sentences_txt.lower():
                matched_sentences.append(sentences_txt)
    return matched_sentences


def check_user(new_user: dict): 
    is_user = False

    for user in users:
        if new_user.get('id') == user.get('id'):
            is_user = True
    return is_user


def write_new_user(user_data: dict, level: str):
    user_data['lvl'] = int(level)
    users.append(user_data)


def create_result_message(matched_sentences:list)->str:
    result_message = ""
    if not matched_sentences:
        result_message = "Sorry, not found sentences for your request"
    if len(matched_sentences) == 1:
        result_message = matched_sentences[0]
    if len(matched_sentences) > 1:
            for x in matched_sentences:
                result_message += x + "\n...\n"
    return result_message

        


