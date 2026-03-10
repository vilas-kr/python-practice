# Program to count frequency of each character in a string

def count_character(s: str):
    result = {}
    for i in s:
        if i in result:
            result[i] += 1 
        else:
            result[i] = 1
    return result

if __name__ == '__main__':
    s = input('Enter a string : ')
    char_frequency = count_character(s)
    for i in char_frequency:
        print(f'{i} -> {char_frequency[i]}')
    