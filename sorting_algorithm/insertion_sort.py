def insertion_sort(lst: list):
    for i in range(1, len(lst)):
        insert_index = i
        cur_ele = lst[i]
        for j in range((i-1), -1, -1):
            if cur_ele < lst[j]:
                lst[j+1] = lst[j]
                insert_index = j
            else:
                break
        lst[insert_index] = cur_ele
        
                
lst = [5,6,9,23,4,5,3,7]
insertion_sort(lst)
print(lst)         