def validate_brackets(string):
    '''
    Returns True if the string has balanced brackets, False otherwise.
    '''
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for bracket in string:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if not stack or bracket_pairs[stack.pop()] != bracket:
                return False
    
    return len(stack) == 0
