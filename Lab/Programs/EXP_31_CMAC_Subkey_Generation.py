IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,
     24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
SBOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]


def permute(bits, table):
    return [bits[i - 1] for i in table]


def hex_to_bits(h):
    return [int(b) for b in bin(int(h, 16))[2:].zfill(len(h) * 4)]


def bits_to_hex(bits):
    return hex(int("".join(map(str, bits)), 2))[2:].zfill(len(bits) // 4).upper()


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]


def generate_subkeys(key_hex):
    cd = permute(hex_to_bits(key_hex), PC1)
    c, d = cd[:28], cd[28:]
    keys = []
    for s in SHIFTS:
        c, d = c[s:] + c[:s], d[s:] + d[:s]
        keys.append(permute(c + d, PC2))
    return keys


def feistel(r, k):
    x = xor(permute(r, E), k)
    out = []
    for i in range(8):
        b = x[6 * i:6 * i + 6]
        row = b[0] * 2 + b[5]
        col = b[1] * 8 + b[2] * 4 + b[3] * 2 + b[4]
        out += [int(c) for c in bin(SBOX[i][row][col])[2:].zfill(4)]
    return permute(out, P)


def des_block(block_hex, subkeys):
    bits = permute(hex_to_bits(block_hex), IP)
    l, r = bits[:32], bits[32:]
    for k in subkeys:
        l, r = r, xor(l, feistel(r, k))
    return bits_to_hex(permute(r + l, FP))


def des_encrypt(block_hex, key_hex):
    return des_block(block_hex, generate_subkeys(key_hex))


def des_decrypt(block_hex, key_hex):
    return des_block(block_hex, generate_subkeys(key_hex)[::-1])

def build_sbox():
    sb = [0] * 256
    p = q = 1
    while True:
        p = p ^ ((p << 1) & 0xFF) ^ (0x1B if p & 0x80 else 0)
        q ^= (q << 1) & 0xFF
        q ^= (q << 2) & 0xFF
        q ^= (q << 4) & 0xFF
        if q & 0x80:
            q ^= 0x09
        rot = lambda v, n: ((v << n) | (v >> (8 - n))) & 0xFF
        sb[p] = q ^ rot(q, 1) ^ rot(q, 2) ^ rot(q, 3) ^ rot(q, 4) ^ 0x63
        if p == 1:
            break
    sb[0] = 0x63
    return sb


SB = build_sbox()


def xtime(a):
    return ((a << 1) ^ 0x1B) & 0xFF if a & 0x80 else a << 1


def expand_key(key):
    w = [list(key[4 * i:4 * i + 4]) for i in range(4)]
    rcon = 1
    for i in range(4, 44):
        t = w[i - 1][:]
        if i % 4 == 0:
            t = t[1:] + t[:1]
            t = [SB[b] for b in t]
            t[0] ^= rcon
            rcon = xtime(rcon)
        w.append([a ^ b for a, b in zip(w[i - 4], t)])
    return [sum(w[4 * r:4 * r + 4], []) for r in range(11)]


def aes_encrypt(block, key):
    rk = expand_key(key)
    s = [b ^ k for b, k in zip(block, rk[0])]
    for rnd in range(1, 11):
        s = [SB[b] for b in s]
        s = [s[(i + 4 * (i % 4)) % 16] for i in range(16)]
        if rnd != 10:
            for c in range(4):
                a = s[4 * c:4 * c + 4]
                t = a[0] ^ a[1] ^ a[2] ^ a[3]
                s[4 * c + 0] = a[0] ^ t ^ xtime(a[0] ^ a[1])
                s[4 * c + 1] = a[1] ^ t ^ xtime(a[1] ^ a[2])
                s[4 * c + 2] = a[2] ^ t ^ xtime(a[2] ^ a[3])
                s[4 * c + 3] = a[3] ^ t ^ xtime(a[3] ^ a[0])
        s = [b ^ k for b, k in zip(s, rk[rnd])]
    return bytes(s)
CONSTANTS = {64: (0x1B, "x^64 + x^4 + x^3 + x + 1"),
             128: (0x87, "x^128 + x^7 + x^2 + x + 1")}


def double(value, bits, rb):
    msb = (value >> (bits - 1)) & 1
    value = (value << 1) & ((1 << bits) - 1)
    return value ^ rb if msb else value


des_key = input("Enter a 64-bit DES key (16 hex digits): ").upper()
aes_key = input("Enter a 128-bit AES key (32 hex digits): ")
print("(a) Constants Rb for the subkey generation")
for bits, (rb, poly) in CONSTANTS.items():
    print("    block size %3d : Rb = 0x%0*X   polynomial %s"
          % (bits, bits // 4, rb, poly))
l64 = int(des_encrypt("0" * 16, des_key), 16)
l128 = int.from_bytes(aes_encrypt(bytes(16), bytes.fromhex(aes_key)), "big")
for bits, l in ((64, l64), (128, l128)):
    rb = CONSTANTS[bits][0]
    k1 = double(l, bits, rb)
    k2 = double(k1, bits, rb)
    print("(b) %d bit block cipher" % bits)
    print("    L  = E(K, 0^%d) = %0*X" % (bits, bits // 4, l))
    print("    K1 = %0*X   (MSB of L = %d)" % (bits // 4, k1, l >> (bits - 1)))
    print("    K2 = %0*X   (MSB of K1 = %d)" % (bits // 4, k2, k1 >> (bits - 1)))
print("Left shift = multiplication by x; XOR with Rb performs the reduction")
print("modulo the irreducible polynomial whenever the MSB was 1.")
