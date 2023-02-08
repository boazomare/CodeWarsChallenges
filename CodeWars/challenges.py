# Usually when you buy something, you're asked whether your credit card number,
# phone number or answer to your most secret question is still correct.
# However, since someone could look over your shoulder, you don't want that shown on your screen.
# Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into
from getpass import getpass
def maskify(text):
    text = ''.join(text.split())
    characterList = list(text)
    last4characters = characterList[-4:]
    length = len(characterList) - 4
    mask = []
    for i in range(length):
        mask.append('#')
    string = mask + last4characters
    print(''.join(string))
text = getpass("Enter your security answer >")
maskify(text)
