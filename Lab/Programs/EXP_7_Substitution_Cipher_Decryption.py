from collections import Counter

ciphertext = input("Enter the ciphertext: ").replace(" ", "")
print("Length of ciphertext:", len(ciphertext))


freq = Counter(ciphertext)
print("Most frequent symbols:")
for symbol, count in freq.most_common(8):
    print("   %s  appears %d times" % (symbol, count))


guess = {freq.most_common(1)[0][0]: "e"}


trigrams = Counter(ciphertext[i:i + 3] for i in range(len(ciphertext) - 2))
for tri, count in trigrams.most_common():
    if tri[2] in guess:
        guess[tri[0]], guess[tri[1]] = "t", "h"
        print("Most common trigram ending in e: %s -> 'the' (%d times)"
              % (tri, count))
        break
print("Partial decryption:")
print("  ", "".join(guess.get(c, "_") for c in ciphertext))


KEY = ("5a 2b —c †d 8e 1f 3g 4h 6i 0l 9m *n ‡o .p (r )s "
       ";t ?u ¶v ]w :y")
mapping = {item[0]: item[1] for item in KEY.split()}
print("Substitution table:", KEY)
plaintext = "".join(mapping.get(c, c) for c in ciphertext)
print("Decrypted message:")
print("  ", plaintext)
