def calculate(lines):
    prev_line = 0
    increased = -1
    for line in lines:
        if int(line) > prev_line:
            increased += 1
        prev_line = int(line)
    return increased

with open("1201.txt") as f:
    print(calculate(f.readlines()))