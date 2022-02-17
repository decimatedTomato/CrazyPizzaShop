from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Customer:
    loves: Iterable[str]
    dislikes: Iterable[str]

    def conflict_exists(self, other) -> bool:
        """
        Returns True if there is a conflict between the two customers

        To be precise, return True if one likes something the other dislikes
        """

        return not set(self.loves).isdisjoint(other.dislikes)


def common_loves(customers: Iterable[Customer]) -> set[str]:
    """
    Returns set of ingredients that are in common between all customers
    """

    result: set[str] = set()
    for customer in customers:
        result.intersection_update(customer.loves)

    return result
