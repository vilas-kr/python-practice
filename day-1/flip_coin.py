import random

count = int(input("Enter number of times to flip coin : "))
while(count <= 0):
    count = int(input("Enter positive number : "))
head = 0
tail = 0
for i in range(count):
    if(0.5 < random.random()):
        tail += 1
    else:
        head += 1
print(f"Head : {(head/count)*100 :.2f}%   Tail : {(tail/(count))*100 :.2f}%")
    
