def reverse_words(s: str) -> str:
    s = s.split()
    s = s[::-1]
    return " ".join(s)

if __name__ == "__main__":
    s = input("Enter a sentance : ")
    print(f"reverse sentance is : {reverse_words(s)}")
