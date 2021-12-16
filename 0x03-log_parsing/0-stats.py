#!/usr/bin/python3
"""
This module contains the function that displays the
stats from the standard input
"""
import re
import sys
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
print_counter = 0
size_summation = 0


def print_logs():
    """
    Prints status codes to the logs
    """
    print("File size: {}".format(size_summation))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            std_line = line.replace("\n", "")
            log_list = re.split('- | "|" | " " ', str(std_line))
            try:
                codes = log_list[-1].split(" ")
                if int(codes[0]) not in status_codes.keys():
                    continue
                status_codes[int(codes[0])] += 1
                print_counter += 1
                size_summation += int(codes[1])
                if print_counter % 10 == 0:
                    print_logs()
            except():
                pass
        print_logs()
    except KeyboardInterrupt:
        print_logs()
        raise
