import pytest


@pytest.fixture
def sample_repo_response():
    return {
        "full_name": "owner/repo",
        "description": "A repo",
        "stargazers_count": 42,
        "default_branch": "main",
        "topics": ["python", "github", "api"],
    }
