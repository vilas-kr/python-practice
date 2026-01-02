def sequence(n):
    count = 1
    while count < n:
        yield count
        count += 2

for i in sequence(int(input("Enter a range : "))):
    print(i)