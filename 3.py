n = int(input("введите число"))
i = 1
while i <= n:
    i += 1
    if n % i == 0:
        print(i)
        break

for i in range(2, n + 1):
    if not n % i:
        print(i)
        break