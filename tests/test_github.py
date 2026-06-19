import pytest

import repostat.github as github


def test_build_repo_details_maps_fields(sample_repo_response):
    repo = github._build_repo_details(sample_repo_response)

    assert repo.full_name == "owner/repo"
    assert repo.description == "A repo"
    assert repo.stargazers_count == 42
    assert repo.default_branch == "main"
    assert repo.topics == ["python", "github", "api"]


def test_print_repo_details_with_json(sample_repo_response, capsys):
    expected = (
        "{\n"
        '  "full_name": "owner/repo",\n'
        '  "description": "A repo",\n'
        '  "stargazers_count": 42,\n'
        '  "default_branch": "main",\n'
        '  "topics": [\n'
        '    "python",\n'
        '    "github",\n'
        '    "api"\n'
        "  ]\n"
        "}\n"
    )
    github._print_repo_details(sample_repo_response, True)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_print_repo_details_with_class(sample_repo_response, capsys):
    expected = (
        "Repository: owner/repo\n"
        "Description: A repo\n"
        "Stars: 42\n"
        "Default Branch: main\n"
        "Topics: python, github, api\n"
    )

    github._print_repo_details(sample_repo_response, False)
    captured = capsys.readouterr()
    assert captured.out == expected


def test_build_client_includes_auth_header_when_token_set(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setenv("GITHUB_TOKEN", "test_token")
    client = github._build_client()

    assert "Authorization" in client.headers
    assert client.headers["Authorization"] == "Bearer test_token"


def test_build_client_omits_auth_header_when_no_token_set():
    client = github._build_client()
    assert "Authorization" not in client.headers


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
