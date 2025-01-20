# Removing the last element (default behavior)
numbers = [1, 2, 3, 4, 5]
last_item = numbers.pop()
print(last_item)  # Output: 5
print(numbers)    # Output: [1, 2, 3, 4]

# Removing an element at a specific index
fruits = ["apple", "banana", "cherry", "date"]
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: 'banana'
print(fruits)         # Output: ['apple', 'cherry', 'date']

#Using .pop() in a loop
stack = [1, 2, 3, 4, 5]
while stack:
    print(stack.pop())  # Removes and prints elements from the end