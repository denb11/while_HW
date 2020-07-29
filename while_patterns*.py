# counter




n = int(input("intoduceti numarul de rinduri: "))
x = 1
while x <= n:
    y = 1
    while y <= x:
        print("*", end=" ")
        y += 1

    print()
    x += 1
