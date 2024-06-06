import requests
from exceptions import RequestError
from requests.exceptions import RequestException


class GitHubAPI:
    def __init__(self, username: str):
        self.username = username
        self.base_url = "https://api.github.com"

    def get_user_repositories(self) -> list[dict[str, str]] | None:
        url = f"{self.base_url}/users/{self.username}/repos"
        try:
            response = requests.get(url)
            json_response = response.json()
            response.raise_for_status()
            return json_response
        except RequestException as e:
            raise RequestError(f"Request error: {str(e)}")
