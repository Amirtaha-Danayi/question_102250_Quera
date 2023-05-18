def find(num1, num2, num3):
    list_number = []
    list_number.append(num1)
    list_number.append(num2)
    list_number.append(num3)
    base_list = [1,2,3,4]

    for i in base_list:
        if i not in list_number:
            return(i)
