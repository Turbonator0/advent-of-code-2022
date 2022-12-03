import string


char_array = [  "a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z","A","B","C","D","E","F","G",
                "H","I","J","K","L","M","N","O","P","Q","R",
                "S","T","U","V","W","X","Y","Z"]

total = 0
with open("input") as f:
    chars = string.ascii_letters
    for line in f.readlines():
        first = line[:int(len(line)/2)]
        second = line[(int(len(line)/2)):]
        for char in chars:
            if char in first and char in second:
                for i in range(len(chars)):
                    if char_array[i] == char:
                        print(i)
                        total += i+1


print(total)