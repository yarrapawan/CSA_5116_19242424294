from math import gcd

q = int(input("Enter the prime q: "))
alpha = int(input("Enter the generator alpha: "))
a = int(input("Enter the public number a for the x^a scheme: "))
xa = int(input("Enter Alice's secret x_A: "))
xb = int(input("Enter Bob's secret x_B: "))
print("Standard Diffie-Hellman (send alpha^x mod q)")
ya, yb = pow(alpha, xa, q), pow(alpha, xb, q)
print("   Alice sends %d, Bob sends %d" % (ya, yb))
print("   Alice key = %d, Bob key = %d" % (pow(yb, xa, q), pow(ya, xb, q)))
print("Modified scheme (send x^a mod q)")
xa_pub, xb_pub = pow(xa, a, q), pow(xb, a, q)
print("   Alice sends %d, Bob sends %d" % (xa_pub, xb_pub))
if gcd(a, q - 1) != 1:
    raise SystemExit("a must be coprime with q - 1 for this demonstration")
a_inv = pow(a, -1, q - 1)
print("   a^-1 mod (q - 1) =", a_inv)
bob_found = pow(xb_pub, a_inv, q)
alice_found = pow(xa_pub, a_inv, q)
print("   Alice recovers x_B =", bob_found, " and Bob recovers x_A =",
      alice_found)
print("   Common key K = x_A * x_B mod q:", xa * bob_found % q,
      "=", xb * alice_found % q)
print("Eve sees only the two public values, but she can do the same:")
print("   Eve finds x_A =", pow(xa_pub, a_inv, q), ", x_B =",
      pow(xb_pub, a_inv, q))
print("   Eve's key =", pow(xa_pub, a_inv, q) * pow(xb_pub, a_inv, q) % q)
print("So the scheme is broken: x is easy to find from x^a mod q.")
