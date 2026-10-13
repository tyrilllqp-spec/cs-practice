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
