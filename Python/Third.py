# Сложность алгоритма O(nlogn)
def max_concatenated_number(array):
    # Я использовал лямбда-функцию чтобы приравнять строки в списке к одной длине и сравнить их, это учтет частные случаи которые не были учтены до этого
    array = sorted(array, key=lambda x: x * len(max(array)), reverse=True)
    return int(''.join(array)) 


def max_concatenated_number1(array):
    s_sorted = list()
    for i in range(len(array)):
        array[i] = array[i]*3
    sorted_lst = sorted(array, reverse=True)
    for i in sorted_lst:
        s_sorted.append(int(i))
    print(s_sorted)
    # return int(''.join(sorted_lst)) 

array = ['4' ,'43' ,'5' ,'54' ,'543']
for i in array:
    print(int(i))

print(max_concatenated_number1(array))