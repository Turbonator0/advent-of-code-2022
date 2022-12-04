import string

total = 0
with open("input") as f:
    chars = string.ascii_letters
    for line in f.readlines():
        first = line[:int(len(line)/2)]
        second = line[(int(len(line)/2)):]
        for char in chars:
            if char in first and char in second:
                if char.islower():
                    i = ord(char) - 96
                else: i = ord(char) - 38

                total += i
                    
print(total)