def solution(n, m, section):
    """Calculate the minimum number of times to paint the required sections."""
    count = 0  # Counter for the number of times painting is required
    current_position = 0  # Track the last painted position
    
    for s in section:
        if s > current_position:  # If the section is not already covered
            count += 1  # Increment the number of paintings
            current_position = s + m - 1  
            # Move the roller to cover this section
            """
            If you start at section s, 
            the roller will extend to s + m - 1 
            (because s itself is already counted as the first position).
            """
    
    return count

# Example usage
print(solution(8, 4, [2, 3, 6]))  # Output: 2
print(solution(5, 4, [1, 3]))  # Output: 1
print(solution(4, 1, [1, 2, 3, 4]))  # Output: 4
