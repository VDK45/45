tovar = {'Наименование': '', 'Цена': '', 'Количество': ''}
analitic = {'Наименование': [], 'Цена': [], 'Количество': []}
i = 0
while True:
    in_name = input('Какой товар пришел: ')
    in_price = input('Цена: ')
    in_count = input('Количество: ')
    i += 1
    tovar['Наименование'] = in_name
    tovar['Цена'] = in_price
    tovar['Количество'] = in_count
    analitic['Наименование'].append(in_name)
    analitic['Цена'].append(in_price)
    analitic['Количество'].append(in_count)
    print(
        '{}, Название: {} Цена: {} Количество: {}'.format(i, tovar['Наименование'], tovar['Цена'], tovar['Количество']))

    questions = input('Ещё добавить товар (нет выход): ')
    if questions == 'нет':
        break
    else:
        continue
print('Название: {}'.format(analitic['Наименование']))
print('Цена: {}'.format(analitic['Цена']))
print('Количество: {}'.format(analitic['Количество']))
