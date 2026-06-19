import pytest


def test_build_repo_details_maps_fields():
    pass


def test_print_repo_details_with_json():
    pass


def test_print_repo_details_with_class():
    pass


def test_build_client_includes_auth_header_when_token_set():
    pass


def test_build_client_omits_auth_header_when_no_token_set():
    pass


def test_fetch_returns_dict_on_success():
    pass


def test_fetch_raises_repository_not_found_on_404():
    pass


def test_fetch_raises_error_on_other_http_errors():
    pass


@pytest.mark.parametrize("use_json", [True, False])
def test_print_repo_stats_prints_correctly_on_success(use_json):
    pass


def test_print_repo_stats_logs_error_on_failure():
    pass


@pytest.fixture
def sample_repo_response():
    return {
        "full_name": "owner/repo",
        "description": "A repo",
        "stargazers_count": 42,
        "default_branch": "main",
        "topics": ["python", "github", "api"],
    }
