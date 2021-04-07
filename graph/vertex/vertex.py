from abc import abstractmethod


class VertexInterface:
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set(self, value, edges):
        pass

    @abstractmethod
    def get_vertex(self, edge):
        pass

    @abstractmethod
    def get_edges(self):
        pass

    @abstractmethod
    def add_edge(self, edge, vertex):
        pass
