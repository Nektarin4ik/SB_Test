# Сложность алгоритма O(nlogn)
def max_number(array: list):
    for s in array:
        if not s.isdigit():
            raise ValueError("Строка должна содержать только цифры: {}".format(s))
    sorted_lst = sorted(array, reverse=True)
    concatenated_num = int(''.join(sorted_lst))
    return concatenated_num