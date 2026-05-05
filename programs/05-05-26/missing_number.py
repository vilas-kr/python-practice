nums = [1,2,4,5]

n = len(nums) + 1
expected = n * (n + 1) // 2

print(expected - sum(nums))