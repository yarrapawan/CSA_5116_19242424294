from itertools import combinations
from math import gcd


def minor(m, i, j):
    return [row[:j] + row[j + 1:] for k, row in enumerate(m) if k != i]


def det(m):
    if len(m) == 1:
        return m[0][0]
    return sum((-1) ** j * m[0][j] * det(minor(m, 0, j)) for j in range(len(m)))


def inverse_mod(m, mod=26):
    n = len(m)
    d = det(m) % mod
    if gcd(d, mod) != 1:
        return None
    d_inv = pow(d, -1, mod)
    if n == 1:
        return [[d_inv]]
    return [[(d_inv * (-1) ** (i + j) * det(minor(m, j, i))) % mod
             for j in range(n)] for i in range(n)]


def multiply(a, b, mod=26):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % mod
             for j in range(len(b[0]))] for i in range(len(a))]


def to_blocks(text, n):
    nums = [ord(c) - 65 for c in text]
    return [nums[i:i + n] for i in range(0, len(nums), n)]


def encrypt(text, key):
    out = ""
    for block in to_blocks(text, len(key)):
        col = multiply(key, [[x] for x in block])
        out += "".join(chr(v[0] + 65) for v in col)
    return out


n = int(input("Enter the matrix size n: "))
plain = "".join(c for c in input("Enter the known plaintext: ").upper()
                if c.isalpha())
cipher = "".join(c for c in input("Enter the matching ciphertext: ").upper()
                 if c.isalpha())
pb, cb = to_blocks(plain, n), to_blocks(cipher, n)
print("Known plaintext blocks :", pb)
print("Known ciphertext blocks:", cb)
key = None
for idx in combinations(range(len(pb)), n):
    P = [[pb[j][i] for j in idx] for i in range(n)]
    C = [[cb[j][i] for j in idx] for i in range(n)]
    p_inv = inverse_mod(P)
    if p_inv is None:
        continue
    candidate = multiply(C, p_inv)
    if encrypt(plain, candidate) == cipher:
        key = candidate
        print("Blocks used for the attack:", [i + 1 for i in idx])
        break
if key is None:
    print("Attack failed: supply more independent plaintext blocks")
else:
    print("K = C x P^-1 (mod 26) =")
    for row in key:
        print("   ", row)
    print("Key as letters:", "".join(chr(v + 65) for r in key for v in r))
    print("Chosen plaintext attack (unit vectors give the columns of K):")
    for i in range(n):
        chosen = "".join("B" if j == i else "A" for j in range(n))
        print("   plaintext %s -> ciphertext %s" % (chosen, encrypt(chosen, key)))
