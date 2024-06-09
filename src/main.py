import os

import jmespath
import typer
from constants import OutputFormat
from dotenv import load_dotenv
from github import GitHubAPI
from printer import DataPrinter

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
    sort_by: str = typer.Option(None, "--sort", "-s", help="Sort by keys"),
) -> None:
    repos = GitHubAPI(username=user).get_user_repositories()
    if query:
        repos = jmespath.search(query, repos)
    if sort_by:
        expr = f"sort_by(@, &{sort_by}).reverse(@)"
        repos = jmespath.search(expr, repos)
    if repos:
        printer = DataPrinter(data=repos)
        printer.print_beauty(output=output)


if __name__ == "__main__":
    app()
