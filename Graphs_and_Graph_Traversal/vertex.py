"""An instance of Vertex will store data and
a Python dictionary which tracks other Vertex
instances connected to self"""


class Vertex:
    def __init__(self, value):
        self.value = value
        """A key in the Vertex instance’s edges dictionary 
        represents a connection to that other vertex"""
        self.edges = {}

    def get_edges(self):
        return list(self.edges.keys())

    def add_edge(self, vertex, weight=0):
        # vertex here is a value
        # print("Adding edge to {}".format(vertex))
        self.edges[vertex] = weight


# grand_central = Vertex('Grand Central Station')
# forty_second_street = Vertex('42nd Street Station')
#
# print(grand_central.get_edges())

# call .add_edge() below here
# grand_central.add_edge(forty_second_street.value)
