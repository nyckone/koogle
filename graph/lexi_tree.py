from graph.vertex.top_searches_vertex import TopSearchesVertex
from graph.tree import TreeInterface


class LexiTree(TreeInterface):
    def __init__(self, phrases_list=None):
        self.__tree_head = TopSearchesVertex()

        if phrases_list:
            for phrase in phrases_list:
                self.create_phrase(phrase, 0)

    def do_action_on_traverse(self, phrase, action):
        if self.get_node(phrase) is None:
            raise ValueError("No such phrase to traverse!")

        vertex_iterator = self.__tree_head
        action(vertex_iterator)

        for letter in phrase:
            vertex_iterator = vertex_iterator.get_vertex(letter)
            action(vertex_iterator)

    def get_node(self, phrase):
        vertex_iterator = self.__tree_head

        for letter in phrase:
            current_vertex = vertex_iterator.get_vertex(letter)
            if current_vertex is None:
                raise ValueError("No such phrase to traverse!")

            vertex_iterator = current_vertex

        return vertex_iterator

    def create_phrase(self, phrase, counter):
        vertex_iterator = self.__tree_head
        current_word = ""

        for letter in phrase:
            current_word += letter
            current_vertex = vertex_iterator.get_vertex(letter)
            if current_vertex is None:
                current_vertex = TopSearchesVertex(current_word, counter=counter)
                vertex_iterator.add_edge(letter, current_vertex)

            vertex_iterator = current_vertex

        return vertex_iterator
