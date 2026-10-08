import secrets


def to_nums(text):
    return [ord(c) - 65 for c in text.upper() if c.isalpha()]


def to_text(nums):
    return "".join(chr(n % 26 + 65) for n in nums)


plaintext = input("Enter the plaintext: ")
choice = input("Enter the key stream (or type RANDOM): ")
p = to_nums(plaintext)
if choice.strip().upper() == "RANDOM":
    key = [secrets.randbelow(26) for _ in p]
else:
    key = [int(v) % 26 for v in choice.split()]
if len(key) < len(p):
    raise SystemExit("The key stream is shorter than the plaintext")
c = [(a + k) % 26 for a, k in zip(p, key)]
print("Plaintext  :", to_text(p))
print("Key stream :", " ".join(map(str, key[:len(p)])))
print("Ciphertext :", to_text(c))
d = [(a - k) % 26 for a, k in zip(c, key)]
print("Decrypted  :", to_text(d))
