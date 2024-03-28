#!/usr/bin/python3
"""
Log stats module
"""
import sys
from operator import itemgetter

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    line_count = 0
    for line in sys.stdin:
        # Split the line into components
        parts = line.split()
        if len(parts) < 10:
            # Skip lines that don't match the expected format
            continue
        
        # Extract file size and status code
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print(f'Total file size: File size: {total_file_size}')
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f'{code}: {count}')

except KeyboardInterrupt:
    # If interrupted by CTRL + C, print the final statistics
    print(f'Total file size: File size: {total_file_size}')
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f'{code}: {count}')
