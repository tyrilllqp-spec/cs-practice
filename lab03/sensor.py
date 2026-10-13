# Максимум и среднее считаются только по корректным показаниям: error в них не участвует.
limit = float(input('Введите порог: '))
n = int(input('Введите количество записей: '))
assert n > 0, 'Количество записей должно быть больше нуля'

errors = 0
above = 0
i = 0

while i < n:
    record = input('Введите температуру или error: ')
    if record == 'error':
        errors = errors + 1
    else:
        temp = float(record)
        if temp > limit:
            above = above + 1
    i = i + 1

print('Всего записей:', n)
print('Ошибок:', errors)
print('Превышений:', above)
