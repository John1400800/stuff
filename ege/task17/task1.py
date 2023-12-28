def f(n: int) -> bool:
    if all(n % i for i in (7, 17, 19, 27)):
        return True
    return False

maxGood = 0
count = 0
for n in range(1017, 7937 + 1, 3):
    if f(n):
        count += 1
        maxGood = n
print(count, maxGood)
