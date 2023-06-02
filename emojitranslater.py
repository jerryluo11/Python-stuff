message = input('> ')

def emoji_convert(message):
    words = message.split(' ')
    emojis = {
        ':)': '😀',
        ':(': '🙁'
    }
    output = ''
    for word in words:
        output+=emojis.get(word, word) + ' '
    return output
print(emoji_convert(message))
print(emoji_convert(':) And :('))