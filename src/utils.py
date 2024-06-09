import csv
import sys
from typing import Any

from constants import OutputFormat
from rich import console, print_json, table


def print_beauty(data: list[dict[Any, Any]], output: OutputFormat) -> None:
    if output == OutputFormat.CSV:
        headers = data[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
    elif output == OutputFormat.JSON:
        print_json(data=data)
    elif output == OutputFormat.TABLE:
        tbl = table.Table()
        headers = data[0].keys()
        tbl.add_column("")
        for h in headers:
            tbl.add_column(str(h), justify="right", style="cyan", no_wrap=True)

        for repo in data:

            tbl.add_row(*[str(data.index(repo) + 1)] + [str(r) for r in repo.values()])

        cnsl = console.Console()
        cnsl.print(tbl)
