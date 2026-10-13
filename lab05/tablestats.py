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
