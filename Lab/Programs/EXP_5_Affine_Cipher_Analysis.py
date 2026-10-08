from math import gcd


def is_one_to_one(a, b):
    return len({(a * p + b) % 26 for p in range(26)}) == 26


print("(a) Is there any limitation on b?")
valid_a = [a for a in range(26) if gcd(a, 26) == 1]
ok = all(is_one_to_one(a, b) for a in valid_a for b in range(26))
print("    Every b from 0 to 25 works for every valid a:", ok)
print("    So b has no limitation (it only shifts the result).")
print("(b) Values of a that are not allowed")
allowed = [a for a in range(26) if is_one_to_one(a, 0)]
not_allowed = [a for a in range(26) if a not in allowed]
print("    Allowed values     :", allowed)
print("    Not allowed values :", not_allowed)
print("    Rule: a is allowed only when gcd(a, 26) = 1")
a = int(input("Enter a to test: "))
b = int(input("Enter b to test: "))
print("Testing E(p) = (%d p + %d) mod 26 :" % (a, b), "gcd(a, 26) =", gcd(a, 26))
seen = {}
for p in range(26):
    c = (a * p + b) % 26
    if c in seen:
        print("Not one-to-one: E(%d) = E(%d) = %d" % (seen[c], p, c))
        break
    seen[c] = p
else:
    print("The cipher is one-to-one for these values of a and b")
