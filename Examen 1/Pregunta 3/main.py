import vectores

vector1 = vectores.Vector(1, 1, 1)

vector2 = vectores.Vector(1, 1, 1)

print(f"vector1 = {vector1}")
print(f"vector2 = {vector2}")

print(f"vector1 + vector2 = {vector1 + vector2}")
print(f"vector1 - vector2 = {vector1 - vector2}")
print(f"vector1 * vector2 = {vector1 * vector2}")
print(f"vector1 % vector2 = {vector1 % vector2}")

print(f"vector1 + 7 = {vector1 + 7}")
print(f"vector1 - 7 = {vector1 - 7}")
print(f"vector1 * 7 = {vector1 * 7}")

print("\n")

a = vectores.Vector(0, 0, 0)
b = vectores.Vector(1, 1, 1)
c = vectores.Vector(2, 2, 2)

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print(f"b + c = {b + c}")
print(f"a * b + c = {a * b + c}")
print(f"(b + b) * (c - a) = {(b + b) * (c - a)}")
print(f"a % (c * b) = {a % (c * b)}")

print(f"b + 3 = {b + 3}")
print(f"a * 3.0 + 7.0 = {a * 3.0 + 7.0}")
print(f"(b + b) * (c - a) = {(b + b) * (c - a)}")