paragraph = """This is not a Palindrom sentence mom, Bob  its a simple code
but this new line will not have any palindrome
how can mom"""
count = 0
for sentence in paragraph.split('\n'):
    for word in sentence.split(' '):
        word = word.replace(',', '').upper()
        if len(word) < 2:
            continue
        if word == word[::-1]:
            count += 1
    print('number of palindrom in "{}" is {}'.format(sentence, count))
    count = 0