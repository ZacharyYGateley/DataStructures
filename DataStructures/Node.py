

class Node:
    key = None

    def __init__(self, key=None, **kwargs):
        """
        Initialize with kwargs for each object variable
        :param **kwargs: key, Node parent, Node left, Node right
        """
        self.key = kwargs.get('key')

    @classmethod
    def or_none(cls, func):
        """
        Decorator for node setting
        If the passed value is Node,
        pass that value to the original function
        Otherwise, pass None to the original function
        :param cls: class name, can override
        :param func: decorating function
        :returns: decorator that calls function with (Node object || None)
        """

        def inner(obj, potential_node, *args, **kwargs):
            # Get Node object or None
            node = None
            if isinstance(cls, potential_node):
                print ('Is instance of', cls.__name__)
                node = potential_node

            # Call function with appropriate arguments
            if args is not None:
                if kwargs is not None:
                    return func(node, *args, **kwargs)
                else:
                    return func(node, *args)
            elif kwargs is not None:
                return func(node, **kwargs)
            else:
                return func(node)

        return inner

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key
