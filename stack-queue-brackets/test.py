from stack_queue_brackets import validate_brackets
def test_validate_brackets():
    # Test valid cases
    assert validate_brackets("{}") == True
    assert validate_brackets("{}(){}") == True
    assert validate_brackets("()[[Extra Characters]]") == True
    assert validate_brackets("(){}[[]]") == True
    assert validate_brackets("{}{Code}[Fellows](())") == True

    # Test invalid cases
    assert validate_brackets("[({}]") == False
    assert validate_brackets("(](") == False
    assert validate_brackets("{(})") == False
    assert validate_brackets("(") == False
    assert validate_brackets(")") == False
    assert validate_brackets("[") == False
    assert validate_brackets("]") == False
    assert validate_brackets("{") == False
    assert validate_brackets("}") == False
    assert validate_brackets("([)]") == False
    assert validate_brackets("((()") == False
    assert validate_brackets("}}}}") == False
    assert validate_brackets("{{{") == False
    assert validate_brackets("({)}") == False
    assert validate_brackets("({{[[]]}}})") == False
    assert validate_brackets("({{[[]]})") == False
