def single_letter_count(word, letter):
    lowercase_word = word.lower()
    letter_count = 0
    for words in lowercase_word:
        if words == letter:
            letter_count += 1
    return letter_count

    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """