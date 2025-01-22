# from itertools import combinations

# def is_prime(n):
#     """Check if a number is prime."""
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def solution(nums):
#     """Count the number of cases where the sum of three numbers is prime."""
#     count = 0
    
#     # Generate all possible combinations of three numbers
#     for combo in combinations(nums, 3):
#         if is_prime(sum(combo)):
#             count += 1
    
#     return count

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    """Count the number of cases where the sum of three numbers is prime."""
    count = 0
    n = len(nums)
    
    # Iterate through all possible triples in the list
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    count += 1
    
    return count

# Example usage
print(solution([1,2,3,4]))  # Output: 1
print(solution([1,2,7,6,4]))  # Output: 4