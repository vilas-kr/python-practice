def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = merge_sort(unsortedArr)
print("Sorted array:", sortedArr)
    