def solution(X, Y):
    # Create dictionaries to count occurrences of each digit in X and Y
    count_X = {}
    count_Y = {}
    
    for digit in X:
        if digit in count_X:
            count_X[digit] += 1
        else:
            count_X[digit] = 1
    
    for digit in Y:
        if digit in count_Y:
            count_Y[digit] += 1
        else:
            count_Y[digit] = 1
    
    # Find the common digits and their minimum occurrences
    common_digits = []
    for digit in count_X:
        if digit in count_Y:
            common_digits.extend([digit] * min(count_X[digit], count_Y[digit]))
    
    # If no common digits, return "-1"
    if not common_digits:
        return "-1"
    
    # Sort in descending order to get the largest possible number
    common_digits.sort(reverse=True)
    
    # If the largest number is "0", return "0"
    if common_digits[0] == "0":
        return "0"
    
    # Join and return as a string
    return "".join(common_digits)

# Example test cases
print(solution("100", "2345"))  # Output: "-1"
print(solution("100", "203045"))  # Output: "0"
print(solution("100", "123450"))  # Output: "10"
print(solution("12321", "42531"))  # Output: "321"
print(solution("5525", "1255"))  # Output: "552"
