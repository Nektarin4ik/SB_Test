# Вариант с использованием встроенных методов для строк и сложностью O(n+k)
def upgrade_number1(num: str):
    good_num_left, good_num_right = num.split("\\")
    lenght_left = len(good_num_left)
    lenght_right = len(good_num_right)
    if 2 <= lenght_left <= 4 and 2 <= lenght_right <= 5:
        if lenght_left < 4:
            good_num_left = '0'*(4-lenght_left) + good_num_left
        if lenght_right < 5:
            good_num_right = '0'*(5-lenght_right) + good_num_right
        return good_num_left + '\\' + good_num_right
    return ('Error: неправильный формат хорошего номера')

# Вариант со сложностью O(n)
def upgrade_num(num: str):
    result = ""
    leading_zeros = ""
    for i in range(len(num)):
        if num[i] == "\\":
            result += num[i]
        elif num[i].isdigit():
            leading_zeros += num[i]
            if i < len(num)-1 and num[i+1] == '\\':
                if 2 <= len(leading_zeros) <=4: 
                    num_zeros = 4 - len(leading_zeros)
                    result += "0" * num_zeros + leading_zeros
                    leading_zeros = ""
                else:
                    return('Error: неправильный формат хорошего номера')
            elif i == len(num) - 1:
                if 2 <= len(leading_zeros) <=5: 
                    num_zeros = 5 - len(leading_zeros)
                    result += "0" * num_zeros + leading_zeros
                    leading_zeros = ""
                else:
                    return('Error: неправильный формат хорошего номера')
    return result
