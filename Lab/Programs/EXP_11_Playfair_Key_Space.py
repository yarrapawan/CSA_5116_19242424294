import math

LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def build_matrix(keyword):
    seq = ""
    for ch in keyword.upper().replace("J", "I") + LETTERS:
        if ch in LETTERS and ch not in seq:
            seq += ch
    return [list(seq[i:i + 5]) for i in range(0, 25, 5)]


def encrypt_pair(m, a, b):
    pos = {m[r][c]: (r, c) for r in range(5) for c in range(5)}
    (r1, c1), (r2, c2) = pos[a], pos[b]
    if r1 == r2:
        return m[r1][(c1 + 1) % 5] + m[r2][(c2 + 1) % 5]
    if c1 == c2:
        return m[(r1 + 1) % 5][c1] + m[(r2 + 1) % 5][c2]
    return m[r1][c2] + m[r2][c1]


def cipher_table(m):
    return tuple(encrypt_pair(m, a, b) for a in LETTERS for b in LETTERS
                 if a != b)


def variants(m):
    result = []
    for flip in (False, True):
        base = [list(r) for r in zip(*m)] if flip else m
        for rs in range(5):
            shifted = base[rs:] + base[:rs]
            for cs in range(5):
                result.append([row[cs:] + row[:cs] for row in shifted])
    return result


keyword = input("Enter a keyword to build a sample key matrix: ")
total = math.factorial(25)
print("(a) Number of possible keys = 25! = %d" % total)
print("    25! is about 2^%.2f, i.e. approximately 2^84" % math.log2(total))
matrix = build_matrix(keyword)
original = cipher_table(matrix)
same = [v for v in variants(matrix) if cipher_table(v) == original]
unique = {tuple(map(tuple, v)) for v in same}
print("(b) Matrices tested (row shifts, column shifts, transpose) :",
      len(variants(matrix)))
print("    Matrices giving exactly the same encryption             :",
      len(unique))
effective = total // len(unique)
print("    Effectively unique keys = 25!/%d = %d" % (len(unique), effective))
print("    which is about 2^%.2f" % math.log2(effective))
