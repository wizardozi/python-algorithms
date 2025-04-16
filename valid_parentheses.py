def valid_parentheses(input):
    open = ['(', '{', '[']
    close = [')', '}', ']']
    stack = []    
    for bracket in input:
        if bracket in open:            
            stack.append(bracket)
        elif bracket in close:
            if stack and close.index(bracket) == open.index(stack[-1]):                
                stack.pop()           
            else: 
                return False 
        else:
            return False
    
    return not stack
        
bracket_string = input('Enter some brackets: ')

print(str(valid_parentheses(bracket_string)))