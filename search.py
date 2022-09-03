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


def check_user(new_user: dict):
    for user in users:
        if new_user.get('id') == user.get('id'):
            return True
        else:
            return False


def write_new_user(user_data: dict, text: int):
    user_data['lvl'] = int(text)
    users.append(user_data)


def find_user_lvl(id):
    for user in users:
        if id == user.get('id'):
            return user.get('lvl')

def search_sentence(word, id):
    found_sentence = []
    found_user_lvl = find_user_lvl(id)

    for sentence_dict in sentences:
        if found_user_lvl == sentence_dict.get('level'):
            if word.lower() in sentence_dict.get('text').lower():
                found_sentence.append(sentence_dict.get('text'))

    if len(found_sentence) > 0:
        return found_sentence
    else:
        found_sentence.append('Nothing was found')
        return found_sentence

