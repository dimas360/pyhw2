num = int(input("Количество учеников: "))
list_of_heigth = []
for i in range(num):
    heigth = int(input(f"Рост {i + 1} ученика: "))
    list_of_heigth.append(heigth)
petya = int(input("Рост Пети: "))
list_of_heigth.append(petya)
list_of_heigth.sort(reverse=True)
print(list_of_heigth.index(petya) + 1)


lst = []
for i in range(int(input("Кол-во: "))):
    lst.append(int(input("Рост по убыванию: ")))
pet = int(input("Рост Пети: "))
for j in range(len(lst)):
    if lst[j] <= pet:
        print(j + 1)
        break