#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    name_list = dir(hidden_4)
    sorted(name_list)
    for i, name in enumerate(name_list):
        if name[:2] == "__":
            print("{:s}".format(name))
