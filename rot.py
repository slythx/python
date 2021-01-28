#!/usr/bin/python3

'''
Author: Slytherin
Date created: 1/24/2020
Description: This tool shifts both uppercase and lowercase letters only to the right depending on user's input rot #
Example: ROT13
    - Encrypted string: 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'
    - Decrypted string: 'The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu'
    - Source: https://overthewire.org/wargames/bandit/bandit12.html
'''

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
string = str(input('Enter encrypted string: '))
start, decrypted = 0, ''

try:
    rot = int(input('Enter ROT #: '))
except Exception:
    print('ERROR! Enter numeric value only for ROT #')
    print('== Program execution ended ==')
    exit()

for i in range(len(string)):
    if string[i].lower() in ascii_lowercase:
        pos = ascii_lowercase.index(string[i].lower())
        rot_pos = pos + rot
        if rot_pos >= len(ascii_lowercase):
            char = ascii_lowercase[rot_pos - len(ascii_lowercase)]
        else:
            char = ascii_lowercase[pos + rot]
        decrypted += char.upper() if string[i].isupper() else char
    else:
        decrypted += string[i]

print(f"Decrypted string: {decrypted}")
print('== End ==')


