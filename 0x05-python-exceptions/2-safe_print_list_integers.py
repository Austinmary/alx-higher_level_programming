#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        for i in range(x):
            if (my_list[i]):
                if (isinstance(my_list[i], (int))):
                    print("{:d}".format(my_list[i]), end="")
                    n += 1
                else:
                    continue
    except Exception:
        raise
    else:
        print("")
        return n
