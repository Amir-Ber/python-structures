from structures.stack import Stack

open_brackets = ["{", "[", "("]
closed_brackets = ["}", "]", ")"]
brackets_dict = {"{": "}", "[": "]", "(": ")"}

brackets = "{[]}"
open_brackets_stack = Stack()
closed_brackets_stack = Stack()

# before starting lets verify that brackets are even
if len(brackets) % 2 != 0:
    print("baasa")
    exit()

for i in brackets:
    if i in open_brackets:
        open_brackets_stack.push(i)
    else:
        closed_brackets_stack.push(i)

# lets verify that there is the same amount of open and close brackets
if open_brackets_stack.__sizeof__() != closed_brackets_stack.__sizeof__() :
    print("baasa")
    exit()

i = open_brackets_stack.pop()
# check if brackets from open eq closed barckets end pop represented in brackets_dict
while i:

    barckets_dict_pop = brackets_dict.get(i)


    if i == brackets_dict.get(closed_brackets_stack.end_stack_pop()):
        i = open_brackets_stack.pop()
        continue
    else:
        print("baasa")
        exit()



def is_valid_brackets(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return not stack

# ✅ Tests

tests = [
    ("()[]{}", True),
    ("([{}])", True),
    ("(]", False),
    ("({[})", False),
    ("", True),
    ("[()]", True),
    ("[(])", False),
    ("([{}])[]", True),
]

for s, expected in tests:
    result = is_valid_brackets(s)
    print(f"{s!r} -> {result} (Expected: {expected})")
