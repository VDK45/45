spisok = list(input("Введите список: "))
#spisok = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'f', '5', 'g', '6']
i = 0
for x in range(len(spisok)//2):
    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
    i += 2
print(spisok)

print('-'*9, 'второй вариан с while переворпачивает список обратно: ')

i = len(spisok) // 2
x = 0
while 0 < i:
    spisok[x], spisok[x + 1] = spisok[x + 1], spisok[x]
    i -= 1
    x += 2
print(spisok)
