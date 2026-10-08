from math import gcd


def factor_from_keys(n, e, d):
    k = e * d - 1
    t, r = 0, k
    while r % 2 == 0:
        r //= 2
        t += 1
    for g in range(2, n - 1):
        if gcd(g, n) > 1:
            return gcd(g, n)
        x = pow(g, r, n)
        if x in (1, n - 1):
            continue
        for _ in range(t):
            y = pow(x, 2, n)
            if y == 1:
                p = gcd(x - 1, n)
                if 1 < p < n:
                    return p
                break
            if y == n - 1:
                break
            x = y


n = int(input("Enter the common modulus n: "))
e = int(input("Enter Bob's old public exponent e: "))
d = int(input("Enter Bob's leaked private exponent d: "))
e_new = int(input("Enter Bob's new public exponent e': "))
p = factor_from_keys(n, e, d)
q = n // p
phi = (p - 1) * (q - 1)
print("Attacker factors n using (e, d): p = %d, q = %d" % (p, q))
print("phi(n) = %d" % phi)
if gcd(e_new, phi) != 1:
    raise SystemExit("e' is not valid for this modulus")
d_new = pow(e_new, -1, phi)
print("Bob's new public key  : (e', n) = (%d, %d)" % (e_new, n))
print("Attacker computes d'  :", d_new)
m = 1234 % n
print("Test: encrypt %d with e', attacker decrypts ->" % m,
      pow(pow(m, e_new, n), d_new, n))
print("Conclusion: keeping the same n is NOT safe; a new n must be chosen.")
