import math
from DataStructures.BinarySearchNode import BinarySearchNode


class EmptyTreeException(Exception):
    def __init__(self, expression="EmptyTree", message="Tree is empty"):
        self.expression = expression
        self.message = message


class NodeNotFoundException(Exception):
    def __init__(self, expression="NodeNotFound", message="Node not found"):
        self.expression = expression
        self.message = message


class BinarySearchTree:
    """
    Implement binary search tree

    For simplicity, all input must be integers
    """

    head = None

    def __init__(self):
        pass

    def insert(self, key, verbose=False):
        """
        Insert key into tree
        :param key: key of new node
        :param verbose: boolean show actions during insert
        :return: no return value
        """
        # Assert valid input
        assert(isinstance(int, key))

        # Create a new node with this key
        node = BinarySearchNode(key=key)

        # If empty tree, add as Head
        if self.head is None:
            self.head = node
        else:
            # Otherwise, find new parent node in tree by binary search
            parent = self.search(node.key, verbose=verbose)

            # Insert node here
            node.parent = parent

    def delete(self, key, verbose=False):
        """
        Delete a node in the tree by the passed key value.
        Do not raise exception on not found.
        :param key: key of node to delete
        :param verbose: boolean show actions during insert
        :return: no return value
        """
        # Assert valid input
        assert(isinstance(int, key))

        # Find first instance of key in tree
        node = self.search(key, verbose=verbose)

        # Exit if key not found in tree
        # No error required
        if not node:
            return

        # Find replacement node
        # If node on the left, replace with successor
        # If no successor, then the first node on the left can be promoted
        replacement = self.successor(node, verbose=verbose) or node.get_left()

        # Remove replacement from tree
        # This represents the root of a subtree
        replacement = replacement.remove_as_subtree()

        # Splice replacement into tree at node
        node.replace_with(replacement)

    def search(self, key, verbose=False):
        """
        Finds the first instance of a node with the given search key
        Binary search tree property:
            parent.key > parent.left.key
            parent.key <= parent.right.key
        :param key: search key
        :param verbose: boolean show actions during insert
        :return: node
        """

        # Cannot search an empty tree
        try:
            assert(not self.is_empty())
        except AssertionError:
            raise EmptyTreeException

        # Loop until the key is found or we hit the bottom of the tree
        node = self.head
        while node is not None:
            this_key = node.key()
            if key < this_key:
                node = node.get_left()
            elif key > this_key:
                node = node.get_right()
            else:
                break
        return node

    def is_empty(self):
        """
        :return: True if (tree is empty) else False
        """
        return self.head is None
