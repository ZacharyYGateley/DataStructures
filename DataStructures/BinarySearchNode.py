from DataStructures.BinaryNode import BinaryNode


class BinarySearchNode(BinaryNode):
    @classmethod
    def or_none(cls, node):
        """
        Verify passed node is a member of this class
        Return either the node or None
        :param node: node in question
        :return: BinarySearchNode object || None
        """
        return node if isinstance(node, cls) else None

    def predecessor(self, verbose=False):
        """
        Get the predecessor node of this node by using the binary search tree property
        :param verbose: boolean show actions during insert
        :return: NodeBST predecessor or None
        """
        # First get left child
        predecessor = self.get_left()
        # Then crawl right side of subtree
        if predecessor is not None:
            # Show process if verbose
            if verbose:
                self.show(highlight=self, secondary_highlight=predecessor)

            while predecessor.get_right() is not None:
                predecessor = predecessor.get_right()

        # Show the process if verbose
        if verbose:
            self.show(highlight=self, secondary_highlight=predecessor)

        # Finish
        return predecessor

    def successor(self, verbose=False):
        """
        Get the successor node of this node by using the binary search tree property
        :param verbose: boolean show actions during insert
        :return: NodeBST successor or None
        """
        # First get right child
        successor = self.get_right()
        # Then traverse left side of tree until we hit a leaf
        if successor is not None:
            # Show process if verbose
            if verbose:
                self.show(highlight=self, secondary_highlight=successor)

            while successor.get_left() is not None:
                successor = successor.get_left()

        # Show the process if verbose
        if verbose:
            self.show(highlight=self, secondary_highlight=successor)

        # Finish
        return successor

    def rotate_left(self, verbose=False):
        """
        Rotate subtree rooted at self to the left
        Recommended this be called from a Tree function of the same name
        So that Tree.head can be accounted for
        :param verbose: boolean show actions during insert
        :return: new root of subtree
        """
        #
        new_subroot = self.get_right()
        if new_subroot is None:
            print ("Cannot rotate subtree rooted at node (%d) to the left".format(self.get_key()))
            return

        # If right child has a left child,
        # it needs to jump to the other side of the new root
        problem_child = new_subroot.get_left()
        if problem_child is not None:
            problem_child = problem_child.remove_as_subtree()

        # Shift new subroot up
        new_subroot.set_parent(self.get_parent())
        new_subroot.set_left(self)

        # Shift self down
        self.set_parent(new_subroot)
        self.set_right(problem_child)

        # Return new subroot of tree
        return new_subroot

    def rotate_right(self, verbose=False):
        """
        Rotate subtree rooted at self to the right
        Recommended this be called from a Tree function of the same name
        So that Tree.head can be accounted for
        :param verbose: boolean show actions during insert
        :return: new root of subtree
        """
        new_subroot = self.get_left()
        if new_subroot is None:
            print("Cannot rotate subtree rooted at node (%d) to the left".format(self.get_key()))
            return None

        # If left child has a right child,
        # It needs to jump from left side to right side
        problem_child = new_subroot.get_right()
        if problem_child is not None:
            problem_child = problem_child.remove_as_subtree()

        # Shift new subroot up
        new_subroot.set_parent(self.get_parent())
        new_subroot.set_right(self)

        # Shift self down
        self.set_parent(new_subroot)
        self.set_left(problem_child)

        # Return new subroot of tree
        return new_subroot

    def show(self, highlight=None, secondary_highlight=None):
        """
        Mirrors show of BinarySearchTree
        :param args: Any arguments to pass on to BinarySearchTree
        :return: no return value
        """
        if self.tree and self.tree.show:
            self.tree.show(highlight=highlight, secondary_highlight=secondary_highlight)