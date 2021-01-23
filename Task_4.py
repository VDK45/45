list_in = input("Напишите: ")
k = list_in.split()
print(k)
k.reverse()
i = len(k)
n = 1
while i > 0:
    print('{}: {}'.format(n, k[i - 1][0:10]))
    n += 1
    i -= 1
