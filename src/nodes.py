from collections.abc import Iterable
from pprint import pprint

from networkx import Graph, convert_node_labels_to_integers

from src.customer import Customer


def maximum_independent_set(customers: Iterable[Customer]):
    """
    Returns the maximum independent set of customers in the given list of customers.
    """
    new_graph: Graph = Graph()
    new_graph.add_nodes_from(customers)
    pprint(new_graph.nodes)

    new_graph = convert_node_labels_to_integers(new_graph)
    pprint(new_graph.nodes)


def main():
    """
    Main function.
    """
    customers = [
        Customer(("lobster", "tomato"), ("cheese", "potato")),
        Customer(("cheese", "tomato"), ("shrimp",)),
        Customer(("shrimp", "potato"), ("egg",)),
    ]
    maximum_independent_set(customers)


if __name__ == "__main__":
    main()
