from DataStructures import Node


class BinaryNode(Node):
    tree    = None
    parent  = None
    left    = None
    right   = None

    @classmethod
    def or_none(cls, func):
        """
        Decorator
        Verify passed parameter to func is a member of NodeBST
        Overrides Node.or_none
        For class inheritance, if or_none is needed,
        you likely want to override this method to pass the subclass
        :param func: decorating function
        :return: decorated function with parameter (Node object || None)
        """
        return super().or_none(cls, func)

    def __init__(self, key, tree=None, parent=None, left=None, right=None):
        """
        Initialize with kwargs for each object variable
        :param key: key value for new node
        :param parent: BinaryNode parent of new new node
        :param left: BinaryNode left child of new node
        :param right: BinaryNode right child of new node
        """
        super().__init__(self, key)

        self.tree   = BinaryNode.or_none(tree)
        self.parent = BinaryNode.or_none(parent)
        self.left   = BinaryNode.or_none(left)
        self.right  = BinaryNode.or_none(right)

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
    def set_parent(self, new_parent):
        """
        Set parent to passed node if valid
        :param new_parent: new parent node
        :return: no return value
        """
        self.parent = new_parent

    @or_none
    def set_left(self, new_left_child):
        """
        Set left child to passed node if valid
        :param new_left_child: new left child node
        :return: no return value
        """
        self.left = new_left_child

    @or_none
    def set_right(self, new_right_child):
        """
        Set right child to passed node if valid
        :param new_right_child: new right child node
        :return: no return value
        """
        self.right = new_right_child

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
        Replace self subtree with replacement subtree
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