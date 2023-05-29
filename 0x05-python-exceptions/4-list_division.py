#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    num = 0
    res_list = []
    while num < list_length:
        result = 0
        try:
            result = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            res_list_list.append(result)
            num += 1
    return res_list
