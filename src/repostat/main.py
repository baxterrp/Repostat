from typing import Any
from models import Repository

import httpx


def get_repo(owner: str, repo_name: str) -> dict[str, Any]:
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def main():
    owner = "baxterrp"
    repo_name = "repostat"
    repo_info = get_repo(owner, repo_name)
    rep = Repository(
        full_name=repo_info["full_name"],
        description=repo_info["description"],
        stargazers_count=repo_info["stargazers_count"],
        default_branch=repo_info["default_branch"],
        topics=repo_info.get("topics", []),
    )

    print(rep.summarize())


if __name__ == "__main__":
    main()
