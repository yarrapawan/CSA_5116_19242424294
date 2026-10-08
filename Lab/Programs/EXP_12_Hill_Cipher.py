def to_pairs(text):
    nums = [ord(c) - 97 for c in text.lower() if c.isalpha()]
    if len(nums) % 2:
        nums.append(23)
    return [nums[i:i + 2] for i in range(0, len(nums), 2)]


def letter(n):
    return chr(n + 97).upper()


def show(blocks, k, title):
    out = []
    print(title)
    for p1, p2 in blocks:
        c1 = (k[0][0] * p1 + k[0][1] * p2) % 26
        c2 = (k[1][0] * p1 + k[1][1] * p2) % 26
        print("  [%2d %2d] -> (%d*%d + %d*%d) mod 26 = %2d ,"
              " (%d*%d + %d*%d) mod 26 = %2d  =>  %s%s"
              % (p1, p2, k[0][0], p1, k[0][1], p2, c1,
                 k[1][0], p1, k[1][1], p2, c2, letter(c1), letter(c2)))
        out.append([c1, c2])
    return out


row1 = list(map(int, input("Enter key row 1: ").split()))
row2 = list(map(int, input("Enter key row 2: ").split()))
plaintext = input("Enter the plaintext: ")
key = [row1, row2]
det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
print("Determinant mod 26 =", det)
try:
    det_inv = pow(det, -1, 26)
except ValueError:
    raise SystemExit("The key matrix is not invertible mod 26")
blocks = to_pairs(plaintext)
print("Plaintext blocks:", " ".join(letter(a) + letter(b) for a, b in blocks))
cipher = show(blocks, key, "(a) Encryption  C = K P mod 26")
print("Ciphertext:", "".join(letter(a) + letter(b) for a, b in cipher))
inverse = [[det_inv * key[1][1] % 26, -det_inv * key[0][1] % 26],
           [-det_inv * key[1][0] % 26, det_inv * key[0][0] % 26]]
print("Inverse key matrix K^-1 =", inverse, "(determinant inverse =", det_inv, ")")
plain = show(cipher, inverse, "(b) Decryption  P = K^-1 C mod 26")
print("Recovered plaintext:", "".join(letter(a) + letter(b) for a, b in plain))
