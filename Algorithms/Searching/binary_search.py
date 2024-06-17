from typing import List, Optional, Any

def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Perform binary search on a sorted list.

    Parameters:
    arr (List[Any]): The sorted list to search.
    target (Any): The target value to search for.

    Returns:
    Optional[int]: The index of the target value if found, otherwise None.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Usage example
if __name__ == "__main__":
    sorted_list = [2, 3, 4, 10, 40, 50, 70]
    target = 10
    result = binary_search(sorted_list, target)
    
    if result is not None:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in the list")
