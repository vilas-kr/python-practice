def linear_search(arr: list, key: object):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

lst = [454,6,99,3,36,46,23]
print(linear_search(lst, 9))