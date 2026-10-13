# Максимум и среднее считаются только по корректным показаниям: error в них не участвует.
limit = float(input('Введите порог: '))
n = int(input('Введите количество записей: '))
assert n > 0, 'Количество записей должно быть больше нуля'

errors = 0
above = 0
count = 0
total = 0
max_temp = 0
i = 0

while i < n:
    record = input('Введите температуру или error: ')
    if record == 'error':
        errors = errors + 1
    else:
        temp = float(record)
        count = count + 1
        total = total + temp
        if count == 1 or temp > max_temp:
            max_temp = temp
        if temp > limit:
            above = above + 1
    i = i + 1

assert count > 0, 'Нужно хотя бы одно корректное показание'
print('Всего записей:', n)
print('Ошибок:', errors)
print('Превышений:', above)
print(f'Максимум: {max_temp:.1f}')
print(f'Среднее: {total / count:.1f}')
