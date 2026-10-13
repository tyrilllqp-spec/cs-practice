# Первая строка — заголовок: названия колонок.
def read_rows(lines: list[str]) -> list[dict]:
    header = []
    rows = []
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        fields = line.split(',')
        for i in range(len(fields)):
            fields[i] = fields[i].strip()
        if header == []:
            header = fields
        elif len(fields) == len(header):
            row = {}
            for i in range(len(header)):
                row[header[i]] = fields[i]
            rows.append(row)
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row['тип']
        if kind in counts:
            counts[kind] = counts[kind] + 1
        else:
            counts[kind] = 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row['тип'] == kind:
            text = row['минуты'].replace(',', '.')
            try:
                minutes = float(text)
            except ValueError:
                continue
            total = total + minutes
    return round(total, 1)


def to_csv(counts: dict) -> str:
    text = 'тип,количество\n'
    for kind in sorted(counts):
        text = text + kind + ',' + str(counts[kind]) + '\n'
    return text


# >>> rows = read_rows([])
# >>> print(rows)
# []
# >>> print(count_types(rows))
# {}
# >>> print(total_minutes(rows, 'ошибка'))
# 0.0

# >>> rows = read_rows(['дата,тип,минуты', '2026-03-01,запуск,1.5', '2026-03-01,ошибка,0.4'])
# >>> print(count_types(rows))
# {'запуск': 1, 'ошибка': 1}
# >>> print(total_minutes(rows, 'ошибка'))
# 0.4

# >>> rows = read_rows(['дата,тип,минуты', 'битая строка', '2026-03-01,ошибка,1', 'лишние,поля,в,строке'])
# >>> print(len(rows))
# 1
# >>> print(total_minutes(rows, 'ошибка'))
# 1.0

# >>> rows = read_rows([' ', ' дата , тип , минуты ', '', ' 2026-03-01 , ошибка , 2.5 '])
# >>> print(rows)
# [{'дата': '2026-03-01', 'тип': 'ошибка', 'минуты': '2.5'}]
# >>> print(total_minutes(rows, 'ошибка'))
# 2.5

# >>> rows = [{'тип': 'ошибка', 'минуты': '1,5'}, {'тип': 'ошибка', 'минуты': 'нет'}, {'тип': 'ошибка', 'минуты': '0.5'}]
# >>> print(total_minutes(rows, 'ошибка'))
# 2.0
# >>> print(total_minutes(rows, 'запуск'))
# 0.0

# >>> print(to_csv({'проверка': 4, 'ошибка': 4, 'запуск': 4, 'выгрузка': 2}), end='')
# тип,количество
# выгрузка,2
# запуск,4
# ошибка,4
# проверка,4
