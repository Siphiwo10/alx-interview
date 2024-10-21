#!/usr/bin/python3
"""adding collectios of stats"""


from collections import defaultdict


total_size = 0
line_count = 0
status_counts = defaultdict(int)  # Store counts for each status code

def print_stats():
  global total_size, line_count, status_counts
  print(f"File size: {total_size}")
  sorted_status_counts = sorted(status_counts.items())
  for status_code, count in sorted_status_counts:
    print(f"{status_code}: {count}")
  line_count = 0
  total_size = 0
  status_counts.clear()

try:
  for line in sys.stdin:
    # Split line and extract information
    try:
      ip, date, _, _, status_code, file_size = line.strip().split()
      status_code = int(status_code)
      file_size = int(file_size)
    except ValueError:
      # Skip lines with invalid format
      continue

    # Update counters
    total_size += file_size
    status_counts[status_code] += 1
    line_count += 1

    # Print stats after every 10 lines or on keyboard interrupt
    if line_count % 10 == 0 or line_count == 1:
      print_stats()

except KeyboardInterrupt:
  # Print stats on keyboard interrupt
  print_stats()
