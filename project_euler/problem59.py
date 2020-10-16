'''
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange).
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key
on the cipher text, restores the plain text; for example,
65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using p059_cipher.txt, a file containing the encrypted ASCII
codes, and the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.
'''

import os
import string
from itertools import permutations

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'p059_cipher.txt')) as cipher_file:
    cipher_text = cipher_file.read().split(',')


def returnSumOfDecryptedAscii():
    for x in permutations(string.ascii_lowercase, 3):
        message = []
        i = 0
        for c in cipher_text:
            if i == 3:
                i = 0
            key = ord(x[i])
            message.append(int(c) ^ key)
            i += 1
        decrypted_message = ''
        for char in message:
            decrypted_message = decrypted_message + chr(char)
            if decrypted_message.count('the') > 2 \
                    and decrypted_message.count('that') > 2:
                print(x)
                print(decrypted_message)
                return sum(message)


print(returnSumOfDecryptedAscii())
