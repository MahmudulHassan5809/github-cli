import csv
import sys
from constants import OutputFormat


def print_beauty(data: list[dict], output: OutputFormat):
    if output == OutputFormat.CSV:
        headers = data[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)