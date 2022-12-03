import string


char_array = [  "a","b","c","d","e","f","g","h","i","j","k",
                "l","m","n","o","p","q","r","s","t","u","v",
                "w","x","y","z","A","B","C","D","E","F","G",
                "H","I","J","K","L","M","N","O","P","Q","R",
                "S","T","U","V","W","X","Y","Z"]

total = 0
with open("input") as f:
    chars = string.ascii_letters
    content = f.readlines()
    for line in range(0, len(content), 3):
        for char in range(len(char_array)):
            if char_array[char] in content[line] and char_array[char] in content[line+1] and char_array[char] in content[line+2]:
                total += char +1
                print(char)        
            
print(total)