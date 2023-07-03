def repeated_word(input_string):
    # Clean the input string by removing punctuations and converting to lowercase
    cleaned_string = ''.join(char.lower() if char.isalnum() else ' ' for char in input_string)

    # Split the cleaned string into words
    words = cleaned_string.split()

    # Create a hash set to store encountered words
    word_set = set()

    # Iterate through each word in the words list
    for word in words:
        # If the word is already in the word_set, it's the first repeated word
        if word in word_set:
            return word
        # Otherwise, add the word to the word_set
        word_set.add(word)

    # Return None if no repeated words found
    return None
