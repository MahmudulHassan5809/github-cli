import os

import typer
from dotenv import load_dotenv

from src.cli.repo import repo_app
from src.cli.user import user_app

if os.path.isfile(".env"):
    load_dotenv()

app = typer.Typer()


app.add_typer(repo_app, name="repo", help="repository commands")
app.add_typer(user_app, name="user", help="user commands")


if __name__ == "__main__":
    app()
