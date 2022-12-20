#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    n = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            newlist.append(result)
    return newlist
