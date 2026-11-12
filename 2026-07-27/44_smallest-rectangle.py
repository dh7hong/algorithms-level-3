
businessCard_sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    max_width = 0
    max_height = 0

    for w, h in sizes:
        print(f'오리지날: width={w}, height={h}')  # Debug: print original dimensions
        w, h = max(w, h), min(w, h)  # Ensure w is always the larger side
        print(f'조정 후: width={w}, height={h}')  # Debug: print adjusted dimensions
        max_width = max(max_width, w)  # Track the largest width
        max_height = max(max_height, h)  # Track the largest height
        print(f'현재 최대 너비: {max_width}, 현재 최대 높이: {max_height}')  # Debug: print current max dimensions

    return max_width * max_height  # The minimum wallet size

print(solution(businessCard_sizes))  # 4800