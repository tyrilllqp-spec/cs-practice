# Итоги соревнования разбираются четырьмя небольшими функциями: кто победил, каков средний результат, как выглядит рейтинг и кто выступил выше среднего.
def winner(names: list[str], scores: list[float]) -> str:
    assert len(names) == len(scores)
    if len(names) == 0:
        return ''
    best = 0
    for i in range(len(scores)):
        if scores[i] > scores[best]:
            best = i
    return names[best]


def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0
    total = 0.0
    for score in scores:
        total = total + score
    return round(total / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    assert len(names) == len(scores)
    result = names.copy()
    points = scores.copy()
    for i in range(len(points) - 1):
        for j in range(len(points) - 1 - i):
            if points[j] < points[j + 1]:
                score = points[j]
                points[j] = points[j + 1]
                points[j + 1] = score
                name = result[j]
                result[j] = result[j + 1]
                result[j + 1] = name
    return result


def above_average(names: list[str], scores: list[float]) -> list[str]:
    assert len(names) == len(scores)
    mean = average(scores)
    result = []
    for i in range(len(scores)):
        if scores[i] > mean:
            result.append(names[i])
    return result


# >>> names = ['Аня', 'Боря', 'Вика']
# >>> scores = [7.0, 9.0, 9.0]
# >>> print(winner(names, scores))
# Боря
# >>> print(average(scores))
# 8.33
# >>> print(ranking(names, scores))
# ['Боря', 'Вика', 'Аня']
# >>> print(above_average(names, scores))
# ['Боря', 'Вика']

# >>> names = ['Оля', 'Ира', 'Лена']
# >>> scores = [5.0, 5.0, 5.0]
# >>> print(winner(names, scores))
# Оля
# >>> print(average(scores))
# 5.0
# >>> print(ranking(names, scores))
# ['Оля', 'Ира', 'Лена']
# >>> print(above_average(names, scores))
# []

# >>> names = ['Коля']
# >>> scores = [4.5]
# >>> print(winner(names, scores))
# Коля
# >>> print(average(scores))
# 4.5
# >>> print(ranking(names, scores))
# ['Коля']
# >>> print(above_average(names, scores))
# []

# >>> names = ['Аня', 'Боря', 'Вика']
# >>> scores = [-5.0, -1.0, -3.0]
# >>> print(winner(names, scores))
# Боря
# >>> print(average(scores))
# -3.0
# >>> print(ranking(names, scores))
# ['Боря', 'Вика', 'Аня']
# >>> print(above_average(names, scores))
# ['Боря']

# >>> names = ['Лена', 'Оля', 'Ира', 'Аня']
# >>> scores = [1.0, 3.0, 2.0, 3.0]
# >>> print(winner(names, scores))
# Оля
# >>> print(average(scores))
# 2.25
# >>> print(ranking(names, scores))
# ['Оля', 'Аня', 'Ира', 'Лена']
# >>> print(above_average(names, scores))
# ['Оля', 'Аня']

# >>> names = []
# >>> scores = []
# >>> print(average(scores))
# 0.0
# >>> print(ranking(names, scores))
# []
# >>> print(above_average(names, scores))
# []
