import networkx as nx

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.minimum_cut.html#networkx.algorithms.flow.minimum_cut


class Day25:
    def __init__(self, data):
        self.data = data
        self.components = {
            component.strip(): others.strip().split(" ")
            for component, others in [line.split(":") for line in self.data]
        }

    def solve_part_one(self):
        graph = nx.Graph()
        for component, others in self.components.items():
            for other in others:
                graph.add_edge(component, other, capacity=1)

        print(graph.nodes)
        print(graph.edges)
        partition_counts = []
        for edge in graph.edges:
            # print(edge)
            cut_value, partition = nx.minimum_cut(graph, edge[0], edge[1])
            if cut_value == 3 and len(partition) == 2:
                print(cut_value)
                print(partition)
                counts = [len(x) for x in partition]
                partition_counts = counts
                print(counts)
                break

        print(graph)
        return partition_counts[0] * partition_counts[1]

    def solve_part_two(self):
        pass
