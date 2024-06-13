from typing import List 


def counting_sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr 
    
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num 
        count[num - min_val] -= 1
    
    return output 

if __name__ == "__main__":
    sample_list = [4, 2, 2, 8, 3, 3, 1]
    print("Original list:", sample_list)
    sorted_list = counting_sort(sample_list)
    print("Sorted list:", sorted_list)