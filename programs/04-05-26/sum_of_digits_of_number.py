def sum_of_digits(n: int) -> int:
    sum = 0
    while(n > 0):
        rem = n % 10
        n = n // 10
        sum += rem
    return sum

if __name__ == "__main__":
    print(sum_of_digits(156))