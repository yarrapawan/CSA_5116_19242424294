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
keyword = input("Enter the keyword: ")
plaintext = input("Enter the plaintext: ")
matrix = build_matrix(keyword)
print("5 x 5 key matrix (I and J share a cell):")
show_matrix(matrix)
pairs = make_pairs(plaintext)
print("Plaintext digraphs :", " ".join(pairs))
cipher_pairs = [crypt_pair(matrix, p, 1) for p in pairs]
print("Ciphertext         :", " ".join(cipher_pairs))
decrypted = [crypt_pair(matrix, p, -1) for p in cipher_pairs]
print("Decrypted digraphs :", " ".join(decrypted))
