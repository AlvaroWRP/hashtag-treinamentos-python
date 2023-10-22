import string
from collections import Counter

def remove_punctuation(user_text):
    for char in user_text:
        if char in string.punctuation:
            user_text = user_text.replace(char, '')

    return user_text

user_text = input('Type something: ')

user_text = remove_punctuation(user_text)
user_text = user_text.lower().split()

words_counter = Counter(user_text)
total_words = len(user_text)

letters_dict = {}

for word in user_text:
    for char in word:
        if char not in letters_dict:
            letters_dict.update({char: 1})
        else:
            letters_dict[char] += 1

print(user_text)
print(letters_dict)
print(words_counter)
print(total_words)
