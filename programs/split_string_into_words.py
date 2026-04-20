def split_words(s: str) -> list[str]:
    s = s.split(" ")
    return s

if __name__ == "__main__":
    s = input("Enter a sentance : ")
    words = split_words(s)
    print(f"Number of words in the entered sentance is {len(words)}")