def sorted_numbers(inp):
    for i in range(1, len(inp)):
        x = inp[i]
        idx = i
        while idx > 0 and inp[idx - 1] > x:
            inp[idx] = inp[idx - 1]
            idx = idx - 1
        inp[idx] = x
    return inp

def binary_search(sequence, numb_from_seq, left, right):
    if left > right:
        return print("Число в списке не найдено!")

    middle = (right + left) // 2
    if sequence[middle] == numb_from_seq:
        return middle
    elif numb_from_seq < sequence[middle]:
        return binary_search(sequence, numb_from_seq, left, middle - 1)
    else:
        return binary_search(sequence, numb_from_seq, middle + 1, right)

numb = input('Введите числа через пробел ').split()
sequence = list(map(int, numb))
sequence_sorted = sorted_numbers(sequence)
print("Создаем упорядоченный список:")
print(sequence_sorted)
numb_from_seq = int(input('Введите число для поиска его в остортированном списке '))
id_numb = binary_search(sequence_sorted, numb_from_seq, 0, len(sequence_sorted))
print("Индекс числа в отсортированном списке: ", id_numb)
