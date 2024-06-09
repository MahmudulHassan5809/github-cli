import logging

import jmespath
import typer

from src.constants import OutputFormat
from src.github import GitHubAPI
from src.printer import DataPrinter
from src.utils import sort_by_key

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

repo_app = typer.Typer()


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


@repo_app.command(name="delete", help="delete user repository")
def delete_repo(
    user: str = typer.Option(..., "--user", "-u", help="github user name"),
    repo: str = typer.Option(..., "--repo", "-r", help="repo name"),
) -> None:
    if GitHubAPI(username=user).delete_user_repository(repo_name=repo):
        logger.info(f"{repo} deleted successfully.")
    else:
        logger.info(f"failed to delete repository {repo}.")
