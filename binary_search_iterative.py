def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"Checking index {mid}, value {arr[mid]}")

        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"{target} not found in array")
    return -1


# Example run
arr = [2, 4, 6, 8, 10, 12, 14]
search_for = 7
print("Array:", arr)
binary_search(arr, search_for)
