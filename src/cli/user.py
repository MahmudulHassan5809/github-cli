import typer

from src.constants import OutputFormat
from src.github import GitHubAPI
from src.printer import DataPrinter

user_app = typer.Typer()


@user_app.command("profile", help="list user profile")
def list_repos(
    user: str = typer.Option(..., "--user", "-u", help="github username"),
) -> None:
    github_api = GitHubAPI(username=user)
    repos = github_api.get_user_repositories()
    followers = github_api.get_github_user_followers_count()
    following = github_api.get_github_user_following_count()

    profile = {
        "repositories": len(repos) if repos else 0,
        "followers": followers,
        "following": following,
    }

    printer = DataPrinter(data=[profile])
    printer.print_beauty(output=OutputFormat.TABLE)
