from typing import List, Tuple


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    """
    Знаходить мінімальний та максимальний елементи в масиві, використовуючи метод «розділяй і володарюй».

    Args:
        arr: Список чисел довільної довжини.

    Returns:
        Кортеж значень (мінімум, максимум).
    """
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return min(arr[0], arr[1]), max(arr[0], arr[1])

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)


# Тестування
if __name__ == "__main__":
    test_arrays = [
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [10],
        [8, 3],
        [-5, -10, 0, 5, 10],
        [100, 200, 300, 0, -100]
    ]

    for arr in test_arrays:
        min_val, max_val = find_min_max(arr)
        print(f"Масив: {arr}")
        print(f"Мінімум: {min_val}, Максимум: {max_val}\n")
