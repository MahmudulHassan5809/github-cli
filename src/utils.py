import csv
import sys
from typing import Any

from constants import OutputFormat
from rich import print_json


def print_beauty(data: list[dict[Any, Any]], output: OutputFormat) -> None:
    if output == OutputFormat.CSV:
        headers = data[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    elif output == OutputFormat.JSON:
        print_json(data=data)
