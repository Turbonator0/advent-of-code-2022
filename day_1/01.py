elves = {"1" : 0}

elfIndex = 1
with open("input") as f:
    for line in f:
        if line == "\n":
            elfIndex += 1
            elves[str(elfIndex)] = 0
        else: 
            print(line, end='')
            elves[str(elfIndex)] += int(line)
largest = (1,0)
for k,v in zip(elves.keys(), elves.values()):
    if v > largest[1]:
        largest = (k,v)
    print(k,v)
print(largest)