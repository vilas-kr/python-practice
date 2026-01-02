def binary_search(arr, key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1
lst = [2,6,7,94,658,3214]
print(binary_search(lst, 6))