import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT
cipher_input = input("Enter a message to decrypt: ")  # Take encrypted message
decrypted_text = ""  # Store decrypted message

for letter in cipher_input:
    index = key.index(letter)  # Find letter in shuffled key
    decrypted_text += chars[index]  # Get original letter

print(f"Encrypted message: {cipher_input}")
print(f"Decrypted message: {decrypted_text}")  # Correctly restored message



