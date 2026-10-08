def to_nums(text):
    return [ord(c) - 97 for c in text.lower() if c.isalpha()]


def to_text(nums):
    return "".join(chr(n % 26 + 97) for n in nums)


plaintext = input("Enter the plaintext: ")
key = list(map(int, input("Enter the key stream: ").split()))
p = to_nums(plaintext)
if len(key) < len(p):
    raise SystemExit("The key stream is shorter than the plaintext")
c = [(a + k) % 26 for a, k in zip(p, key)]
print("(a) Plaintext numbers :", p)
print("    Ciphertext numbers:", c)
print("    Ciphertext        :", to_text(c))
target = input("Enter the plaintext required from the same ciphertext: ")
t = to_nums(target)
new_key = [(ci - ti) % 26 for ci, ti in zip(c, t)]
print("(b) Required key stream:", " ".join(map(str, new_key)))
check = [(ci - k) % 26 for ci, k in zip(c, new_key)]
print("    Decrypting with this key gives:", to_text(check))
