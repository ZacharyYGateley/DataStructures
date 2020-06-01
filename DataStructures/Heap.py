import numpy as np

class Heap:
    """
    Implement heap data structure as np.ndarray
    """

    # Heap as unlimited numpy array
    # Useful for math functions such as max
    heap = np.array([], dtype=np.int)
    # Last item points to size
    last_item = -1
    # Deepest level, zero-indexed1
    level = 0
    # When an item is not found
    default_value = 0

    def add_item(self, new_value):
        """
        Add item to heap
        :param new_value: new value
        :return: No return value
        """
        # Add as last item
        # Numpy append not in place
        self.heap = np.append(self.heap, new_value)

        # Update heap last_item and level
        self.last_item = self.last_item + 1
        self.level = np.floor(np.log(self.last_item + 1) / np.log(2))

    def show(self):
        """ Show heap """

        if self.last_item < 0:
            print ('No items in heap')
            return

        # Maximum number of digits determines padding
        minimum_cell = int(np.ceil(np.log(np.max(self.heap) / np.log(10)))) + 3

        def demarcate():
            print (''.center(minimum_cell * int(np.power(2, self.level)), '*'))

        # Output each level
        demarcate()
        last_level = 0
        for i in range(0, self.last_item + 1, 1):
            value_at = self.get_value_at(i)

            # Center each level so that has appropriate width
            level = np.floor(np.log(i + 1) / np.log(2))
            # At level up, break line
            if level > last_level:
                last_level = level
                print('\n', end='')
            # On last line, pad each item by one space each side
            width_each = int(np.power(2, self.level - level)) * minimum_cell
            print (str(value_at).center(width_each), end='')

        # End line
        print ('\n', end='')
        demarcate()

    @staticmethod
    def get_parent_index(i):
        """
        Get index of parent node
        :param i: index of node in question
        :return: parent node index
        """
        return i // 2

    @staticmethod
    def get_left_index(i):
        """
        Get index of left child
        :param i: index of parent item
        :return: left child index
        """
        return 2 * i

    @staticmethod
    def get_right_index(i):
        """
        Get index of right child
        :param i: index of parent item
        :return: right child index
        """
        return 2 * i + 1

    def get_value_at(self, i):
        """
        Get value at index or -np.inf if it doesn't exist
        :param i: potential index
        :return: value at index or default value
        """
        return self.default_value if i > self.last_item else self.heap[i]

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