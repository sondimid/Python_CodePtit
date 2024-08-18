def min_sum_of_triplet(arr):

    min1, min2, min3 = float('inf'), float('inf'), float('inf')

    for num in arr:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num

    return min1 + min2 + min3


# Đọc dữ liệu vào
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if N < 3:
        print("Error: Array must have at least 3 elements")
    else:
        result = min_sum_of_triplet(A)
        print(result)
