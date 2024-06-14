from typing import List 


def quick_sort(arr: List[int]) -> None:
    _quick_sort(arr, 0, len(arr) - 1)

def _quick_sort(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)

def _partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    sample_list = [10, 7, 8, 9, 1, 5]
    print("Original list:", sample_list)
    quick_sort(sample_list)
    print("Sorted list:", sample_list)