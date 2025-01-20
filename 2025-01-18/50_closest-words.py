def solution(s):
    # Dictionary to store the last seen index of each character
    last_seen = {}
    # List to store the result
    result = []
    
    # Iterate through the string
    for i, char in enumerate(s):
        if char in last_seen:
            # If the character was seen before, calculate the distance
            result.append(i - last_seen[char])
        else:
            # If the character is appearing for the first time, append -1
            result.append(-1)
        
        # Update the last seen index of the current character
        last_seen[char] = i
    
    return result

def solution(s):
    def find_previous_occurrence(index, s):
        for j in range(index - 1, -1, -1):
            if s[index] == s[j]:
                return index - j
        return -1
    
    return [find_previous_occurrence(i, s) for i in range(len(s))]

# comment