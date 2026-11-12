def solution(a, b, n):
    # Base case: not enough bottles to exchange
    if n < a:
        return 0
    
    # How many colas we get in this round
    new_cola = (n // a) * b
    
    # Remaining empty bottles after exchange + drinking
    remaining = (n % a) + new_cola
    
    # Recursive call + current result
    return new_cola + solution(a, b, remaining)