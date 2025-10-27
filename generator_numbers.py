import re # підгружаємо модуль регулярних виразів
from typing import Callable

def generator_numbers(text: str):
    # створюємо функцію generator_numbers, яка приймає один аргумент text — у якому будемо шукати числа;
    pattern = re.compile(r'(?<!\S)\d+(?:\.\d+)?(?!\S)')

    # шаблон знаходить окремі числа (цілі або з десятковою крапкою), відокремлені пробілами
    # Довго парилась, дякую Gpt))))
    # (?<!\S) — ліворуч НЕ-може бути символу, відмінного від пробілу 
    # (?!\S)  — праворуч теж має бути пробіл/кінець

    for num in pattern.finditer(text): # Шукаємо всі входження чисел у тексті:    
        yield float(num.group())

def sum_profit(text: str, func: Callable) -> float:
    # Створюємо функцію, яка підсумовує всі числа, які повернув генератор func(text).

    # func — функція, яку можна викликати (Callable), тобто я передаватиму сюди функцію generator_numbers

    return round(sum(func(text)), 2)

    # func(text) — запускаємо передану функцію (generator_numbers) для пошуку чисел у тексті;

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 та 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


