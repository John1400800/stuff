def f(n):
    if all(n % i for i in (11, 17, 19, 23)):
        return True
    return False

count = 0
maxGood = 0
for n in range(1035, 7738, 5):
    if f(n):
        count += 1
        maxGood = n

print(count, maxGood)