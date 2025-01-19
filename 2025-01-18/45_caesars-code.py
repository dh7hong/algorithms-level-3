
# print(ord('a'))  # 97

# print("b".isupper())  # False

# print(chr(97))  # a

def solution(s, n):
    result = ""  # Initialize the resulting encrypted string

    for char in s:  # Iterate through each character in the input string
        if char.isalpha():  # Check if the character is a letter (not a space)
            ascii_offset = ord('A') if char.isupper() else ord('a')  # Determine if it's uppercase or lowercase
            shifted = (ord(char) - ascii_offset + n) % 26 + ascii_offset  # Shift the char within A-Z or a-z
            result += chr(shifted)  # Convert ASCII back to a char and append it
        else:
            result += char  # If it's a space, keep it unchanged

    return result  # Return the final encrypted string

