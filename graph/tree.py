from abc import abstractmethod


class TreeInterface:
    @abstractmethod
    def get_node(self, phrase):
        pass

    @abstractmethod
    def do_action_on_traverse(self, phrase, action):
        pass
