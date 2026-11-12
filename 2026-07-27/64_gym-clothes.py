def solution(n, lost, reserve):
    # Convert lists to sets for easy comparison
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # Students who lost and have an extra uniform
    intersection = lost_set & reserve_set
    lost_set -= intersection
    reserve_set -= intersection
    
    # Iterate through sorted reserve students to lend uniforms
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)  # Give to the left neighbor
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)  # Give to the right neighbor
    
    # Return the number of students who can participate
    return n - len(lost_set)

# Example test cases
print(solution(5, [2, 4], [1, 3, 5]))  # Output: 5
print(solution(5, [2, 4], [3]))  # Output: 4
print(solution(3, [3], [1]))  # Output: 2
