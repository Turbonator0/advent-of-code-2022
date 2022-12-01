elves = []

total = 0
elfIndex = 0
with open("input") as f:
    for line in f:
        if line == "\n":
            elfIndex += 1
            elves.append((elfIndex, total))
            total = 0
        else: 

            print(line, end='')
            total += int(line)

elves.sort(key = lambda elves: elves[1],reverse=True)
elfTotal = 0
for elf in elves[:3]:
    elfTotal += elf[1]
print(elfTotal)
