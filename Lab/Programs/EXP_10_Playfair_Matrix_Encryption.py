def build_matrix(keyword):
    letters = []
    for ch in (keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper():
        ch = "I" if ch == "J" else ch
        if ch.isalpha() and ch not in letters:
            letters.append(ch)
    return [letters[i:i + 5] for i in range(0, 25, 5)]


def position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def make_pairs(text):
    text = [("I" if c == "J" else c) for c in text.upper() if c.isalpha()]
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else ""
        filler = "X" if a != "X" else "Q"
        if b == "" or a == b:
            pairs.append(a + filler)
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs


def crypt_pair(matrix, pair, step):
    r1, c1 = position(matrix, pair[0])
    r2, c2 = position(matrix, pair[1])
    if r1 == r2:
        return matrix[r1][(c1 + step) % 5] + matrix[r2][(c2 + step) % 5]
    if c1 == c2:
        return matrix[(r1 + step) % 5][c1] + matrix[(r2 + step) % 5][c2]
    return matrix[r1][c2] + matrix[r2][c1]


def show_matrix(matrix):
    for row in matrix:
        print("   ", " ".join(row))
matrix = []
for i in range(1, 6):
    row = input("Enter row %d of the matrix: " % i).upper().replace("J", "I")
    matrix.append(list(row))
message = input("Enter the message: ")
flat = sum(matrix, [])
if len(flat) == 25 and len(set(flat)) == 25:
    print("Playfair matrix:")
    show_matrix(matrix)
    pairs = make_pairs(message)
    cipher_pairs = [crypt_pair(matrix, p, 1) for p in pairs]
    print("Digraphs   :", " ".join(pairs))
    print("Ciphertext :", " ".join(cipher_pairs))
else:
    print("The matrix must contain 25 different letters")
