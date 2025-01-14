from typing import List
import random


def quickselect(arr: List[int], k: int) -> int:
    """
    Знаходить k-ий найменший елемент у несортованому масиві, використовуючи алгоритм Quick Select.

    Args:
        arr: Масив чисел.
        k: Порядковий номер найменшого елемента (1-based).

    Returns:
        k-ий найменший елемент масиву.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k повинно бути в межах від 1 до довжини масиву")

    def partition(low: int, high: int) -> int:
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Переміщення pivot у кінець
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]  # Переміщення pivot на своє місце
        return i

    low, high = 0, len(arr) - 1
    k_index = k - 1  # Перетворення на 0-based індекс

    while low <= high:
        pivot_index = partition(low, high)
        if pivot_index == k_index:
            return arr[pivot_index]
        elif pivot_index < k_index:
            low = pivot_index + 1
        else:
            high = pivot_index - 1


# Тестування
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 1, 5, 4], 3),  # 3-ій найменший елемент -> 3
        ([10, 4, 5, 8, 6, 11, 26], 4),  # 4-ий найменший елемент -> 8
        ([10, 3, 5, 8, 2], 2),  # 1-ий найменший елемент -> 1
        ([7, 10, 4, 3, 20, 15], 4),  # 4-ий найменший елемент -> 10
        ([9, 7, 2, 8, 6], 4)  # 5-ий найменший елемент -> 5
    ]

    for arr, k in test_cases:
        result = quickselect(arr, k)
        print(f"Масив: {arr}, k: {k}, k-ий найменший елемент: {result}")
