"""
Stack Data Structure.
"""
import sys
sys.path.insert(1, '/home/fatih/Desktop/Archive/Code/Python/Data Structures and Algorithms/Stack')
from stack import Stack

def solveStack():
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    print(myStack.get_stack())
    myStack.push("C")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.get_stack())
    print(myStack.is_empty())

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1
        
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
        
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str
   
def convert_int_to_bin(dec_num):
    stack = Stack()
    
    while dec_num > 0:
        if dec_num % 2 == 0:
            stack.push(0)
            dec_num = dec_num / 2
        else:
            stack.push(1)
            dec_num = dec_num // 2
    reverselist = ''
    for _ in range(len(stack.get_stack())):
        reverselist += str(stack.pop())
            
    return reverselist
    
        


def main():
    # solveStack()
    
    # * Determine if Bracket is balanced
    # print("String : (((({})))) Balanced or not?")
    # print(is_paren_balanced("(((({}))))"))

    # print("String : [][]]] Balanced or not?")
    # print(is_paren_balanced("[][]]]"))
    
    # * Reverse String
    # stack = Stack()
    # input_str = "!evitacudE ot emocleW"
    # print(reverse_string(stack, input_str))
    
    # * Convert Decimal Integer to Binary
    print(convert_int_to_bin(16))


if __name__ == "__main__":
    main()
