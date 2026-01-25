def solution(brown, yellow):
    
    for height in range(3, 5000):
        for width in range(height, (yellow+brown)//height+1):
            # print(f"[DEBUG] {width} {height}")
            if (width-2) * (height-2) == yellow and width * height == yellow + brown:
                return [width, height]