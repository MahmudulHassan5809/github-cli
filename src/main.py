import os

import jmespath
import typer
from constants import OutputFormat
from dotenv import load_dotenv
from github import GitHubAPI
from printer import DataPrinter
from utils import sort_by_key

if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command("list", help="list user repositories")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github username"),
    output: OutputFormat = typer.Option(
        OutputFormat.JSON, "--output", "-o", help="output format"
    ),
    query: str = typer.Option(None, "--query", "-q", help="Query with jmespath"),
    sort_by: str = typer.Option(None, "--sort_by", "-s", help="Sort by keys"),
) -> None:
    repos = GitHubAPI(username=user).get_user_repositories()
    if query:
        repos = jmespath.search(query, repos)
    if sort_by:
        if sort_by.startswith("~"):
            reverse = True
            sort_by = sort_by[1:]
        else:
            reverse = False

        sort_by_list = sort_by.split(",")
        repos = sort_by_key(
            data=repos,
            key_list=sort_by_list,
            reverse=reverse,
        )
    if repos:
        printer = DataPrinter(data=repos)
        printer.print_beauty(output=output)


if __name__ == "__main__":
    app()
