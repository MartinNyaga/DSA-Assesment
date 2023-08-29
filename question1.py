
def is_balanced(expression):
    l = []
    condition = True
    
    
    if len(expression) % 2 != 0:
        return False

    for char in expression:
        if condition:
            if char in "{([":
                l.append(char)
            elif char in "})]":
                if char == '}':
                    condition = l.pop() == '{'
                if char == ']':
                    condition = l.pop() == '['
                if char == ')':
                    condition = l.pop() == '('
            else:
                condition = False
                
    return condition
        
expression1 = "([]{})"
expression2 = "([)}]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
