from DataStructures import Heap
import numpy as np

strings = {
    'before':   'Before action performed.',
    'added':    'Value added to end of heap. Max-heap property not necessarily satisfied.',
    'extracted':'Maximum value extracted. Max-heap property not necessarily satisfied.',
    'middle':   'Intermediate heap. Max-heap property not necessarily satisfied.',
    'end':      'Final heap. Max-heap property satisfied.'
}

class MaxHeap(Heap.Heap):
    """
    Implement heap data structure as max heap
    """

    def __init__(self):
        """
        Set default value of heap to negative infinity
        """
        super().__init__()
        self.default_value = -np.inf

    def update_max_heap_property_up(self, starting_index, verbose=False):
        """
        Update max heap property upwards
        :param starting_index: index of value from which to start
        :return: no return value
        """
        i_this = starting_index
        while i_this > 0:
            # This node value
            this = self.get_value_at(i_this)

            # Parent node
            i_parent = self.get_parent_index(i_this)
            parent = self.get_value_at(i_parent)

            if this > parent:
                self.swap(i_this, i_parent)
                i_this = i_parent
            else:
                break

            # Verbose: show intermediate heaps
            if verbose and i_this > 0:
                self.log('middle')

        if verbose:
            self.log('end')

    def update_max_heap_property_down(self, starting_index, verbose=False):
        """
        Update max heap property downwards
        :param starting_index: index from which to start
        :return: no return value
        """
        i_this = starting_index
        while True:
            # This node value
            this = self.get_value_at(i_this)

            # Left child
            i_left = self.get_left_index(i_this)
            left = self.get_value_at(i_left)

            # Right child
            i_right = self.get_right_index(i_this)
            right = self.get_value_at(i_right)

            # Check if changes are needed
            if this < left:
                # This and left child are out of order
                self.swap(i_this, i_left)
                i_this = i_left
            elif this < right:
                # This and right child are out of order
                self.swap(i_this, i_right)
                i_this = i_right
            else:
                # No changes needed
                # Default value -inf reaches here
                break

            # Verbose: Show intermediate heaps
            if verbose:
                self.log('middle')

        # Verbose: show final heap
        if verbose:
            self.log('end')

    def add_item(self, new_value, verbose=False):
        """
        Add item to heap
        Update max heap property
        @overrides method in Heap
        :param new_value: new integer value
        :return: No return value
        """

        # Verbose: show heap before addition
        if verbose:
            self.log('before')

        # Add as last item
        # Update heap last_item and level
        super().add_item(new_value)

        # Verbose: show heap before max-heap property satisfied
        if verbose:
            self.log('added')

        # Update max heap property upwards
        self.update_max_heap_property_up(self.last_item, verbose=verbose)

    def extract_max(self, verbose=False):
        """
        Remove first item (max) and update max-heap property
        :return: int first item (max)
        """
        if self.last_item < 0:
            return self.default_value

        # Verbose: Show tree before popping
        if verbose:
            self.log('before')

        # Remove first item
        max_value = self.get_value_at(0)
        # Replace first item with last item
        self.set_value_at(0, self.get_value_at(self.last_item))
        self.last_item = self.last_item - 1

        # Verbose: Show tree before fixing max heap property
        if verbose:
            self.log('extracted')

        # Update max heap property downwards
        self.update_max_heap_property_down(0, verbose=verbose)

        return max_value

    def log(self, string):
        """
        For verbose output, show message and heap state
        :param string: string from strings[] list
        :return: no return value
        """
        print (strings[string])
        self.show()
        print ('\n', end='')
