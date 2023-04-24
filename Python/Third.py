# Сложность алгоритма O(nlogn)
def max_concatenated_number(array):
    # Я использовал лямбда-функцию чтобы приравнять строки в списке к одной длине и сравнить их, это учтет частные случаи которые не были учтены до этого
    array = sorted(array, key=lambda x: x * len(max(array)), reverse=True)
    return int(''.join(array))  
