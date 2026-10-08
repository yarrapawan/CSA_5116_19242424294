import hashlib
import random

P = 4611686149423890371
Q = 2147483647
G = 2719173151515238304


def h(message):
    return int.from_bytes(hashlib.sha256(message.encode()).digest(),
                          "big") % Q


def dsa_sign(message, x, k):
    r = pow(G, k, P) % Q
    s = pow(k, -1, Q) * (h(message) + x * r) % Q
    return r, s


def dsa_verify(message, sig, y):
    r, s = sig
    w = pow(s, -1, Q)
    v = pow(G, h(message) * w % Q, P) * pow(y, r * w % Q, P) % P % Q
    return v == r


def fresh_signature(message, x):
    while True:
        k = random.randrange(2, Q)
        r, s = dsa_sign(message, x, k)
        if r and s:
            return (r, s), k


message = input("Enter the message: ")
x = int(input("Enter the DSA private key x: "))
y = pow(G, x, P)
sig1, k1 = fresh_signature(message, x)
sig2, k2 = fresh_signature(message, x)
print("DSA  signature 1:", sig1, "valid:", dsa_verify(message, sig1, y))
print("DSA  signature 2:", sig2, "valid:", dsa_verify(message, sig2, y))
print("DSA signatures of the same message are equal:", sig1 == sig2)
rp, rq, re = 104729, 1299709, 65537
rn = rp * rq
rd = pow(re, -1, (rp - 1) * (rq - 1))
hm = int.from_bytes(hashlib.sha256(message.encode()).digest(), "big") % rn
rsa1, rsa2 = pow(hm, rd, rn), pow(hm, rd, rn)
print("RSA  signature 1:", rsa1, " signature 2:", rsa2)
print("RSA signatures of the same message are equal:", rsa1 == rsa2)
print("Implication: a DSA signature is randomised, so it cannot be used to")
print("tell whether two messages are the same, but k must never be reused:")
second = message + " (second message)"
k = random.randrange(2, Q)
r, s1 = dsa_sign(message, x, k)
_, s2 = dsa_sign(second, x, k)
k_found = (h(message) - h(second)) * pow(s1 - s2, -1, Q) % Q
x_found = (s1 * k_found - h(message)) * pow(r, -1, Q) % Q
print("   Two signatures made with the same k reveal k =", k_found == k)
print("   and the private key x =", x_found == x)
