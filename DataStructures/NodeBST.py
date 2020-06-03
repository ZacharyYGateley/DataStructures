from DataStructures import Node


class NodeBST(Node):
    parent = None
    left = None
    right = None

    def __init__(self, key = None, **kwargs):
        """
        Initialize with kwargs for each object variable
        :param **kwargs: key, Node parent, Node left, Node right
        """
        super().__init__()

        def get_node_from_kwargs(kw):
            potential_node = kwargs.get(kw)
            if isinstance(Node, potential_node):
                return potential_node
            else:
                return None

        self.parent = get_node_from_kwargs('parent')
        self.left = get_node_from_kwargs('left')
        self.right = get_node_from_kwargs('right')

    @classmethod
    def or_none(cls, func):
        """
        Decorator
        Verify passed parameter to func is a member of NodeBST
        Overrides Node.or_none
        :param func: decorating function
        :return: decorated function with parameter (Node object || None)
        """
        return super().or_None(cls, func)

    def get_parent(self):
        """
        Return parent node (None if not set)
        :return: parent node
        """
        return self.parent

    def get_left(self):
        """
        Return left child node (None if not set)
        :return: left child node
        """
        return self.left

    def get_right(self):
        """
        Return right child node (None if not set)
        :return: right child node
        """
        return self.right

    @or_none
    def set_parent(self, node):
        """
        Set parent to passed node if valid
        :param node: new parent node
        :return: no return value
        """
        self.parent = node

    @or_none
    def set_left(self, node):
        """
        Set left child to passed node if valid
        :param node: new left child node
        :return: no return value
        """
        self.left = node

    @or_none
    def set_right(self, node):
        """
        Set right child to passed node if valid
        :param node: new right child node
        :return: no return value
        """
        self.right = node

    @or_none
    def is_left_child(self):
        """
        Return boolean is node left child of parent
        :return: boolean is node left child of parent
        """
        is_left_child = False
        parent = self.get_parent()
        if parent is not None:
            is_left_child = parent.get_left() == self

        return is_left_child

    @or_none
    def is_right_child(self):
        """
        Return boolean is node right child of parent
        :param node: node in question
        :return: boolean is node right child of parent
        """
        is_right_child = False
        parent = self.get_parent()
        if parent is not None:
            is_right_child = parent.get_right() == self

        return is_right_child

    @or_none
    def remove_as_subtree(self):
        """
        Remove subtree rooted at self out of its tree
        :return: self
        """
        parent = self.get_parent()
        if parent is not None:
            if self.is_left_child():
                parent.set_left(None)
            else:
                parent.set_right(None)

        return self

    @or_none
    def replace_with(self, replacement):
        """
        Replace self with replacement in self's tree
        :param replacement: NodeBST replacement node
        :return: replacement node
        """
        # Do not proceed if replacement is invalid
        if replacement is None:
            return None
        # Nothing to do if replacing node with itself
        if replacement == self:
            return self

        # Link parent
        parent = self.get_parent()
        if parent is not None:
            if self.is_left_child():
                parent.set_left(replacement)
            else:
                parent.set_right(replacement)

        # Link left
        left = self.get_left()
        # Prevent infinite loops
        if left is not replacement:
            replacement.set_left(left)

        # Link right
        right = self.get_right()
        # Prevent infinite loops
        if right is not replacement:
            replacement.set_right(right)

        # Delete node
        self.set_parent(None)
        self.set_left(None)
        self.set_right(None)
