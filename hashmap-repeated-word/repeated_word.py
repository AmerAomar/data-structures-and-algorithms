def repeated_word(input_string):
    cleaned_string = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string)

    
    words = cleaned_string.split()

    word_dict = {}

    for word in words:
        
        if word in word_dict:
            return word
        word_dict[word] = True

    return None
