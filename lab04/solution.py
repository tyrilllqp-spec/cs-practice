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
