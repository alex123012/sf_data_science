"""Игра угадай число."""

import numpy as np


number = np.random.default_rng().integers(1, 101)  # загадываем число

# количество попыток
COUNT = 0

while True:
    COUNT += 1
    predict_number = int(input("Угадай число от 1 до 100: "))

    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {COUNT} попыток")
        break  # конец игры выход из цикла
