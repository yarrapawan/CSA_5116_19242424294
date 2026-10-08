def caesar(text, k):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + k) % 26 + base)
        else:
            result += ch
    return result


plaintext = input("Enter the plaintext: ")
k = int(input("Enter the key k (1-25): "))
if 1 <= k <= 25:
    ciphertext = caesar(plaintext, k)
    print("Ciphertext :", ciphertext)
    print("Decrypted  :", caesar(ciphertext, -k))
else:
    print("Key must be in the range 1 to 25")
