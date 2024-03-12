def distance(time, start, speed):
    return (start + time * speed) % 360  # Приведение к интервалу [0, 360)


def meet_at_same_distance(start1, speed1, start2, speed2):
    # Функция для нахождения разности расстояний между мальчиками в заданный момент времени
    def f(t):
        return distance(t, start1, speed1) - distance(t, start2, speed2)

    # Бинарный поиск или метод Ньютона для нахождения момента времени, когда расстояния будут равными
    left = 0
    right = 360  # Максимальное время, чтобы обеспечить обход всего круга
    epsilon = 1e-9  # Точность

    while right - left > epsilon:
        mid = (left + right) / 2
        if f(mid) > 0:
            left = mid
        else:
            right = mid

    # Проверяем, сходятся ли расстояния в пределах точности
    if abs(f(left)) < epsilon:
        return "YES\n{}".format(left)
    else:
        return "NO"


# Пример использования
start1 = 1
speed1 = 1
start2 = 3
speed2 = 1

print(meet_at_same_distance(start1, speed1, start2, speed2))