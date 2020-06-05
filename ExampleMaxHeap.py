from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from ExampleMenu import ExampleMenu


class ExampleMaxHeap:
    myHeap = BinaryMaxHeap()
    verbose = False

    @classmethod
    def add(cls):
        """Add a new item to the max heap"""
        print ("Enter new integer value: ")
        new_value = ExampleMenu.get_int()
        print ('\n', end='')
        ExampleMaxHeap.myHeap.add_item(new_value, verbose=ExampleMaxHeap.verbose)

    @classmethod
    def extract(cls):
        """Extract an item from the max heap"""
        max_value = ExampleMaxHeap.myHeap.extract_max(verbose=ExampleMaxHeap.verbose)
        print ('The maximum value has been extracted and is', max_value, end='')

    @classmethod
    def show(cls):
        """Show the max heap"""
        ExampleMaxHeap.myHeap.show()

    @classmethod
    def toggle_verbose(cls):
        """Turn max heap verbose on/off"""
        ExampleMaxHeap.verbose = ~ExampleMaxHeap.verbose
        print ("Verbose is now", "on" if ExampleMaxHeap.verbose else "off")

    @classmethod
    def empty_tree(cls):
        """Erase binary max heap. Create new."""
        ExampleMaxHeap.myHeap = BinaryMaxHeap()

    @classmethod
    def get_menu(cls, parent=None) -> ExampleMenu:
        """
        Get max heap menu options
        :param parent: ExampleMenu parent menu of this max menu
        :return: ExampleMenu max heap menu
        """
        menu = ExampleMenu("""Max heap main menu.
Please select an option below.
""", parent=parent)
        # Menu options
        # Pass *references* to functions, not return values
        menu.add_option("Add an item", function=ExampleMaxHeap.add)
        menu.add_option("Extract the maximum value", function=ExampleMaxHeap.extract)
        menu.add_option("Show the max heap", function=ExampleMaxHeap.show)
        menu.add_option("Toggle verbose on/off", function=ExampleMaxHeap.toggle_verbose)
        menu.add_option("Empty max heap", function=ExampleMaxHeap.empty_tree)

        return menu
