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
""", parent_menu=parent)
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

    class Rotate:
        @classmethod
        def left(cls):
            """Rotate the tree left"""
            print("Enter the key at which to rotate left: ")
            key_value = Menu.get_int()
            print('\n', end='')
            node = BST.tree.search(key_value, verbose=BST.verbose)
            if isinstance(node, BinarySearchNode):
                new_root = node.rotate_left(verbose=BST.verbose)
                if new_root is not None:
                    print("The tree was rotated left at", key_value)
                else:
                    print("Unable to rotate the tree left at", key_value)
            else:
                print(key_value, "was not found in the tree")


        @classmethod
        def right(cls):
            """Rotate the tree right"""
            print("Enter the key at which to rotate right: ")
            key_value = Menu.get_int()
            print('\n', end='')
            node = BST.tree.search(key_value, verbose=BST.verbose)
            if isinstance(node, BinarySearchNode):
                new_root = node.rotate_right(verbose=BST.verbose)
                if new_root is not None:
                    print("The tree was rotated right at", key_value)
                else:
                    print("Unable to rotate the tree right at", key_value)
            else:
                print(key_value, "was not found in the tree")

        @classmethod
        def get_menu(cls, parent=None):
            """
            Rotate the tree
            :param parent: ExampleMenu parent menu of this max menu
                           Should be from BST
            :return: ExampleMenu rotate menu
            """
            menu = Menu("""Rotate the tree:
            """, parent_menu=parent)
            # Menu options
            # Pass *references* to functions, not return values
            menu.add_option("Rotate left at...", function=BST.Rotate.left)
            menu.add_option("Rotate right at...", function=BST.Rotate.right)

            return menu


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
        BST.tree.show()

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
        Get binary search tree menu options
        :param parent: ExampleMenu parent menu of this max menu
        :return: ExampleMenu max heap menu
        """
        menu = Menu("""Binary search tree main menu.
Please select an option below.
""", parent_menu=parent)

        rotate_menu = BST.Rotate.get_menu(parent=menu)

        # Menu options
        # Pass *references* to functions, not return values
        menu.add_option("Add an item to the tree", function=BST.insert)
        menu.add_option("Find an item in the tree", function=BST.search)
        menu.add_option("Delete an item from the tree", function=BST.delete)
        menu.add_option("Rotate tree", submenu=rotate_menu)
        menu.add_option("Show the tree", function=BST.show)
        menu.add_option("Toggle verbose on/off", function=BST.toggle_verbose)
        menu.add_option("Empty the tree", function=BST.empty_tree)

        return menu

    pass