def vigenere(text, key, direction):
    result, j = "", 0
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shift = ord(key[j % len(key)]) - ord("A")
            result += chr((ord(ch) - base + direction * shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result


plaintext = input("Enter the plaintext: ")
key = input("Enter the key (letters only): ").upper()
if key.isalpha():
    ciphertext = vigenere(plaintext, key, 1)
    print("Ciphertext :", ciphertext)
    print("Decrypted  :", vigenere(ciphertext, key, -1))
else:
    print("The key must contain letters only")
