import os

import requests
from exceptions import RequestError
from requests.exceptions import RequestException


class GitHubAPI:
    def __init__(self, username: str):
        self.username = username
        self.base_url = "https://api.github.com"
        self.headers: dict | None = None
        if os.environ.get("GITHUB_TOKEN"):
            self.headers = {"Authorization": f"Bearer {os.environ.get('GITHUB_TOKEN')}"}
        else:
            self.headers = None

    def delete_user_repository(self, repo_name: str) -> bool:
        url = f"{self.base_url}/repos/{self.username}/{repo_name}"
        response = requests.delete(
            url=url,
            headers=self.headers,
        )
        return response.status_code == 204

    def get_user_repositories(self) -> list[dict[str, str]]:
        all_repos = []
        page = 1
        per_page = 100

        while True:
            url = f"{self.base_url}/users/{self.username}/repos"
            params = {"per_page": per_page, "page": page}
            try:
                response = requests.get(
                    url,
                    params=params,
                    headers=self.headers,
                )
                response.raise_for_status()
                repos = response.json()

                if not repos:
                    break

                for repo in repos:
                    all_repos.append(
                        {
                            "id": repo["id"],
                            "name": repo["name"][:5],
                            "url": repo["html_url"],
                            "description": str(repo["description"])[:5],
                            "language": repo["language"],
                            "stars": repo["stargazers_count"],
                            "forks": repo["forks_count"],
                            "fork": str(repo["fork"]),
                            "created_at": repo["created_at"],
                        },
                    )
                page += 1

            except RequestException as e:
                raise RequestError(f"Request error: {str(e)}")

        return all_repos
