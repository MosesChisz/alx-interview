#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
"""

import sys


def get_line(line):
    """
    Parse a log entry and update the status code counts.
    """
    try:
        parsed_line = line.split()
        status_code = parsed_line[-2]
        if status_code in status:
            status[status_code] += 1
        return int(parsed_line[-1])
    except Exception:
        return 0


def print_stats():
    """
    Print statistics based on the total file size
    and status code counts.
    """
    print("File size: {}".format(file_size))
    for key in sorted(status):
        if status[key]:
            print("{}: {}".format(key, status[key]))


if __name__ == "__main__":
    # Initialize status code counts, line count, and total file size
    status = {"200": 0,
              "301": 0,
              "400": 0,
              "401": 0,
              "403": 0,
              "404": 0,
              "405": 0,
              "500": 0}
    count = 1
    file_size = 0

    try:
        # Process log entries from stdin
        for line in sys.stdin:
            file_size += get_line(line)
            # Print statistics after every 10 lines
            if count % 10 == 0:
                print_stats()
            count += 1
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully, print final statistics before exiting
        print_stats()
        raise
    print_stats()
