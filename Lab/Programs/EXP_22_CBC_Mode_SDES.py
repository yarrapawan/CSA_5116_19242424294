P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP8 = [2, 6, 3, 1, 4, 8, 5, 7]
IP8_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]


def perm(bits, table):
    return [bits[i - 1] for i in table]


def to_bits(s):
    return [int(c) for c in s.replace(" ", "")]


def to_str(bits):
    return "".join(str(b) for b in bits)


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def sdes_keys(key):
    k = perm(key, P10)
    l, r = k[:5], k[5:]
    l, r = l[1:] + l[:1], r[1:] + r[:1]
    k1 = perm(l + r, P8)
    l, r = l[2:] + l[:2], r[2:] + r[:2]
    k2 = perm(l + r, P8)
    return k1, k2


def sbox(bits, box):
    row = bits[0] * 2 + bits[3]
    col = bits[1] * 2 + bits[2]
    v = box[row][col]
    return [v >> 1, v & 1]


def fk(bits, k):
    l, r = bits[:4], bits[4:]
    t = xor(perm(r, EP), k)
    t = sbox(t[:4], S0) + sbox(t[4:], S1)
    return xor(l, perm(t, P4)) + r


def sdes_encrypt(block, key):
    k1, k2 = sdes_keys(key)
    b = perm(block, IP8)
    b = fk(b, k1)
    b = b[4:] + b[:4]
    b = fk(b, k2)
    return perm(b, IP8_INV)


def sdes_decrypt(block, key):
    k1, k2 = sdes_keys(key)
    b = perm(block, IP8)
    b = fk(b, k2)
    b = b[4:] + b[:4]
    b = fk(b, k1)
    return perm(b, IP8_INV)
key = to_bits(input("Enter the 10-bit key: "))
iv = to_bits(input("Enter the 8-bit initialization vector: "))
plaintext = to_bits(input("Enter the binary plaintext (multiple of 8 bits): "))
if len(key) != 10 or len(iv) != 8 or len(plaintext) % 8:
    raise SystemExit("Invalid key, IV or plaintext length")
cipher, prev = [], iv
for i in range(0, len(plaintext), 8):
    block = plaintext[i:i + 8]
    prev = sdes_encrypt(xor(block, prev), key)
    cipher += prev
print("CBC ciphertext :", " ".join(to_str(cipher[i:i + 4])
                                   for i in range(0, len(cipher), 4)))
decrypted, prev = [], iv
for i in range(0, len(cipher), 8):
    block = cipher[i:i + 8]
    decrypted += xor(sdes_decrypt(block, key), prev)
    prev = block
print("CBC decryption :", " ".join(to_str(decrypted[i:i + 4])
                                   for i in range(0, len(decrypted), 4)))
