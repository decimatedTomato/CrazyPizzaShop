from collections.abc import Iterable
from itertools import combinations
from pprint import pprint

from networkx import Graph, convert_node_labels_to_integers

from src.customer import Customer


def maximum_independent_set(customers: Iterable[Customer]) -> Graph:
    """
    Returns the maximum independent set of customers in the given list of customers

    Function should return the largest set of customers with no internal conflicts
    """

    new_graph: Graph = Graph()
    new_graph.add_nodes_from(customers)

    return new_graph


def main():
    customers = [
        Customer(("lobster", "tomato"), ("cheese", "potato")),
        Customer(("cheese", "tomato"), ("shrimp",)),
        Customer(("shrimp", "potato"), ("egg",)),
    ]

    result: Graph = maximum_independent_set(customers)
    pprint([*result.nodes.data()])

    pprint(result.nodes[1])


if __name__ == "__main__":
    main()
