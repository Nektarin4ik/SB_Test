import re
MIN = 2
MAX_LEFT = 4
MAX_RIGHT = 5

# Вариант с использованием регулярных выражений и встроенных функций для строк со сложностью O(n+m) 
def up_numbers1(nums: str):
    result =""
    x = re.findall(r'\d+\\\d+', nums) 
    for number in x:
        left, right = number.split('\\')
        if not MIN <= len(left) <= MAX_LEFT or not MIN <= len(right) <= MAX_RIGHT:
            continue
        left = "0"*(MAX_LEFT - len(left)) + left
        right = "0"*(MAX_RIGHT - len(right)) + right
        result = result + f'{left}\{right} '
    return result

# Вариант без регулярных выражений со сложностью O(n)
def up_numbers(num: str):
    one_num = ""
    result = ""
    valid = ""
    for i in range(len(num)):
        if num[i].isdigit():
            valid+=num[i]
        elif num[i] == "\\":
            if len(valid) < MIN or len(valid) > MAX_LEFT:
                valid=''
            elif MIN <= len(valid) <= MAX_LEFT:
                if len(valid) <= MAX_LEFT:
                    valid = "0"*(MAX_LEFT-len(valid))+valid+num[i]
                    one_num += valid
                    valid =""
        else:
            if len(one_num) > MIN and one_num[len(one_num)-1] != "\\" or len(one_num) == 0:
                valid =""
            elif len(valid) < MIN:
                one_num = ""
                valid = ""
            elif 2 <= len(valid) <= MAX_RIGHT:
                if len(valid) <= MAX_RIGHT:
                    one_num = one_num + "0"*(MAX_RIGHT-len(valid))+valid
                    result = result + one_num + " "
                    one_num = ""
                    valid = ""
        if i == len(num)-1 and num[i].isdigit() and num[i-len(valid)+1]=="\\":
            if MIN <= len(valid) <= MAX_RIGHT:
                if len(valid) <= MAX_RIGHT:
                        result = result+ "0"*(5-len(valid))+valid + " "
                        valid=""
    return result