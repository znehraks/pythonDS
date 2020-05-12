from stack import Stack

operator = ["+", "-", "*", "/"]
bracket = ["(", ")"]

def is_number(num):
    if num in operator or num in bracket:
        return False
    else:
        return True

def pref(p):
    if p in bracket:
        return 0
    elif p in ["+", "-"]:
        return 1
    elif p in ["*", "/"]:
        return 2

def infix_to_postfix(str):
    stack = Stack()
    a = []
    str = str.split()
    for i in str:
        if is_number(i):
            a.append(i)
        elif i in operator:
            p = pref(i)
            if not stack.is_empty():
                top = stack.peek()
                if p > pref(top):
                    stack.push(i)
                elif p <= pref(top):
                    a.append(stack.pop())
                    stack.push(i)
            else:
                stack.push(i)
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while True:
                if stack.peek() != "(":
                    a.append(stack.pop())
                else:
                    stack.pop()
                    break
    while not stack.is_empty():
        a.append(stack.pop())       
    return a
    
def postfix_calculator(str):
    stack = Stack()

    for i in str:
        if is_number(i):
            stack.push(i)
        elif i == "+":
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.push(num2 + num1)
        elif i == "-":
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.push(num2 - num1)
        elif i == "*":
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.push(num2 * num1)
        elif i == "/":
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            stack.push(num2 / num1)
    return stack.pop()

print(infix_to_postfix("( 12 + 3 * 3 ) / 3 + ( ( 6 + 8 ) / 2 + 3 ) + ( 5 + 3 ) "))#7

in_to_po = infix_to_postfix("( 12 + 3 * 3 ) / 3 + ( ( 6 + 8 ) / 2 + 3 ) + ( 5 + 3 ) ")
result = postfix_calculator(in_to_po)
print(result)