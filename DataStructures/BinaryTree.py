import numpy as np
from collections import deque
# Support for terminal colors in linux, max, and windows
import colorama
colorama.init()


class BinaryTree:
    """
    Basic binary tree for inheritance.
    """
    # Head of tree is a *Node or None(empty)
    head = None
    # This is a good time-saving idea,
    # But I think that its potential for bugs
    # is too high to implement
    #
    #   Height of tree
    #   height = 0
    #
    #   When height may have changed, set to true
    #   height_unknown = False
    HIGHLIGHT_FORE = colorama.Fore.MAGENTA
    HIGHLIGHT_BACK = colorama.Back.WHITE
    SECONDARY_FORE = colorama.Fore.BLACK
    SECONDARY_BACK = colorama.Back.CYAN

    def get_count_height_and_max_digs(self) -> (int, int, int):
        """
        Get number of nodes in tree
        and height of tree
        and largest number of digits in any entry in tree
        by crawling tree O(n)
        :return (int, int, int): (node count, height of tree, max # digits)
        """
        if self.is_empty():
            return 0

        count=0
        height = 0
        # Record max num until end to minimize Math.log usage
        max_num = 0
        # Queue of all nodes as tuple (node, depth)
        queue = deque()
        # Add head to queue
        queue.appendleft((self.head, 1))
        while len(queue) > 0:
            # Get another node and its depth
            (node, depth) = queue.pop()
            count += 1

            # New height?
            if depth > height:
                height = depth

            # New max num?
            key = node.get_key()
            if key > max_num:
                max_num = key

            # Add children to queue
            left = node.get_left()
            right = node.get_right()
            if left is not None:
                queue.appendleft((left, depth + 1))
            if right is not None:
                queue.appendleft((right, depth + 1))

        # Git maximum number of digits from largest number
        max_digs = int(np.floor(np.log10(max_num)) + 1)

        return count, height, max_digs

    def is_empty(self):
        """
        :return: True if (tree is empty) else False
        """
        return self.head is None

    def show(self, primary_highlights=(None,), secondary_highlights=(None,)):
        """
        Show binary tree
        :param primary_highlights: tuple (BinarySearchNode,) to be highlighted with primary colors
        :param secondary_highlights: tuple (BinarySearchNode,) to be highlighted with secondary colors
        :return: no return value
        """
        # Highlight/secondary must have __contains__ method
        primary_highlights = primary_highlights if type(primary_highlights) is tuple else (None, primary_highlights)
        secondary_highlights = secondary_highlights if type(secondary_highlights) is tuple else (None, secondary_highlights)

        if self.is_empty():
            print ('****************')
            print ('No items in tree')
            print ('****************')
            return

        # Get node count, height of tree, and maximum # digits
        count, height, max_digs = self.get_count_height_and_max_digs()

        # Maximum number of digits determines padding
        minimum_cell = max_digs + 3

        def get_cell_width(depth, hgt=height, min_wid=minimum_cell) -> int:
            """
            Return the width of each cell on THIS line,
            given the width of cells on the bottom-most level
            :param depth: depth of this cell relative to the top of the tree
            :param hgt: total height of the tree
            :param min_wid: width of the smallest cell in the tree
            :return int: cell width on this level
            """
            return int(np.power(2, hgt - depth)) * minimum_cell

        def demarcate_tree(hgt=height, cell_wid=minimum_cell):
            """
            Show line of asterisks to demarcate bounds of tree
            :return: no return value
            """
            # Number of nodes on bottom is 2^hgt
            max_nodes = int(np.power(2, hgt - 1))
            print (''.center(cell_wid * max_nodes, '*'))

        # Show bound of top of tree
        demarcate_tree()

        # Output tree
        # Loop through nodes
        # For each node, add another node to the queue
        # Loop until all non-empty nodes (# == count) are printed
        last_level = 1
        # Queue holds (node, depth of node)
        queue = deque()
        queue.appendleft((self.head, 1))
        while count > 0:
            # Get another node
            node, depth = queue.pop()
            # We know the total number of non-empty nodes
            # Keep record of when one is printed
            # so that we can exit when they are all out
            if node is not None:
                count -= 1

            # At next level, break line
            if depth > last_level:
                last_level = depth
                print ('\n', end='')

            # On last line, pad each item by one space each side
            width_each = get_cell_width(depth)

            # Get string value
            value_str = ""
            if node is not None:
                value_str = str(node.get_key())
            value_formatted = value_str.center(width_each)
            if node is not None and (node in primary_highlights or node in secondary_highlights):
                fore = self.HIGHLIGHT_FORE if node in primary_highlights else self.SECONDARY_FORE
                back = self.HIGHLIGHT_BACK if node in primary_highlights else self.SECONDARY_BACK
                value_highlighted = fore + back + value_str + colorama.Style.RESET_ALL
                value_formatted = value_formatted.replace(value_str, value_highlighted)
            print (value_formatted, end='')

            # Set up next level
            # get_left/right return node or None
            left = right = None
            if node is not None:
                left = node.get_left()
                right = node.get_right()
            queue.appendleft((left, depth + 1))
            queue.appendleft((right, depth + 1))

        # End line
        print ('\n', end='')

        # Show bound of bottom of tree
        demarcate_tree()