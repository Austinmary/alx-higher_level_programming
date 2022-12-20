#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            if (my_list[i]):
                n += 1
                print(f"{my_list[i]}", end="")
    except Exception:
        pass
    print("")
    return n
