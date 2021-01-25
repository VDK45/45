num = float(input('Введите число: '))
my = [7, 5, 3, 3, 2]
for i in my:
    if num > my[0]:
        my.insert(0, num)
        print(my)
        break
    elif num <= my[-1]:
        my.append(num)
        print(my)
        break
    elif num == my[my.index(i)] and num == my[my.index(i) + 1]:
        my.insert(my.index(i) + 2, num)
        print(my)
        break
    elif num == my[my.index(i)]:
        my.insert(my.index(i) + 1, num)
        print(my)
        break
    elif num < my[my.index(i)] and num > my[my.index(i) + 1]:
        my.insert(my.index(i) + 1, num)
        print(my)
        break
