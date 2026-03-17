# Multi Processing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time


def square_numbers(number):
    time.sleep(2)
    return f"Square: {number * number}"


numbers = [1, 2, 3, 4, 5, 11, 12, 13, 14, 3, 9, 8]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)
