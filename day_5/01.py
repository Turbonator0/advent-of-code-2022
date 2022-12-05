import re, collections

stack_dict = collections.defaultdict(int)

def fromStackToStack(amount: int, fromStack: int, toStack: int):
    toStack = toStack -1
    fromStack = fromStack -1
    for i in range(amount):
        stack_dict[toStack].appendleft(stack_dict[fromStack].popleft())
        print(stack_dict[toStack],stack_dict[fromStack])

with open("testinput.txt") as f:
    content = f.read()
    stacks = re.findall("\[(\w)\]|    ", content)
    stack_width = int(re.findall(" (\d) [^\w]", content)[::-1][0])
    stack_height = len(re.findall("(\D)\n", content))-1
    #print(stacks, stack_width, stack_height)
    for height in range(1,stack_height+1):
        current_line = stacks[stack_width*height-stack_width:stack_width*height]
        for item in range(len(current_line)):
            if current_line[item] == "":
                pass
            else: 
                print(current_line[item])
                stack_dict.setdefault(item, collections.deque()).append(current_line[item])

    instructions = re.findall("(\d+) \w+ (\d+) \w+ (\d+)", content)
    for inst in instructions:
        fromStackToStack(int(inst[0]), int(inst[1]), int(inst[2]))
    for i in range(stack_width):
        print(stack_dict[i].popleft(), end="")
#print(stack_dict)