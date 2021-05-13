import json
import random

with open('emojis.json') as f:
  data = json.load(f)

emojis = data['emojis']

repetitions = 50
most_emojis_at_a_time = 5
msg = 'eid mubarak'
pasta = ''

def get_random_emoji():
    return emojis[random.randint(0, len(emojis) - 1)]['emoji']

def permute_msg_case(msg):
    return ''.join(random.choice((str.upper,str.lower))(x) for x in msg)

def augment_msg(msg):
    beginnings = [
        ' ',
        'DID YOU JUST SAY',
        'WOAH OMG, LITERALLY I ALSO WILL TELL YOU'
        'like who would have thought of that?',
        'so thoughtful of you',
        'THAT IS GENIUS'
        'SALUTATIONS AND'
        'I WISH YOU A VERY'
        'TO YOU, A VERY GOOD'
        'Aye oop',
        'Ay up',
        'Ahoy',
        'Good day',
        'Greetings',
        'Hello',
        'Hey there',
        'Hey',
        'Hi there',
        'Hi',
        'Hiya',
        'How are things',
        'How are ya',
        'How ya doin',
        'How is it goin',
        'How is it going',
        'How iss life',
        'Howdy',
        'Sup',
        'What is new',
        'What is up',
        'Yo'
    ]
    ends = [
        '??? so cool'
        'that is amazing'
        'spectacular'
        'BRUH'
        'thank you for thinking me'
        'that is very nice of you'
        'LIKE WOAH DUDE'
        'LIKE WOAH, I CANNOT BELIEVE YOU WOULD SAY SOMETHING LIKE'
        'I did not expect that you know?'
        'from someone like you??'
        ' '
    ]
    rand_beginning = permute_msg_case(beginnings[random.randint(0, len(beginnings) - 1)])
    rand_end = permute_msg_case(ends[random.randint(0, len(ends) - 1)])
    full_msg = f' {rand_beginning} {(permute_msg_case(msg) + " ") * random.randint(1, 20)} {rand_end} '

    augmented_msg = ''
    for word in full_msg.split(' '):
        augmented_msg += f' {word} {get_random_emoji()} '

    return augmented_msg

for i in range(repetitions):
    pasta += f' {augment_msg(msg)} '

print(pasta)