import string


def make_alphabet(keyword):
    sequence = ""
    for ch in keyword.upper() + string.ascii_uppercase:
        if ch.isalpha() and ch not in sequence:
            sequence += ch
    return sequence


def substitute(text, source, target):
    table = {}
    for s, t in zip(source, target):
        table[s] = t
        table[s.lower()] = t.lower()
    return "".join(table.get(ch, ch) for ch in text)


keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")
alphabet = string.ascii_uppercase
cipher_alphabet = make_alphabet(keyword)
print("plain :", " ".join(alphabet.lower()))
print("cipher:", " ".join(cipher_alphabet))
ciphertext = substitute(plaintext, alphabet, cipher_alphabet)
print("Ciphertext :", ciphertext)
print("Decrypted  :", substitute(ciphertext, cipher_alphabet, alphabet))
