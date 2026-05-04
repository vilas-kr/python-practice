from collections import Counter

def count_frequency(s: str) -> str:
    frequency_count = Counter(s)
    return frequency_count

if __name__ == "__main__":
    s = input("Enter a string : ")
    print(count_frequency(s))
    
    
