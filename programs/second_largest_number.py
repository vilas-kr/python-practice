# Program to find the second largest number in a list

def find_second_largest(lst: list[int]):
    '''
    Find second largest number in the given list
    Args:
        lst : list of integers
    
    Returns:
        Second largest number in the given list
    '''
    first_largest = second_largest = lst[0]
    for i in lst[1:]:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i
        elif i > second_largest:
            second_largest = i
    return second_largest

if __name__ == '__main__':
    n = int(input('Enter number of elements : '))
    lst = [] 
    for i in range(n):
        lst.append(int(input()))
    second_largest = find_second_largest(lst)
    print(f'Second largest number in the given list is : {second_largest}')