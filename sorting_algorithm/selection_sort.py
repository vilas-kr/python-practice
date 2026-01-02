def selection_sort(lst:  list):
    for i in range(len(lst)-1):
        small = i
        for j in range(i+1, len(lst)):
            if lst[small] > lst[j]:
                small = j
        lst[small], lst[i] = lst[i], lst[small]

lst = [3, 2, 7, 4, 6, 6, 7, 1]
selection_sort(lst)
print(lst)

            