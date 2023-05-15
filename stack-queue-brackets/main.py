from stack_queue_brackets import validate_brackets

if __name__ == "__main__":
    test_cases = [
        "{}",
        "{}(){}",
        "()[[Extra Characters]]",
        "(){}[[]]",
        "{}{Code}[Fellows](())",
        "[({}]",
        "(](",
        "{(})"
    ]

    for case in test_cases:
        if validate_brackets(case):
            print(f"{case}: Balanced")
        else:
            print(f"{case}: Not balanced")
