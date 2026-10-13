# Читает имя таблицы из первой строки ввода, открывает её и печатает три числа:
from pathlib import Path
from tablestats import read_rows, count_types, total_minutes, to_csv


if __name__ == '__main__':
    folder = Path(__file__).resolve().parent
    path = Path(input().strip())
    if not path.is_absolute() and not path.exists():
        path = folder / path

    with open(path, encoding='utf-8') as table:
        rows = read_rows(table)

    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(f'{total_minutes(rows, "ошибка"):.1f}')

    with open(folder / 'summary.csv', 'w', encoding='utf-8') as out:
        out.write(to_csv(counts))


# events.csv
# 14
# 4
# 2.5

# events-small.csv
# 3
# 2
# 2.0
