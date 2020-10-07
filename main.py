list_1 = []

for i in range(10):
    if i % 2 == 0:
        list_1.append(1)

list_2 = [i for i in range(10) if i % 2 == 0]

print(list_1, list_2)

for i in range(1, 11):
    print("=" * (11 - i), "*" * (i * 2 - 1), "=" * (11 - i))

is_upset = False
sweet = 0

while not is_upset:
    sweet = sweet + 1
    print("still not good")
    if sweet == 10:
        is_upset = True
        print("good")
