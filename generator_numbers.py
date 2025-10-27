import re # підгружаємо модуль регулярних виразів
from typing import Callable

def generator_numbers(text: str):
    # створюємо функцію generator_numbers, яка приймає один аргумент text — рядок (тип str).
    pattern = re.compile(r'(?<!\S)\d+(?:\.\d+)?(?!\S)')

    # шаблон знаходить окремі числа (цілі або з десятковою крапкою), відокремлені пробілами
    # Довго парилась, дякую Gpt))))
    # (?<!\S) — ліворуч НЕ-може бути символу, відмінного від пробілу 
    # (?!\S)  — праворуч теж має бути пробіл/кінець

    for num in pattern.finditer(text): # Шукаємо всі входження чисел у тексті:    
        yield float(num.group())

def sum_profit(text: str, func: Callable) -> float:
    # Створюємо функцію, яка підсумовує всі числа, які повернув генератор func(text).
    