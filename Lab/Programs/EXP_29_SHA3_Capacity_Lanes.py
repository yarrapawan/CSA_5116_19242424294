import hashlib
import random


MASK = (1 << 64) - 1
RC = [0x0000000000000001, 0x0000000000008082, 0x800000000000808A,
      0x8000000080008000, 0x000000000000808B, 0x0000000080000001,
      0x8000000080008081, 0x8000000000008009, 0x000000000000008A,
      0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
      0x000000008000808B, 0x800000000000008B, 0x8000000000008089,
      0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
      0x000000000000800A, 0x800000008000000A, 0x8000000080008081,
      0x8000000000008080, 0x0000000080000001, 0x8000000080008008]
ROT = [[0, 36, 3, 41, 18], [1, 44, 10, 45, 2], [62, 6, 43, 15, 61],
       [28, 55, 25, 21, 56], [27, 20, 39, 8, 14]]


def rol(v, n):
    n %= 64
    return ((v << n) | (v >> (64 - n))) & MASK if n else v


def theta(a):
    c = [a[x][0] ^ a[x][1] ^ a[x][2] ^ a[x][3] ^ a[x][4] for x in range(5)]
    d = [c[(x - 1) % 5] ^ rol(c[(x + 1) % 5], 1) for x in range(5)]
    return [[a[x][y] ^ d[x] for y in range(5)] for x in range(5)]


def rho_pi(a):
    b = [[0] * 5 for _ in range(5)]
    for x in range(5):
        for y in range(5):
            b[y][(2 * x + 3 * y) % 5] = rol(a[x][y], ROT[x][y])
    return b


def chi(a):
    return [[a[x][y] ^ ((~a[(x + 1) % 5][y]) & a[(x + 2) % 5][y] & MASK)
             for y in range(5)] for x in range(5)]


def iota(a, rnd):
    a[0][0] ^= RC[rnd]
    return a


def keccak_f(a):
    for rnd in range(24):
        a = iota(chi(rho_pi(theta(a))), rnd)
    return a


def sha3(msg, rate_bytes, out_len):
    a = [[0] * 5 for _ in range(5)]
    msg = bytearray(msg)
    msg.append(0x06)
    while len(msg) % rate_bytes:
        msg.append(0)
    msg[-1] |= 0x80
    for off in range(0, len(msg), rate_bytes):
        for i in range(rate_bytes // 8):
            lane = int.from_bytes(msg[off + 8 * i:off + 8 * i + 8], "little")
            a[i % 5][i // 5] ^= lane
        a = keccak_f(a)
    out = b"".join(a[i % 5][i // 5].to_bytes(8, "little")
                   for i in range(rate_bytes // 8))
    return out[:out_len]
rate = int(input("Enter the block size r in bits: "))
rate_lanes = rate // 64
capacity_bits = 1600 - rate
print("Capacity c = 1600 - %d = %d bits = %d lanes"
      % (rate, capacity_bits, 25 - rate_lanes))
print("Check Keccak against hashlib:",
      sha3(b"abc", 136, 32) == hashlib.sha3_256(b"abc").digest())
state = [[0] * 5 for _ in range(5)]
for i in range(rate_lanes):
    state[i % 5][i // 5] = random.getrandbits(64) | 1
tracked = [(i % 5, i // 5) for i in range(rate_lanes, 25)]


def zero_lanes(s):
    return sum(1 for x, y in tracked if s[x][y] == 0)


print("Before round 1: zero capacity lanes =", zero_lanes(state))
rnd = 0
while zero_lanes(state) and rnd < 24:
    state = theta(state)
    print("Round %d after theta : zero capacity lanes = %d"
          % (rnd + 1, zero_lanes(state)))
    state = rho_pi(state)
    tracked = [(y, (2 * x + 3 * y) % 5) for x, y in tracked]
    print("Round %d after pi    : zero capacity lanes = %d"
          % (rnd + 1, zero_lanes(state)))
    state = iota(chi(state), rnd)
    print("Round %d after chi   : zero capacity lanes = %d"
          % (rnd + 1, zero_lanes(state)))
    rnd += 1
print("All capacity lanes contain a nonzero bit after %d round(s)." % rnd)
