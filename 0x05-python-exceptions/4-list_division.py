#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    quotients = []
    while i < list_length:
        try:
            quotients.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            quotients.append(0)
        except TypeError:
            print("wrong type")
            quotients.append(0)
        except IndexError:
            print("out of range")
            quotients.append(0)
        finally:
            i += 1
    return quotients
