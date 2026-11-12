
t = "3141592"
p = "271"

def solution(t, p):
    count = 0
    p_length = len(p)
    p_value = int(p)  # Convert p to an integer for comparison
    
    # Iterate through t, extracting substrings of length p_length
    for i in range(len(t) - p_length + 1):  
        substring = t[i:i + p_length]  # Extract substring
        if int(substring) <= p_value:  # Compare as integers
            count += 1  # Increment count if condition is met

    return count  # Return the total count

print(solution(t, p))  # 3