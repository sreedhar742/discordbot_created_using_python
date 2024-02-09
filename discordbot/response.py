from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered == '':
        return 'Well, youare awfully silent...'
    elif "hii" in lowered:
        return 'how do you do....'
    elif 'hello' in lowered:
        return 'Hello there...!'
    elif 'how are you' in lowered:
        return 'Good, thanks..!'
    elif 'bye' in lowered:
        return 'See you....soon!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])