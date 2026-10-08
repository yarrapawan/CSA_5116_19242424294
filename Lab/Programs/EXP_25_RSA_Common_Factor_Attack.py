from math import gcd

n = int(input("Enter the modulus n: "))
e = int(input("Enter the public exponent e: "))
blocks = list(map(int, input("Enter the ciphertext blocks: ").split()))
print("Computing gcd(c, n) for every ciphertext block")
p = None
for c in blocks:
    g = gcd(c, n)
    print("   gcd(%d, %d) = %d" % (c, n, g))
    if 1 < g < n and p is None:
        p = g
if p is None:
    print("No block shares a factor with n")
else:
    q = n // p
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    print("n is factored: p = %d, q = %d, so phi(n) = %d" % (p, q, phi))
    print("Private key d = %d" % d)
    print("Recovered plaintext blocks:", [pow(c, d, n) for c in blocks])
