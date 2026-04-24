from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Находит индекс целевого элемента в отсортированном массиве.

    Args:
        arr (List[int]): Отсортированный по возрастанию список целых чисел.
        target (int): Искомое значение.

    Returns:
        int: Индекс элемента, если он найден. В противном случае возвращает -1.

    Time Complexity: O(log n), где n - длина массива.
    Space Complexity: O(1), так как используется константное количество дополнительной памяти.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Избегаем потенциального переполнения типа integer (важно для понимания CS)
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
