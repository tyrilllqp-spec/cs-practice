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
