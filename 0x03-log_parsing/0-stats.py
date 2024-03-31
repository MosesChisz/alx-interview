#!/usr/bin/env python3

import sys
import signal

# Define variables to store metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Signal handler for keyboard interruption
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Function to print statistics
def print_statistics():
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
for line in sys.stdin:
    line = line.strip()
    
    # Split the line by space
    parts = line.split()
    
    # Check if the line matches the expected format
    if len(parts) == 7:
        ip_address, date, request, status_code_str, file_size_str = parts
        if request == "GET" and file_size_str.isdigit():
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            
            # Update metrics
            total_file_size += file_size
            status_code_count[status_code] += 1
            line_count += 1
            
            # Check if it's time to print statistics
            if line_count % 10 == 0:
                print_statistics()
    else:
        continue
