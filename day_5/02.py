import re, collections

stack_dict = collections.defaultdict(int)

def makeMove(amount: int, fromStack: int, toStack: int):
    toStack = toStack -1
    fromStack = fromStack -1
    secretQueue = collections.deque()
    for i in range(amount):
        secretQueue.appendleft(stack_dict[fromStack].popleft())
    print(secretQueue)
    for i in range(amount):
        #print("Nice int",stack_dict[toStack])
        stack_dict[toStack].appendleft(secretQueue.popleft())
    print(toStack,fromStack)


with open("input.txt") as f:
    content = f.read()
    stacks = re.findall("\[(\w)\]|    ", content)
    stack_width = int(re.findall(" (\d) [^\w]", content)[::-1][0])
    stack_height = len(re.findall("(\D)\n", content))-1
    #print(stacks, stack_width, stack_height)
    for y in range(0,stack_height*stack_width,stack_width):
        currentLine = stacks[y:y+stack_width]
        for char in range(len(currentLine)):
            #print(currentLine)
            if currentLine[char] == "":
                pass
            else:
                stack_dict.setdefault(char, collections.deque()).append(currentLine[char])
    print(stack_dict)
    instructions = re.findall("(\d+) \w+ (\d+) \w+ (\d+)", content)
    for inst in instructions:
        makeMove(int(inst[0]), int(inst[1]), int(inst[2]))

sorted(stack_dict)

for i in sorted(stack_dict):
    print(stack_dict[i].popleft(), end="")