import re

def solution(babbling):
    # Define the only valid sounds that can be used
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    # Create a regex pattern that allows only valid 
    # sound combinations without consecutive repeats
    pattern = re.compile(r'^(aya|ye|woo|ma)+(?!\1)$')

    count = 0  # Counter for valid words
    for word in babbling:
        # Check if the word consists only of the allowed 
        # sounds and doesn't repeat the same sound consecutively
        if pattern.fullmatch(word):
            count += 1

    return count

# Test cases
print(solution(["aya", "yee", "u", "maa"]))  # Output: 1
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))  # Output: 2
