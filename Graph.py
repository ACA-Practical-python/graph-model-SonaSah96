import copy


class Node:
    def __init__(self, vertex_id):
        self.vertex_id = vertex_id


class Graph:
    def __init__(self):
        self.edge_dict = {}
        self.vertex_dict = {}
        self.neighbours_dict = {}

    def add_vertex(self, i):
        if i not in self.vertex_dict.keys():
            self.vertex_dict[i] = Node(i)
            self.neighbours_dict[i] = set()
        else:
            raise Exception("The Graph already has a vertex with this id")

    def delete_vertex(self, i):
        if i not in self.vertex_dict.keys():
            raise Exception("The Graph does not have a vertex with that id")
        else:
            self.vertex_dict.pop(i)
            self.neighbours_dict.pop(i)
            new_dict = copy.deepcopy(self.edge_dict)
            for key in new_dict:
                if i in key:
                    self.edge_dict.pop(key)
            for val in self.neighbours_dict.values():
                if i in val:
                    val.remove(i)

    def add_edge(self, i, j, weight=0):
        # noinspection PyBroadException
        try:
            self.add_vertex(i)
        except Exception:
            pass
        # noinspection PyBroadException
        try:
            self.add_vertex(j)
        except Exception:
            pass
        if (i, j) in self.edge_dict.keys() or (j, i) in self.edge_dict.keys():
            raise Exception("The Graph already has an edge with these vertexes")
        self.edge_dict[(i, j)] = weight
        for key, val in self.neighbours_dict.items():
            if key == i:
                val.add(j)
            elif key == j:
                val.add(i)
            else:
                continue

    def __contains__(self, graph_2):
        if not isinstance(graph_2, Graph):
            raise Exception("Graph type is expected")
        if not self.neighbours_dict.keys() >= graph_2.neighbours_dict.keys():
            return False
        for key in graph_2.neighbours_dict.keys():
            if not self.neighbours_dict[key] >= graph_2.neighbours_dict[key]:
                return False
        return True




