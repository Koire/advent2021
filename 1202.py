from dayone import calculate
entries = []
with open("1201.txt") as f:
    for line in f:
        entries.append(int(line))
windows = [sum(entries[i:i+3]) for i in range(0, len(entries)) if len(entries[i:i+3]) == 3]
print(calculate(windows))