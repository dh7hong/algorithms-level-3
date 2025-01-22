def count_divisors(num):
    """Return the number of divisors of a given number."""
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

def solution(number, limit, power):
    """
    Calculate the total weight of iron needed to 
    forge weapons for the knights.
    """
    total_weight = 0
    
    for i in range(1, number + 1):
        attack_power = count_divisors(i)  
        # Determine the attack power based on divisor count
        if attack_power > limit:  
            # If attack power exceeds the limit, use the specified power
            attack_power = power
        total_weight += attack_power  # Accumulate total weight
    
    return total_weight

# Example usage
print(solution(5, 3, 2))  # Output: 10
print(solution(10, 3, 2))  # Output: 21
