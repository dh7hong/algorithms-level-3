
s = "try hello world"

# fruits = ["apple", "banana", "cherry"]
# for idx, fruit in enumerate(fruits):
#     print(idx, fruit)

# t = s.upper()
# print(t)

# t = t.lower()
# print(t)

# x = 5 % 3
# print(x)

# fruits.append("orange")
# print(fruits)

# words = s.split(" ")
# print(words, type(words))

# sentence = " ".join(words)
# print(sentence, type(sentence))

def solution(s):
    words = s.split(" ")
    answer = []
    for word in words:
        new_word = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                new_word += char.upper()
            else:
                new_word += char.lower()
        answer.append(new_word)
    return " ".join(answer)

print(solution(s))

s2 = "try hello world"

def solution_2(s2):
    return " ".join(["".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(" ")])

print(solution_2(s2))

"""
step 1: Split the string s2 into words
step 2: list comprehension to iterate over the words
step 3: for each word w, "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) << this gets executed

For example:

# Word: "try"
enumerate("try") → [(0, 't'), (1, 'r'), (2, 'y')]
→ ['T', 'r', 'Y']
→ "TrY"


"""
