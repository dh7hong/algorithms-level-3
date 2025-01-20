def solution(s):
    # Dictionary to map English number words to their corresponding digits
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    # Iterate through the dictionary and replace occurrences 
    # of number words with their digits
    for word, digit in num_dict.items():
        s = s.replace(word, digit)  
        # Replace all occurrences of the word with its corresponding digit
    
    return int(s)  # Convert the final string to an integer and return


student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for name, score in student_scores.items():
    print(f"{name} scored {score} points.")
    