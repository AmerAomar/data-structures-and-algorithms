from repeated_word import repeated_word

def test_repeated_word():
    
    input_string1 = "Once upon a time, there was a brave princess who..."
    assert repeated_word(input_string1) == "a"

    
    input_string2 = "It was the best of times, it was the worst of times, it was the age of wisdom..."
    assert repeated_word(input_string2) == "it"


    input_string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs..."
    assert repeated_word(input_string3) == "summer"

    
    input_string4 = "This is a test string with no repeated words."
    assert repeated_word(input_string4) is None

    
    input_string5 = ""
    assert repeated_word(input_string5) is None

    input_string6 = "hello"
    assert repeated_word(input_string6) is None

    input_string7 = "This is a test case. This is a Test Case."
    assert repeated_word(input_string7) == "this"

    print("All test cases pass.")

test_repeated_word()
