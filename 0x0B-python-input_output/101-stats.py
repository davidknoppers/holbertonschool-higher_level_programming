#!/usr/bin/python3
import sys
"""
module contains one big function
"""

filesize = count = 0
status_codes = {202: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
try:
    for line in sys.stdin:
        if count % 10 == 0:
            print("File size: {}".format(filesize))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
        for key in status_codes.keys():
            if str(key) in line:
                status_codes[key] = status_codes[key] + 1
        size = line.rsplit(' ', 1)[1]
        filesize += int(size)
        count += 1
except KeyboardInterrupt:
    print("File size: {}".format(filesize))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
