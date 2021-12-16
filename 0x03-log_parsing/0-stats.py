#!/usr/bin/python3
"""
"""
import sys
import re


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
print_counter = 0
size_sumation = 0


def get_status_and_size(string):
    """
    Gets string of codes and size to list

    Args:
        string (str): string of integers delimited by space

    Returns:
        list of the integers
    """
    l = string.split(" ")[1:]
    return l


def split_line(line):
    """
    Creates a list from a line with delimeters

    Args:
        line (str): string to split

    Returns: list of strings delimited
    """
    line = line.replace("\n", "")
    l = re.split('- |"|"| " " ', str(line))
    return l


def found_errors(input_list):
    """
    Test the inputs in array for errors

    Args:
        input_list (list): list of inputs to test

    Returns: (1) if error found and (0) otherwise
    """
    if len(input_list) != 4:
        return 1
    codes = get_status_and_size(input_list[3])
    try:
        if int(codes[0]) not in status_codes.keys() or codes[0] == "":
            return 1
        status_codes[int(codes[0])] += 1
        for code in codes:
            code = int(code)
            if type(code) != int:
                return 1
    except:
        return 1
    return 0


def print_logs():
    """
    Prints status codes to the logs
    Returns:
        None
    """
    for k, v in status_codes.items():
        if v == 0:
            continue
        print("{}: {}".format(k, v))
    print("File size: {}".format(size_sumation))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            log_list = split_line(line)
            if found_errors(log_list):
                continue
            codes = get_status_and_size(log_list[3])
            size_sumation += int(codes[1])
            if print_counter % 10 == 0 and print_counter != 0:
                print_logs()
            print_counter += 1
    except:
        print_logs()