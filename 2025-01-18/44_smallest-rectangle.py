
businessCard_sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    max_width = 0
    max_height = 0

    for w, h in sizes:
        w, h = max(w, h), min(w, h)  # Ensure w is always the larger side
        max_width = max(max_width, w)  # Track the largest width
        max_height = max(max_height, h)  # Track the largest height

    return max_width * max_height  # The minimum wallet size

print(solution(businessCard_sizes))  # 4800