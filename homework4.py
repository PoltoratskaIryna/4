# Коментар для створення Pull Request: dev відрізняється від main
# Реалізація паралельного обчислення градин Колатца для чисел від 1 до 10 000 000
import time
from concurrent.futures import ThreadPoolExecutor

# Функція для обчислення кількості кроків до 1 за гіпотезою Колатца
def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    N = 10_000_000
    numbers = range(1, N + 1)
    num_threads = 8  # Можна змінити кількість потоків вручну

    start_time = time.time()

    total_steps = 0
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Паралельно обчислюємо градини
        results = executor.map(collatz_steps, numbers, chunksize=1000)
        for steps in results:
            total_steps += steps

    avg_steps = total_steps / N
    elapsed = time.time() - start_time

    print(f"Середня кількість кроків: {avg_steps:.2f}")
    print(f"Загальний час виконання: {elapsed:.2f} секунд")

if __name__ == "__main__":
    main()
