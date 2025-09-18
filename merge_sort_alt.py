def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Add leftovers
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged


# Example run
nums = [9, 1, 4, 7, 2]
print("Before sorting:", nums)
sorted_nums = merge_sort(nums)
print("After sorting:", sorted_nums)
