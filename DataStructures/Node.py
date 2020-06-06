

class Node:
    """
    Very basic ADT of a node
    Designed to be inherited for more interesting ADTs
    """
    key = 0

    @classmethod
    def or_none(cls, node):
        """
        Verify passed node is a member of this class
        Return either the node or None
        :param node: node in question
        :return: Node object || None
        """
        return node if isinstance(node, cls) else None

    def __init__(self, key):
        """
        Initialize with kwargs for each object variable
        :param key: key value for new node
        """
        self.key = key

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
