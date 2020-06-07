import numpy as np
# Support for terminal colors in linux, max, and windows
import colorama
colorama.init()


class BinaryHeap:
    """
    Implement heap data structure as np.ndarray

    For simplicity, only allow integers
    """

    # Heap as unlimited numpy array
    # Useful for math functions such as max
    heap_size = 10
    heap = np.array([0] * heap_size, dtype=np.int)
    # Last item points to size
    last_item = -1
    # Deepest level, zero-indexed1
    level = 0
    # When an item is not found
    default_value = 0
    # Highlight colors for verbose
    HIGHLIGHT_FORE = colorama.Fore.MAGENTA
    HIGHLIGHT_BACK = colorama.Back.WHITE

    def add_item(self, new_value):
        """
        Add item to heap
        :param new_value: new value
        :return: No return value
        """

        # Allocate more memory if necessary
        # This keeps add_item to O(1), generally.
        # Otherwise, have to duplicate ndarray every time
        # last_item is an index, heap_size is a limit (index + 1)
        if self.last_item >= self.heap_size - 1:
            # Allocate double the memory
            new_heap_list = self.heap.tolist() + [0] * self.heap_size
            self.heap = np.array(new_heap_list, dtype=np.int)
            self.heap_size *= 2

        # Add item index and value
        # to already allocated memory
        self.last_item = self.last_item + 1
        self.heap[self.last_item] = new_value

        # Update heap level
        self.level = np.floor(np.log(self.last_item + 1) / np.log(2))

    def show(self, highlight=None):
        """
        Show heap
        :param highlight: highlight this index
        :return:
        """

        if self.last_item < 0:
            print ('****************')
            print ('No items in heap')
            print ('****************')
            return

        # Maximum number of digits determines padding
        max_digs = self.get_max_digs()
        minimum_cell = max_digs + 3

        def demarcate_heap(hgt=self.level, cell_wid=minimum_cell):
            """
            Show line of asterisks to demarcate bounds of heap
            :return: no return value
            """
            # Number of nodes on bottom is 2^hgt
            max_nodes = int(np.power(2, hgt))
            print (''.center(cell_wid * max_nodes, '*'))

        # Output each level
        demarcate_heap()
        last_level = 0
        for i in range(0, self.last_item + 1, 1):
            # Center each level so that has appropriate width
            level = np.floor(np.log(i + 1) / np.log(2))
            # At level up, break line
            if level > last_level:
                last_level = level
                print ('\n', end='')
            # On last line, pad each item by one space each side
            width_each = int(np.power(2, self.level - level)) * minimum_cell

            # Get string value
            value_str = str(self.get_value_at(i))
            value_formatted = value_str.center(width_each)
            if i == highlight:
                number_highlighted = self.HIGHLIGHT_FORE + self.HIGHLIGHT_BACK + value_str + colorama.Style.RESET_ALL
                value_formatted = value_formatted.replace(value_str, number_highlighted)
            print (value_formatted, end='')

        # End line
        print ('\n', end='')
        demarcate_heap()

    @staticmethod
    def get_parent_index(i):
        """
        Get index of parent node
        :param i: index (0-indexed) of node in question
        :return: parent node index
        """
        # Indexing for i_parent == i // 2 is NOT ZERO-INDEXED
        pos = i + 1
        parent_pos = pos // 2
        parent_index = parent_pos - 1
        return parent_index

    @staticmethod
    def get_left_index(i):
        """
        Get index of left child
        :param i: index (0-indexed) of parent item
        :return: left child index
        """
        pos = i + 1
        left_pos = 2 * pos
        left_index = left_pos - 1
        return left_index

    @staticmethod
    def get_right_index(i):
        """
        Get index of right child
        :param i: index (0-indexed) of parent item
        :return: right child index
        """
        pos = i + 1
        right_pos = 2 * pos + 1
        right_index = right_pos - 1
        return right_index

    def get_value_at(self, i):
        """
        Get value at index or -np.inf if it doesn't exist
        :param i: potential index
        :return: value at index or default value
        """
        return self.default_value if i > self.last_item else self.heap[i]

    def get_max_digs(self):
        """
        Return the height of the heap
        and the maximum number of digits for any entry in the heap
        :return (int, int): height, max_digs
        """

        # Get maximum number of digits
        # 20200607: np.ceil --> np.floor + 1
        #   Consider edge case n = 9 vs n = 10
        #   ceil(log_10(9)) == 1,       ceil(log_10(10)) == 1
        #   floor(log_10(9)) + 1 == 1,  floor(log_10(10)) + 1 == 2
        max_digs = int(np.floor(np.log10(np.max(self.heap))) + 1)

        return max_digs


    def set_value_at(self, i, new_value=default_value):
        """
        Set value at index
        :param i: index of element
        :param new_value: new value to be set
        :return: no return value
        """
        self.heap[i] = new_value

    def swap(self, index_0, index_1):
        """
        Swap values at index_0 and index_1
        :param index_0: index of first element
        :param index_1: index of second element
        :return: no return value
        """
        value_0 = self.get_value_at(index_0)
        value_1 = self.get_value_at(index_1)
        self.set_value_at(index_0, value_1)
        self.set_value_at(index_1, value_0)