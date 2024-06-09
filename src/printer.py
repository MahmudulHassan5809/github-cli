import csv
import sys
from typing import Any

from constants import (  # Assuming OutputFormat is defined in constants module
    OutputFormat,
)
from rich import console, print_json, table


class DataPrinter:
    def __init__(self, data: list[dict[Any, Any]]) -> None:
        self.data = data

    def print_csv(self) -> None:
        headers = self.data[0].keys()
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        writer.writerows(self.data)

    def print_json(self) -> None:
        print_json(data=self.data)

    def print_table(self) -> None:
        tbl = table.Table()
        headers = self.data[0].keys()
        tbl.add_column("")
        for h in headers:
            tbl.add_column(str(h), justify="right", style="cyan", no_wrap=True)

        for index, repo in enumerate(self.data, start=1):
            tbl.add_row(str(index), *[str(r) for r in repo.values()])

        cnsl = console.Console()
        cnsl.print(tbl)

    def print_beauty(self, output: OutputFormat) -> None:
        output_functions = {
            OutputFormat.CSV: self.print_csv,
            OutputFormat.JSON: self.print_json,
            OutputFormat.TABLE: self.print_table,
        }

        output_function = output_functions.get(output)
        if output_function:
            output_function()
        else:
            raise ValueError(f"Unsupported output format: {output}")
