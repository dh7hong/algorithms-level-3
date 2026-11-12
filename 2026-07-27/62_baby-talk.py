def solution(babbling):
    # Define the possible words that the baby can pronounce
    possible_words = ["aya", "ye", "woo", "ma"]
    
    # Initialize a counter for valid words
    count = 0
    
    # Iterate through each word in the input list
    for word in babbling:
        original_word = word  # Store the original word for reference
        
        # Replace the possible words in the word with a placeholder ' '
        for pw in possible_words:
            word = word.replace(pw, ' ')
        
        # Check if the modified word consists only of spaces 
        # (valid pronunciation)
        if word.strip() == '':
            # Check for consecutive same words using simple logic
            is_valid = True
            for pw in possible_words:
                if pw * 2 in original_word:  # Consecutive repetition check
                    is_valid = False
                    break
            
            if is_valid:
                count += 1  # Increase valid word count
    
    return count  # Return the total count of valid words

# Example test cases
print(solution(["aya", "yee", "u", "maa"]))  # Output: 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # Output: 2
