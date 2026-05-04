from collections import defaultdict

def first_non_repeating_character(s: str) -> str:
    char_list = defaultdict(int)
    
    for c in s:
        char_list[c] += 1
        
    for k, v in char_list.items():
        if v == 1:
            return k
    
if __name__ == "__main__":
    s = input("Enter a string : ")
    print(first_non_repeating_character(s))