# Encrypted Messaging program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Encrypt

plain_text = input("Enter a message to encrypt: ")
encrypt_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypt_text += key[index]

print(f"Your message encrypted is: {encrypt_text}")

# Decrypt

encrypt_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in encrypt_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Your message encrypted is: {plain_text}")