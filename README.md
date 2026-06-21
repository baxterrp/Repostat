# repostat

A typed Python CLI that fetches public GitHub repository metadata and prints a clean summary or structured JSON. Built as the foundation of a regulated-document AI platform — the same skeleton (CLI, HTTP client, typed models, error handling, tests) runs through every project in the series.

## Usage

```
uv run repostat <owner> <repo> [--json]
```

```
$ uv run repostat microsoft semantic-kernel

Repository: microsoft/semantic-kernel
Description: Integrate cutting-edge LLM technology quickly and easily into your apps
Stars: 23400
Default Branch: main
Topics: ai, azure, llm, openai, semantic-kernel
```

```
$ uv run repostat microsoft semantic-kernel --json

{
  "full_name": "microsoft/semantic-kernel",
  "description": "Integrate cutting-edge LLM technology quickly and easily into your apps",
  "stargazers_count": 23400,
  "default_branch": "main",
  "topics": ["ai", "azure", "llm", "openai", "semantic-kernel"]
}
```

## Auth

The GitHub public API allows ~60 unauthenticated requests/hour. Set `GITHUB_TOKEN` to raise the limit to 5000/hour:

```
# .env
GITHUB_TOKEN=your_token_here
```

The tool works without a token — rate-limited but functional.

## Setup

```
uv sync
uv run repostat --help
```

## Development

```
uv run pytest          # run tests
uv run ruff check src  # lint
uv run pyright src     # type check
```

## Stack

- [httpx](https://www.python-httpx.org/) — async-capable HTTP client
- [typer](https://typer.tiangolo.com/) — type-hint-driven CLI
- [python-dotenv](https://pypi.org/project/python-dotenv/) — `.env` file loading
- [pytest](https://pytest.org/) + [respx](https://lundberg.github.io/respx/) — testing with mocked HTTP

## Part of a series

repostat is project 0 of 6 in a regulated-document AI platform:

| Project | What it adds |
|---------|-------------|
| **repostat** | Python language fundamentals: CLI, REST, typed models, error handling, secrets, tests |
| askdocs | LLM SDK, streaming, naive RAG, multi-provider |
| agentcli | Tool-calling agents, memory, asyncio, MCP |
| ragservice | FastAPI, embeddings, vector + hybrid search, citations, PII handling |
| extractor | Document intelligence, vision, batch processing, structured validation |
| evalkit | Evals, observability, cost tracking, tracing, Docker |
