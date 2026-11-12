def find_previous_occurrence(index, s):
    for j in range(index - 1, -1, -1):
        if s[index] == s[j]:
            return index - j
    return -1

def solution(s):

    result = []
    for i in range(len(s)):
        result.append(find_previous_occurrence(i, s))
    
    return result

print(solution("banana"))  # [-1, -1, -1, 2, 2, 2]
print(solution("foobar"))  # [-1, -1, -1, -1, -1, -1]