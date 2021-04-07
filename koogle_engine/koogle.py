from graph.lexi_tree import LexiTree
from functools import partial


class Koogle(object):
    __COUNTER_POSITION = 1
    __MAX_SUGGESTION_LIMIT = 10

    def __init__(self, lexi_tree=None):
        if lexi_tree:
            self.__lexi_tree = lexi_tree

        else:
            self.__lexi_tree = LexiTree()

    def suggest(self, phrase):
        return self.__lexi_tree.get_node(phrase).get_top_searches()

    def search(self, phrase):
        try:
            current_vertex = self.__lexi_tree.get_node(phrase)
        except ValueError:
            current_vertex = self.__lexi_tree.create_phrase(phrase, 0)

        new_counter = current_vertex.raise_and_get_counter()

        partial_vertex_accepting_func = partial(self.enter_vertex_to_top_search_if_needed, phrase, new_counter)

        self.__lexi_tree.do_action_on_traverse(phrase, partial_vertex_accepting_func)

    def __increase_data_counter(self, phrase, new_counter):
        pass

    def enter_vertex_to_top_search_if_needed(self, phrase, counter, vertex):
        top_searches = vertex.get_top_searches()
        if phrase in top_searches:
            top_searches[phrase] = counter
            return

        if len(top_searches) < self.__MAX_SUGGESTION_LIMIT:
            top_searches[phrase] = counter

        (word, min_counter) = min(top_searches.items(), key=lambda x: x[self.__COUNTER_POSITION])
        if counter > min_counter:
            del (top_searches[word])
            top_searches[phrase] = counter
