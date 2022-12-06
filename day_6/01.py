fuckyou = 0
fuckyou2 = 0
import os
with open("input") as f:
    content = f.read()
    #print(content[4:])
    for i in range(4,len(content)-1,1):
            fuckyou = 0
            fuckyou2 += 1
            for char in content[i-4:i]:
                if content[i-4:i].count(char) > 1:
                    break
                else:
                    fuckyou += 1
                if fuckyou == 4: 
                    print(fuckyou2 +3)
                    os.exit()
