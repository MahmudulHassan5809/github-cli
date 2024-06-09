# GitHub CLI Tool

This is a command-line tool to interact with GitHub using the GitHub API. It allows you to list and delete repositories, fetch user profiles, and more.

## Features

- List user repositories.
- Delete a user repository.
- List user profile, including repository count, followers count, and following count.
- Supports multiple output formats (JSON, CSV, TABLE).

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- GitHub Personal Access Token

### Steps

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/github-cli-tool.git
    cd github-cli-tool
    ```

2. Install the required packages:

    ```sh
    poetry install
    ```

3. (Optional) Create a `.env` file in the project root to store your GitHub token:

    ```sh
    touch .env
    ```

    Add the following line to the `.env` file:

    ```sh
    GITHUB_TOKEN=your_github_token
    ```

## Usage

### Commands

This tool provides several commands through the CLI. Below are some examples:

#### List User Repositories

Lists all repositories for a specified user.

```sh
python main.py repo list -u <username> -o <output_format> -q <jmespath_query> -s <sort_keys>
```

- `-u` or `--user`: GitHub username (required)
- `-o` or `--output`: Output format (json, csv, table) (default: json)
- `-q` or `--query`: JMESPath query for filtering results (optional)
- `-s` or `--sort_by`: Keys to sort the results by, prefix with `~` for descending (optional)

#### Delete User Repository

Deletes a specified repository for a user.

```sh
python main.py repo delete -u <username> -r <repository_name>
```

- `-u` or `--user`: GitHub username (required)
- `-r` or `--repo`: Repository name to delete (required)

#### List User Profile

Displays a user's profile information including repository count, followers count, and following count.

```sh
python main.py user profile -u <username>
```

- `-u` or `--user`: GitHub username (required)

### Example Usage

List repositories in JSON format:

```sh
python main.py repo list -u your_username -o json
```

Delete a repository:

```sh
python main.py repo delete -u your_username -r repo_name
```

List user profile:

```sh
python main.py user profile -u your_username
```

## Configuration

### Environment Variables

The application can be configured using environment variables:

- `GITHUB_TOKEN`: Your GitHub Personal Access Token

You can set these variables in a `.env` file at the root of the project.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyGithub](https://github.com/PyGithub/PyGithub)
- [requests](https://requests.readthedocs.io/)
- [Typer](https://typer.tiangolo.com/)

---

### Additional Notes

- Ensure you replace `"yourusername"` and `"your_github_token"` with your actual GitHub username and personal access token in the provided examples.
- The structure of the README aims to cover the most critical aspects of your project: installation, usage, configuration, and contribution guidelines.
- Make sure to adjust paths and other specific details according to your actual project setup.
