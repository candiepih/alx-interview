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


def get_status_and_size(string):
    """
    Gets string of codes and size to list

    Args:
        string (str): string of integers delimited by space

    Returns:
        list of the integers
    """
    codes_list = string.split(" ")[1:]
    return codes_list


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
    parsed_codes = get_status_and_size(input_list[3])
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
    for k, v in status_codes.items():
        if v == 0:
            continue
        print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            log_list = split_line(line)
            if found_errors(log_list):
                continue
            codes = get_status_and_size(log_list[3])
            size_summation += int(codes[1])
            if print_counter % 10 == 0 and print_counter != 0:
                print_logs()
            print_counter += 1
    except():
        print_logs()
