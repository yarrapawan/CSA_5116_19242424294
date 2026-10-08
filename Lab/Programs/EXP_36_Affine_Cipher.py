from math import gcd

a = int(input("Enter the multiplier a: "))
b = int(input("Enter the shift b: "))
text = input("Enter the plaintext: ").upper()
print("a = 2, b = 3 is not one-to-one: E(0) = %d and E(13) = %d"
      % ((2 * 0 + 3) % 26, (2 * 13 + 3) % 26))
if gcd(a, 26) != 1:
    print("a = %d is not allowed because gcd(a, 26) = %d" % (a, gcd(a, 26)))
    seen = {}
    for p in range(26):
        c = (a * p + b) % 26
        if c in seen:
            print("E(%d) = E(%d) = %d, so decryption is impossible"
                  % (seen[c], p, c))
            break
        seen[c] = p
else:
    a_inv = pow(a, -1, 26)
    print("a = %d is valid, a^-1 mod 26 = %d" % (a, a_inv))
    cipher = "".join(chr((a * (ord(c) - 65) + b) % 26 + 65) if c.isalpha()
                     else c for c in text)
    print("Ciphertext :", cipher)
    plain = "".join(chr(a_inv * (ord(c) - 65 - b) % 26 + 65) if c.isalpha()
                    else c for c in cipher)
    print("Decrypted  :", plain)
