"""Игра угадай число.

Компьютер сам загадывает и сам угадывает число.
"""

from typing import Callable

import numpy as np


def random_predict_by_square_division(number: int = 1) -> int:
    """Рандомно угадываем число.

    Args:
    ----
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
    -------
        int: Число попыток
    """
    count = 0
    base, delim = 50, 2
    predict_number = base
    while True:
        count += 1
        if predict_number == number:
            break

        base = d if (d := base // (delim)) else 1
        if predict_number > number:
            predict_number = predict_number - base
        elif predict_number < number:
            predict_number = predict_number + base

    return count


def score_game(random_predict: Callable[[int], int]) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм.

    Args:
    ----
        random_predict (RandomPredictCallable): функция угадывания

    Returns:
    -------
        int: среднее количество попыток
    """  # noqa: RUF002
    # загадали список чисел
    random_array = np.random.default_rng().integers(1, 101, size=1000)

    count_ls = [random_predict(number) for number in random_array]

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")  # noqa: T201
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict_by_square_division)
