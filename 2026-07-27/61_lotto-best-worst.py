def solution(lottos, win_nums):
    """Determine the highest and lowest rank possible in the lottery."""
    rank = [6, 6, 5, 4, 3, 2, 1]  # Mapping matched count to rank
    
    matched = sum(1 for num in lottos if num in win_nums)  
    # Count of known matched numbers
    unknowns = lottos.count(0)  
    # Count of unknown numbers (0s)
    
    highest_rank = rank[matched + unknowns]  
    # Best case: all unknowns match winning numbers
    lowest_rank = rank[matched]  
    # Worst case: unknowns do not match winning numbers
    
    return [highest_rank, lowest_rank]

# Example usage
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  
# Output: [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [31, 10, 45, 1, 6, 19]))  
# Output: [1, 6]
print(solution([38, 19, 20, 40, 15, 25], [31, 10, 45, 1, 6, 19]))  
# Output: [6, 6]
