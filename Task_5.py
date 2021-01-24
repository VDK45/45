num = int(input('Введите число: '))
my = [7, 5, 3, 3, 2]
for x in my:
    if num > my[0]:
        my.insert(0, num)
        print(my)
        break
    elif num < my[-1]:
        my.append(num)
        print(my)
        break
    elif num == x:
        my.insert(my.index(x) + 1, num)
        print(my)
        break
    elif num < x:
        my.insert(my.index(x) + 1, num)
        print(my)
        break




n = int(input('Number enter: '))
r = [7, 5, 3, 3, 2]
print('Рейтинг - {}'.format(r))
for x in range(len(r)):
    if r[x] == n:
        r.insert(x + 1, n)
        break
    elif r[0] < n:
        r.insert(0, n)
    elif r[-1] > n:
        r.append(n)
    elif r[x] > n and r[x + 1] < n:
        r.insert(x + 1, n)
print('Получилось - {}'.format(r))
