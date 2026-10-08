from math import gcd

COMMON = "ETAOINSHRDLU"


def num(ch):
    return ord(ch) - ord("A")


def decrypt(text, a, b):
    inv = pow(a, -1, 26)
    return "".join(chr((inv * (num(c) - b)) % 26 + 65) if c.isalpha()
                   else c for c in text)


c1 = input("Enter the most frequent ciphertext letter: ").upper()
c2 = input("Enter the second most frequent ciphertext letter: ").upper()
ciphertext = input("Enter the ciphertext to decrypt: ").upper()
candidates = []
for p1 in COMMON:
    for p2 in COMMON:
        if p1 == p2:
            continue
        for a in range(26):
            if gcd(a, 26) != 1:
                continue
            if (a * (num(p1) - num(p2))) % 26 == (num(c1) - num(c2)) % 26:
                b = (num(c1) - a * num(p1)) % 26
                candidates.append((p1, p2, a, b))
print("Assumption (%s -> %s, %s -> %s)" % (COMMON[0], c1, COMMON[1], c2))
print("Candidate keys in order of likelihood:")
for p1, p2, a, b in candidates[:5]:
    print("  %s->%s, %s->%s  gives a = %d, b = %d" % (p1, c1, p2, c2, a, b))
p1, p2, a, b = candidates[0]
print("Selected key: a = %d, b = %d" % (a, b))
print("Decrypted text:", decrypt(ciphertext, a, b))
