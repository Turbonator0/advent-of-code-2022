total = 0
with open("input") as f:
    for line in f.readlines():
        values = line.split(",")
        pair1 = values[0].split("-")
        pair2 = values[1].split("-")
        pair2[1] = pair2[1].strip("\n")
        pair1[1] = pair1[1].strip("\n")
        
        
        # if pair1.max is larger than or eq to pair2.min
        # 1 2 3 4 5 6
        #       4 5 6 7 8 9
        #
        #       4 5 6 7 8 9
        # 1 2 3 4 5 6
        if (int(pair1[1]) >= int(pair2[0]) or int(pair1[0]) >= int(pair2[1])) and int(pair2[1]) >= int(pair1[0]):
            print(pair1,pair2)
            total += 1
        
print(total)