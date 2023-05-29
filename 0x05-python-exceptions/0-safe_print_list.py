#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    value = 0
    for index in range(x):
        try:
            print(my_list[index], end='')
            value += 1
        except indexError:
            None
       	print()
	return value
