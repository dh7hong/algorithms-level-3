def solution(a, b, n):
    total_colas = 0  
    # Variable to store the total number of colas received
    
    while n >= a:  
        # Continue the process while we have enough bottles to exchange
        new_colas = (n // a) * b  
        # Calculate the number of colas received in exchange
        total_colas += new_colas  
        # Add to the total count
        n = (n % a) + new_colas  
        # Update the number of bottles available for the next exchange
    
    return total_colas  
    # Return the total number of colas received
