def evaluate_post_fix(exp):
    stack = MyStack()
    for char in exp:
        if char.isdigit():
            stack.push(char)
        else:
            left = stack.pop()
            right = stack.pop()
            ''' Using Python's eval () method that takes a str expression, 
            evaluates it and returns an integer '''  
            stack.push(str(eval(right + char + left)))
    return int(float(stack.pop()))