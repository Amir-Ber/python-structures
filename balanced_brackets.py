from structures.stack import Stack

open_brackets = ["{", "[", "("]
closed_brackets = ["}", "]", ")"]
brackets_dict = {"{":"}", "[":"]", "(":")"}
brackets = "{}"
open_brackets_stack = Stack()
closed_brackets_stack = Stack()

for i in brackets:
    if i in open_brackets:
        open_brackets_stack.push(i)
    else:
        closed_brackets_stack.push(i)


j=0
i=open_brackets_stack.pop()
while i:

    barckets_dict_pop = brackets_dict.get(i)
    closed_brackets_pop = closed_brackets_stack.pop()



    if barckets_dict_pop == closed_brackets_pop:
        i = open_brackets_stack.pop()
        continue
    elif :
        print("not balanced")
        break




