
rows = int(input("Enter the number of rows: "))

i = 1

while i <= rows:
    spaces = rows - i
    while spaces > 0:
        print(" ", end="")
        spaces = spaces - 1

    stars = 1
    while stars <= i:
        print("*", end="")
        stars = stars + 1

    print()
    i = i + 1
