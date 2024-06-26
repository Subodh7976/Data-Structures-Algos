from typing import List

def counting_sort(arr: List[int], exp: int) -> None:
    n = len(arr)
    output = [0] * n  
    count = [0] * 10  

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr: List[int]) -> None:
    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

