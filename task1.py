def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def find_min_max(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return minimum, maximum


def bubble_sort(numbers):
    """Сортирует список чисел алгоритмом сортировки пузырьком."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def merge_sort(numbers):
    """Сортирует список чисел алгоритмом сортировки слиянием."""
    n = len(numbers)
    if n <= 1:
        return numbers
    # Базовый случай: список из 0 или 1 элемента уже отсортирован

    # 1. Разделяем список на две половины
    mid = n // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]

    # 2. Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 3. Сливаем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    """Сливает два отсортированных списка в один отсортированный список."""

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы из левого и правого списков (если они есть)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Ввод


input_str: str = input("Введите числа, разделенные запятыми: ")
numbers = [int(x.strip()) for x in input_str.split(',')]

# Вызов функций
even_nums = get_even_numbers(numbers)
# minimum, maximum = find_min_max(numbers)
# .copy() чтобы не изменить исходный списо
# sorted_numbers = bubble_sort(numbers.copy())
sorted_numbers = merge_sort(numbers.copy())
minimum, maximum = sorted_numbers[0], sorted_numbers[-1]
# Вывод
print("Четные числа:", even_nums)
print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Отсортированный список:", sorted_numbers)