
#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.

n = int(input("Введите количество монеток: "))
countA = 0
countB = 0
for i in range(n):
    temp = int(input(f"Введите {i + 1} монетку: "))
    if temp == 0:
        countA += 1
    elif temp == 1:
        countB += 1
print(min(countA, countB))


countC = 0
countD = 0
for i in range(int(input("Введите количество монеток: "))):
    if int(input(f"Введите {i + 1} монетку: ")) == 0:
        countC += 1
    else:
        countD += 1
print(min(countC, countD))

10
 
 
if __name__ == "__main__":
    main()