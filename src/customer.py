from dataclasses import dataclass


@dataclass
class Customer:
    loves: tuple[str, ...]
    dislikes: tuple[str, ...]

    def conflict_exists(self, other) -> bool:
        return any(dislike in other.loves for dislike in self.dislikes)
