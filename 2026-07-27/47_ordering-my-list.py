def solution(strings, n):
    """
    Sorts a list of strings based on the character at index 'n'.
    If two strings have the same character at index 'n', they are sorted alphabetically.
    """
    
    # Iterate over each element in the list to implement selection sort
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):  # Compare the current string with the rest
            
            # Compare based on the nth character
            if strings[i][n] > strings[j][n]:
                strings[i], strings[j] = strings[j], strings[i]  # Swap if out of order
            
            # If nth characters are the same, compare the whole string alphabetically
            elif strings[i][n] == strings[j][n] and strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]  # Swap if out of order
    
    return strings  # Return the sorted list

# Test cases to verify the solution
print(solution(["sun", "bed", "car"], 1))  # Expected output: ['car', 'bed', 'sun']
print(solution(["abce", "abcd", "cdx"], 2))  # Expected output: ['abcd', 'abce', 'cdx']
