from graph.vertex.vertex import VertexInterface


class TopSearchesVertex(VertexInterface):
    def __init__(self, word_value=None, counter=0, edges=None, top_searches=None):
        self.__word_value = word_value
        self.__edges = edges
        self.__counter = counter

        if edges is None:
            self.__edges = dict()
        else:
            self.__edges = top_searches

        if top_searches is None:
            self.__top_searches = dict()
        else:
            self.__top_searches = top_searches

    def get_value(self):
        return self.__word_value

    def set(self, value, data=None, edges=None):
        self.__word_value = value
        self.__top_searches = data
        self.__edges = edges

    def add_edge(self, edge, vertex):
        if edge not in self.__edges:
            self.__edges[edge] = vertex

    def get_edges(self):
        return self.__edges

    def raise_and_get_counter(self):
        self.__counter = self.__counter + 1
        return self.__counter

    def get_top_searches(self):
        return self.__top_searches

    def get_vertex(self, edge):
        if edge in self.__edges:
            return self.__edges[edge]

        return None
