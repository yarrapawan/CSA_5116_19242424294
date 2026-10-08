ENGLISH = [8.17, 1.49, 2.78, 4.25, 12.70, 2.23, 2.02, 6.09, 6.97, 0.15,
           0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.10, 5.99, 6.33, 9.06,
           2.76, 0.98, 2.36, 0.15, 1.97, 0.07]


def shift(text, k):
    return "".join(chr((ord(c) - 65 - k) % 26 + 65) for c in text)


def chi_square(text):
    n = len(text)
    total = 0.0
    for i in range(26):
        observed = text.count(chr(65 + i))
        expected = ENGLISH[i] * n / 100
        total += (observed - expected) ** 2 / expected
    return total


ciphertext = input("Enter the ciphertext: ").upper()
top = int(input("How many top plaintexts do you want to see: "))
letters = "".join(c for c in ciphertext if c.isalpha())
candidates = []
for k in range(26):
    plain = shift(letters, k)
    candidates.append((chi_square(plain), k, plain))
candidates.sort()
print("Rank  Key   Chi-square   Plaintext")
for rank, (score, k, plain) in enumerate(candidates[:top], 1):
    print("%3d   %2d   %9.2f   %s" % (rank, k, score, plain))
