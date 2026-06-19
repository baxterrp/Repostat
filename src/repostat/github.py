import json as json_lib
import logging
import os
from typing import Any

import httpx
import typer

from repostat.exceptions import RepositoryNotFoundError
from repostat.models import Repository

logger = logging.getLogger(__name__)


def fetch(client: httpx.Client, owner: str, repo_name: str) -> dict[str, Any]:
    logger.info("Fetching repository info for %s/%s", owner, repo_name)
    url = f"https://api.github.com/repos/{owner}/{repo_name}"

    try:
        return client.get(url).raise_for_status().json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            raise RepositoryNotFoundError(owner, repo_name) from e
        raise


def print_repository_stats(owner: str, repo_name: str, use_json: bool) -> None:
    try:
        with _build_client() as client:
            repo_info = fetch(client, owner, repo_name)

        _print_repo_details(repo_info, use_json)
    except RepositoryNotFoundError as e:
        logger.error(e)
        raise typer.Exit(1)
    except httpx.HTTPError as e:
        logger.error(
            "Error fetching repository info for %s/%s: %s", owner, repo_name, e
        )
        raise typer.Exit(1)
    except (KeyError, json_lib.JSONDecodeError) as e:
        logger.error(
            "Missing key in repository info for %s/%s: %s", owner, repo_name, e
        )
        raise typer.Exit(1)
    except Exception as e:
        logger.error("Unexpected error for %s/%s: %s", owner, repo_name, e)
        raise typer.Exit(1)


def _build_client() -> httpx.Client:
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return httpx.Client(headers=headers)


def _build_repo_details(repo_info: dict[str, Any]) -> Repository:
    return Repository(
        full_name=repo_info["full_name"],
        description=repo_info["description"],
        stargazers_count=repo_info["stargazers_count"],
        default_branch=repo_info["default_branch"],
        topics=repo_info.get("topics", []),
    )


def _print_repo_details(repo_info: dict[str, Any], json: bool) -> None:
    rep = _build_repo_details(repo_info)
    response = repo_info if json else rep.summarize()
    print(response)
