from DataStructures.BinaryTree import BinaryTree
from DataStructures.Node import Node

class BinaryNode(Node):
    tree    = None
    parent  = None
    left    = None
    right   = None

    @classmethod
    def or_none(cls, node):
        """
        Verify passed node is a member of this class
        Return either the node or None
        :param node: node in question
        :return: BinaryNode object || None
        """
        return node if isinstance(node, cls) else None

    def __init__(self, key, tree=None, parent=None, left=None, right=None):
        """
        Initialize with kwargs for each object variable
        :param key: key value for new node
        :param parent: BinaryNode parent of new new node
        :param left: BinaryNode left child of new node
        :param right: BinaryNode right child of new node
        """
        super().__init__(key)

        self.tree   = tree if isinstance(tree, BinaryTree) else None
        self.parent = BinaryNode.or_none(parent)
        self.left   = BinaryNode.or_none(left)
        self.right  = BinaryNode.or_none(right)

    def get_parent(self):
        """
        Return parent node (None if not set)
        :return: parent node
        """
        return BinaryNode.or_none(self.parent)

    def get_left(self):
        """
        Return left child node (None if not set)
        :return: left child node
        """
        return BinaryNode.or_none(self.left)

    def get_right(self):
        """
        Return right child node (None if not set)
        :return: right child node
        """
        return BinaryNode.or_none(self.right)

    def get_tree(self):
        """
        Return the tree this node belongs to (None if not set)
        :return: tree of self
        """
        return self.tree or None

    def set_parent(self, new_parent):
        """
        Set parent to passed node if valid
        Would have decorated with or_none,
        but had complications with inherited decorators
        :param new_parent: new parent node
        :return: no return value
        """
        node = BinaryNode.or_none(new_parent)
        self.parent = node

    def set_left(self, new_left_child):
        """
        Set left child to passed node if valid
        Updates child node with this as parent
        Would have decorated with or_none,
        but had complications with inherited decorators
        :param new_left_child: new left child node
        :return: no return value
        """
        node = BinaryNode.or_none(new_left_child)
        self.left = node
        if node is not None:
            node.parent = self

    def set_right(self, new_right_child):
        """
        Set right child to passed node if valid
        Updates child node with this as parent
        Would have decorated with or_none,
        but had complications with inherited decorators
        :param new_right_child: new right child node
        :return: no return value
        """
        node = BinaryNode.or_none(new_right_child)
        self.right = node
        if node is not None:
            node.parent = self

    def set_tree(self, new_tree):
        """
        Set the tree of this node
        Used for .show mirroring at least
        :param new_tree: BinaryTree
        :return:
        """
        if isinstance(new_tree, BinaryTree):
            self.tree = new_tree

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
        # Clear parent's reference to self
        parent = self.get_parent()
        if parent is not None:
            if self.is_left_child():
                parent.set_left(None)
            elif self.is_right_child():
                parent.set_right(None)
        # Clear self's reference to parent
        self.set_parent(None)

        return self

    def replace_with(self, replacement_arg):
        """
        Replace self subtree with replacement subtree
        May replace node with None
        :param replacement_arg: NodeBST replacement node
        :return: replacement node
        """
        replacement = BinaryNode.or_none(replacement_arg)

        # Do not proceed if replacement is invalid
        # Nothing to do if replacing node with itself
        if replacement == self:
            return self

        # Link parent
        parent = self.get_parent()
        if parent is not None:
            if self.is_left_child():
                parent.set_left(replacement)
            elif self.is_right_child():
                parent.set_right(replacement)
        elif self.tree is not None:
            # Replacing head
            self.tree.head = replacement

        # Remove node from tree
        self.set_parent(None)
