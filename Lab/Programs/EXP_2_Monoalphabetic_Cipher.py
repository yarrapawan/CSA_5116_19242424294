import string


def substitute(text, source, target):
    table = {}
    for s, t in zip(source, target):
        table[s] = t
        table[s.lower()] = t.lower()
    return "".join(table.get(ch, ch) for ch in text)


plaintext = input("Enter the plaintext: ")
key = input("Enter the 26 letter cipher alphabet: ").upper()
alphabet = string.ascii_uppercase
if sorted(key) == list(alphabet):
    ciphertext = substitute(plaintext, alphabet, key)
    print("Plain alphabet  :", alphabet)
    print("Cipher alphabet :", key)
    print("Ciphertext      :", ciphertext)
    print("Decrypted       :", substitute(ciphertext, key, alphabet))
else:
    print("Invalid key: use every letter exactly once")
