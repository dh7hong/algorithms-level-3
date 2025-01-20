a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    result = []  # List to store the final results
    
    # Iterate through each command in commands
    for command in commands:
        i, j, k = command  # Extract i, j, k from the command list
        
        # Step 1: Slice the array from index (i-1) to (j) 
        # (Python slicing excludes the last index)
        sliced_array = array[i-1:j]
        
        # Step 2: Sort the sliced array in ascending order
        sorted_array = sorted(sliced_array)
        
        # Step 3: Find the k-th element 
        # (1-based index, so we access (k-1) in 0-based index)
        kth_element = sorted_array[k-1]
        
        # Append the found element to the result list
        result.append(kth_element)
    
    return result  # Return the final list containing all results

print(solution(a, c))  # Expected output: [5, 1, 3]