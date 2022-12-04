total = 0
with open("input") as f:
    for line in f.readlines():
        values = line.split(",")
        pair1 = values[0].split("-")
        pair2 = values[1].split("-")
        pair2[1] = pair2[1].strip("\n")
        pair1[1] = pair1[1].strip("\n")
        # if pair1.min is larger than pair2.min and pair2.max <= pair1.max
        if int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]):
            print(pair1,pair2)
            total += 1
        elif int(pair2[0]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1]):
            print(pair1,pair2)
            total += 1
print(total)