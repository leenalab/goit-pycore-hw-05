def caching_fibonacci():
    # повертає внутрішню функцію fibonacci(n).
    cache: dict[int, int] = {} 

    # Створюємо порожній словник cache, у якому будемо зберігати результати обчислення

    def fibonacci(n: int) -> int: 
        # створюємо внутрішню функцію замикання, яку обчислює числа Фібоначчі з використанням кешування

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(8))  # 21
    print(fib(10))  # 55   

        #використана для обчислення чисел Фібоначчі з використанням кешування.


        # з використанням кешу (memoization) і рекурсії.
