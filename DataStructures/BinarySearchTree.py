from DataStructures.BinarySearchNode import BinarySearchNode
from DataStructures.BinaryTree import BinaryTree


class EmptyTreeException(Exception):
    def __init__(self, expression="EmptyTree", message="Tree is empty"):
        self.expression = expression
        self.message = message


class NodeNotFoundException(Exception):
    def __init__(self, expression="NodeNotFound", message="Node not found"):
        self.expression = expression
        self.message = message


class BinarySearchTree(BinaryTree):
    """
    Implement binary search tree

    For simplicity, all input must be integers
    """

    def insert(self, key, verbose=False):
        """
        Insert key into tree
        :param key: key of new node
        :param verbose: boolean show actions during insert
        :return: no return value
        """
        # Assert valid input
        assert(isinstance(key, int))

        # Create a new node with this key
        node = BinarySearchNode(key=key, tree=self)

        # If empty tree, add as Head
        if self.head is None:
            self.head = node
        else:
            # Otherwise, find new parent node in tree by binary search
            parent, is_left_child, is_right_child = self.insert_get_parent(node.key, verbose=verbose)

            # Insert node here
            # set_left and set_right link both nodes together
            if parent is not None:
                if is_left_child:
                    parent.set_left(node)
                else:
                    parent.set_right(node)

        # Show tree if verbose
        if verbose:
            # Primary colors for inserted node
            self.show(primary_highlights=node)

    def insert_get_parent(self, key, verbose=False) -> (BinarySearchNode or None, bool, bool):
        """
        Find and return which node should be the parent
        of a node with the given key
        Recall inary search tree property:
            parent.key > parent.left.key
            parent.key <= parent.right.key
        :param key: key to be added to tree
        :param verbose: boolean show actions during insert
        :return: (
            BinarySearchNode new parent or None no parent found,
            should be a left child,
            should be a right child
            )
        """

        # Value not in tree if tree is empty
        if self.is_empty():
            return None

        # Loop until the key is found or we hit the bottom of the tree
        node = self.head
        is_left_child = False
        is_right_child = False
        while node is not None:
            # Highlight node while searching for where it belongs
            if verbose:
                # Secondary colors for searching
                self.show(secondary_highlights=node)

            this_key = node.get_key()
            if key < this_key:
                left = node.get_left()
                if left is not None:
                    node = left
                else:
                    is_left_child = True
                    break
            elif key >= this_key:
                right = node.get_right()
                if right is not None:
                    node = right
                else:
                    is_right_child = True
                    break
            # Do not stop at match, go right

        return node, is_left_child, is_right_child

    def delete(self, key, verbose=False) -> BinarySearchNode or None:
        """
        Delete a node in the tree by the passed key value.
        Do not raise exception on not found.
        :param key: key of node to delete
        :param verbose: boolean show actions during insert
        :return: returns the node if it is in the tree
        """
        # Assert valid input
        assert(isinstance(key, int))

        # Find first instance of key in tree
        node = self.search(key, verbose=verbose)

        # Exit if key not found in tree
        # No error required
        if not node:
            return None

        # Find replacement node
        right = node.get_right()
        left = node.get_left()
        # Simple cases, left or right child of delete are None
        if right is None:
            # Shift left up
            # Left might also be none
            # Logic still works
            if left is not None:
                left = left.remove_as_subtree()
            replacement = node.replace_with(left)
        elif left is None:
            # Shift right up
            replacement = node.replace_with(right.remove_as_subtree())
        else:
            # Right subtree contains the successor
            successor = node.successor(verbose=verbose)
            # If the successor is the right child,
            # Right child is the replacement
            # (successor's left subtree is always empty)
            if successor == right:
                # Pop whole tree to the right
                replacement = right.remove_as_subtree()
                # Replacement is a subtree
            else:
                # Successor is embedded
                # (i.e. successor = node.right.left....left)
                # Successor might have a right subtree
                # Transplant it into successor's position
                problem_child = successor.get_right()
                if problem_child is not None:
                    # Show this problem child
                    if verbose:
                        self.show(primary_highlights=successor, secondary_highlights=problem_child)

                    problem_child = problem_child.remove_as_subtree()
                # Successor parent is not None and is not delete node
                # set_left links both ways, parent->child, child->parent
                successor.get_parent().set_left(problem_child)
                successor.set_right(None)

                # Show the problem child's movement
                if verbose and problem_child is not None:
                    self.show(secondary_highlights=problem_child)

                replacement = successor.remove_as_subtree()
                # Add right side of delete to this node
                replacement.set_right(right)

            # Left children of node go to its replacement subtree
            # Recall successor's left subtree is always empty
            left = left.remove_as_subtree()
            replacement.set_left(left)

        # Clean up any loose ends
        if self.head == node:
            self.head = replacement

        # Show process if verbose
        if verbose:
            self.show(primary_highlights=replacement)

        return node

    def search(self, key, verbose=False) -> BinarySearchNode or None:
        """
        Find first instance of a node with the given search key
        Binary search tree property:
            parent.key > parent.left.key
            parent.key <= parent.right.key
        :param key: search key
        :param verbose: boolean show actions during insert
        :return: node
        """

        # Value not in tree if tree is empty
        if self.is_empty():
            return None

        # Loop until the key is found or we hit the bottom of the tree
        node = self.head
        while node is not None:
            this_key = node.get_key()
            if key == this_key:
                # Key found! Stop at first match
                break

            # Show process if verbose
            if verbose:
                self.show(secondary_highlights=node)

            if key < this_key:
                # Key belongs on the left side of this node (re BST property)
                node = node.get_left()
            elif key > this_key:
                # Key belongs on the right side of this node
                node = node.get_right()

        # Show found item if verbose
        if node is not None and verbose:
            self.show(primary_highlights=node)

        return node
