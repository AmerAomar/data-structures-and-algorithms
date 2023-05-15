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

  #problem domain: giving a string with brackets, check if the brackets are balanced and return true if they are, false if they are not
    #input: string
    #output: boolean
    #edge cases: empty string, string with no brackets, string with only opening or closing brackets
    #approach: use a stack to keep track of the opening brackets, if we encounter a closing bracket, pop the last opening bracket from the stack and compare it to the closing bracket, if they are not the same, return false, if they are the same, continue, if the stack is empty at the end, return true, otherwise return false
    #big o: time: O(n), because we have to iterate through the string once, space: O(n), because we have to store the opening brackets in a stack
    #space: O(n), because we have to store the opening brackets in a stack
    #algorithm:
    #create a stack
    #create a set of opening brackets
    #create a set of closing brackets
    #create a dictionary of bracket pairs
    #iterate through the string
        #if the current character is an opening bracket
            #push it to the stack
        #if the current character is a closing bracket
            #if the stack is empty or the last opening bracket in the stack does not match the current closing bracket
                #return false
            #otherwise
                #pop the last opening bracket from the stack
    #if the stack is empty
        #return true
    #otherwise
        #return false