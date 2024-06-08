import os

import typer
from dotenv import load_dotenv
from github import GitHubAPI

# from rich import print

if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()

repo_app = typer.Typer()

app.add_typer(repo_app, name="repo")


@repo_app.command("list", help="list user repositories")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github username")
) -> None:
    GitHubAPI(username=user).get_user_repositories()
    # print(repo)


if __name__ == "__main__":
    app()
