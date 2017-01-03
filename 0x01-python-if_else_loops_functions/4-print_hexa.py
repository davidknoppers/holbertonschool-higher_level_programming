#!/usr/bin/python3
for hex_num in range(0, 99):
    if hex_num < 17:
        print("{:d} = 0x{:01x}".format(hex_num, hex_num))
    else:
        print("{:d} = 0x{:02x}".format(hex_num, hex_num))
