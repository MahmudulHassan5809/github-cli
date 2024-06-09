import os

import typer
from constants import OutputFormat
from dotenv import load_dotenv
from github import GitHubAPI
from utils import print_beauty

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
) -> None:
    repos = GitHubAPI(username=user).get_user_repositories()
    print_beauty(data=repos, output=output)


if __name__ == "__main__":
    app()
