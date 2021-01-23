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
