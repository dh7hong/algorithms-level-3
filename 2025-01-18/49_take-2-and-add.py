def solution(numbers):
    # Create a set to store unique sums
    sum_set = set()
    
    # Get the length of the numbers list
    n = len(numbers)
    
    # Iterate through all possible pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            # Add the sum of the two numbers to the set
            sum_set.add(numbers[i] + numbers[j])
    
    # Convert the set to a sorted list and return it
    return sorted(sum_set)

# Test cases
print(solution([2, 1, 3, 4, 1]))  # Output: [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7]))    # Output: [2, 5, 7, 9, 12]
