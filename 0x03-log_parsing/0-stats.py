#!/usr/bin/python3
"""
This module contains the function that displays the
stats from the standard input
"""
import sys
import re


status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
print_counter = 0
size_summation = 0


def split_line(std_line):
    """
    Creates a list from a line with delimiters

    Args:
        std_line (str): string to split

    Returns: list of strings delimited
    """
    std_line = std_line.replace("\n", "")
    parsed_data = re.split('- | "|" | " " ', str(std_line))
    return parsed_data


def found_errors(input_list):
    """
    Test the inputs in array for errors

    Args:
        input_list (list): list of inputs to test

    Returns: (1) if error found and (0) otherwise
    """
    if len(input_list) != 4:
        return 1
    parsed_codes = input_list[3].split(" ")
    try:
        if int(parsed_codes[0]) not in status_codes.keys()\
                or parsed_codes[0] == "":
            return 1
        status_codes[int(parsed_codes[0])] += 1
        for code in parsed_codes:
            code = int(code)
            if type(code) != int:
                return 1
    except():
        return 1
    return 0


def print_logs():
    """
    Prints status codes to the logs
    Returns:
        None
    """
    print("File size: {}".format(size_summation))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        log_list = split_line(line)
        if found_errors(log_list):
            continue
        codes = log_list[3].split(" ")
        size_summation += int(codes[1])
        if print_counter % 10 == 0 and print_counter != 0:
            print_logs()
        print_counter += 1
except():
    print_logs()
    raise
