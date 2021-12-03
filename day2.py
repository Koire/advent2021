with open("day2.txt") as f:
    horizontal = 0
    depth = 0
    dirs = [
        l.split(" ") for l in f.read().splitlines()
    ]
    for [command, amount] in dirs:
        if command == "forward":
            horizontal += int(amount)
        if command == "up":
            depth -= int(amount)
        if command == "down":
            depth += int(amount)
    print((horizontal) *(depth))