from dataclasses import dataclass, field


@dataclass
class Repository:
    full_name: str
    description: str
    stargazers_count: int
    default_branch: str
    topics: list[str] = field(default_factory=list)

    def summarize(self) -> str:
        topic_delimeter = ", "
        topics = topic_delimeter.join(self.topics)
        return f"Repository: {self.full_name}\nDescription: {self.description}\nStars: {self.stargazers_count}\nDefault Branch: {self.default_branch}\nTopics: {topics}"
