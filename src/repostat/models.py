from dataclasses import dataclass, field


@dataclass
class Repository:
    full_name: str
    description: str
    stargazers_count: int
    default_branch: str
    topics: list[str] = field(default_factory=list)

    def summarize(self) -> str:
        return (
            f"Repository: {self.full_name}\n"
            f"Description: {self.description}\n"
            f"Stars: {self.stargazers_count}\n"
            f"Default Branch: {self.default_branch}\n"
            f"Topics: {', '.join(self.topics)}"
        )
