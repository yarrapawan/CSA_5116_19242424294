from math import gcd

p = int(input("Enter Bob's prime p: "))
q = int(input("Enter Bob's prime q: "))
e = int(input("Enter Bob's public exponent e: "))
message = input("Enter Alice's message (A-Z): ").upper().replace(" ", "")
n, phi = p * q, (p - 1) * (q - 1)
if gcd(e, phi) != 1:
    raise SystemExit("e must be coprime with phi(n)")
d = pow(e, -1, phi)
numbers = [ord(ch) - 65 for ch in message]
cipher = [pow(m, e, n) for m in numbers]
print("Alice sends (each letter encrypted separately):")
print("   ", cipher)
table = {pow(m, e, n): chr(m + 65) for m in range(26)}
print("Eve encrypts all 26 possible letters with the public key (e, n)")
print("and builds a lookup table:")
print("   ", " ".join("%s=%d" % (table[c], c) for c in sorted(table,
                                                                key=table.get)))
cracked = "".join(table[c] for c in cipher)
print("Eve recovers the message without d:", cracked)
print("Bob decrypts normally           :",
      "".join(chr(pow(c, d, n) + 65) for c in cipher))
print("The method is insecure: only 26 plaintexts exist, so a table lookup")
print("(or frequency analysis) breaks it, however large n is.")
