def node_or_none(func):
    """
    Decorator for node setting
    If the passed value is Node,
    pass that value to the original function
    Otherwise, pass None to the original function
    """

    def inner(obj, potential_node):
        if isinstance(Node, potential_node):
            func(obj, potential_node)
        else:
            func(obj, None)

    return inner


class Node:
    key = None

    def __init__(self, key=None, **kwargs):
        """
        Initialize with kwargs for each object variable
        :param **kwargs: key, Node parent, Node left, Node right
        """
        self.key = kwargs.get('key')

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
