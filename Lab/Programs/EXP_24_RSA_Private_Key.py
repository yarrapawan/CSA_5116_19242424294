def extended_gcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


e = int(input("Enter the public exponent e: "))
n = int(input("Enter the modulus n: "))
p = next(i for i in range(2, n) if n % i == 0)
q = n // p
phi = (p - 1) * (q - 1)
print("Trial and error gives p = %d and q = %d" % (p, q))
print("phi(n) = (p - 1)(q - 1) = %d" % phi)
g, x, y = extended_gcd(e, phi)
print("Extended Euclid: %d x (%d) + %d x (%d) = %d" % (e, x, phi, y, g))
d = x % phi
print("Private key d = %d" % d)
print("Check: e x d mod phi(n) =", (e * d) % phi)
m = 1234 % n
c = pow(m, e, n)
print("Test: m = %d, c = %d, decrypted = %d" % (m, c, pow(c, d, n)))
