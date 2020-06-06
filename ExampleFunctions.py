from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from DataStructures.BinarySearchTree import BinarySearchTree
from DataStructures.BinarySearchNode import BinarySearchNode
from ConsoleMenu import Menu


class MaxHeap:
    heap = BinaryMaxHeap()
    verbose = False

    @classmethod
    def add(cls):
        """Add a new item to the max heap"""
        print ("Enter new integer value: ")
        key_value = Menu.get_int()
        print ('\n', end='')
        MaxHeap.heap.add_item(key_value, verbose=MaxHeap.verbose)
        print ("Item", key_value, "was added to the heap.")

    @classmethod
    def extract(cls):
        """Extract the maximum value from the heap"""
        max_value = MaxHeap.heap.extract_max(verbose=MaxHeap.verbose)
        print ('The maximum value has been extracted and is', max_value, end='')

    @classmethod
    def show(cls):
        """Show the max heap"""
        MaxHeap.heap.show()

    @classmethod
    def toggle_verbose(cls):
        """Turn max heap verbose on/off"""
        MaxHeap.verbose = ~MaxHeap.verbose
        print ("Binary Max Heap: Verbose is now", "on" if MaxHeap.verbose else "off")

    @classmethod
    def empty_tree(cls):
        """Erase binary max heap. Create new."""
        MaxHeap.heap = BinaryMaxHeap()
        print ("Binary max heap was purged.")

    @classmethod
    def get_menu(cls, parent=None) -> Menu:
        """
        Get max heap menu options
        :param parent: ExampleMenu parent menu of this max menu
        :return: ExampleMenu max heap menu
        """
        menu = Menu("""Binary max heap main menu.
Please select an option below.
""", parent=parent)
        # Menu options
        # Pass *references* to functions, not return values
        menu.add_option("Add an item to the binary max heap", function=MaxHeap.add)
        menu.add_option("Extract the maximum value", function=MaxHeap.extract)
        menu.add_option("Show the heap", function=MaxHeap.show)
        menu.add_option("Toggle verbose on/off", function=MaxHeap.toggle_verbose)
        menu.add_option("Empty the heap", function=MaxHeap.empty_tree)

        return menu


class BST:
    tree = BinarySearchTree()
    verbose = False

    @classmethod
    def insert(cls):
        """Add a new item to the tree"""
        print("Enter new integer value: ")
        key_value = Menu.get_int()
        print('\n', end='')
        BST.tree.insert(key_value, verbose=BST.verbose)
        print ("Item", key_value, "was added to the tree")

    @classmethod
    def search(cls):
        """Find item in tree"""
        print ("Enter integer value to search: ")
        key_value = Menu.get_int()
        print("\n", end='')
        node = BST.tree.search(key_value, verbose=BST.verbose)
        print ("Item ", key_value, " is ", "" if node is not None else "not ", "in the tree", sep='')

    @classmethod
    def delete(cls):
        """Remove an item from the tree, if there"""
        print("Enter the integer value to remove: ")
        key_value = Menu.get_int()
        print('\n', end='')
        removed_node = BST.tree.delete(key_value, verbose=BST.verbose)
        if removed_node is not None:
            print (key_value, "was removed from the tree.")
        else:
            print (key_value, "was not found in the tree.")

    @classmethod
    def show(cls):
        """Show the tree"""
        print ("Oops! This doesn't work yet.")
        pass

    @classmethod
    def toggle_verbose(cls):
        """Turn binary search tree verbose on/off"""
        BST.verbose = ~BST.verbose
        print ("Binary Search Tree: Verbose is now", "on" if BST.verbose else "off")

    @classmethod
    def empty_tree(cls):
        """Erase binary search tree. Create new."""
        BST.tree = BinarySearchTree()
        print ("Binary search tree was purged.")

    @classmethod
    def get_menu(cls, parent=None) -> Menu:
        """
        Get max heap menu options
        :param parent: ExampleMenu parent menu of this max menu
        :return: ExampleMenu max heap menu
        """
        menu = Menu("""Binary search tree main menu.
Please select an option below.
""", parent=parent)
        # Menu options
        # Pass *references* to functions, not return values
        menu.add_option("Add an item to the tree", function=BST.insert)
        menu.add_option("Find an item in the tree", function=BST.search)
        menu.add_option("Delete an item from the tree", function=BST.delete)
        menu.add_option("Show the tree", function=BST.show)
        menu.add_option("Toggle verbose on/off", function=BST.toggle_verbose)
        menu.add_option("Empty the tree", function=BST.empty_tree)

        return menu

    pass
