from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from ExampleMenu import ExampleMenu
import ExampleMaxHeap as emh

myHeap = BinaryMaxHeap()


# Build menus
# Build submenus before main menu
# so that references are available
menu = ExampleMenu("""Program main menu.
Please select a data structure type.""")

# Max heap
menu_maxheap = ExampleMenu("""Max heap main menu.
Please select an option below.
""", parent=menu)
menu_maxheap.add_option("Add an item", function=emh.add)
menu_maxheap.add_option("Extract the maximum value", function=emh.extract)
menu_maxheap.add_option("Show the max heap", function=emh.show)
menu_maxheap.add_option("Toggle verbose on/off", function=emh.toggle_verbose)

# Build main menu
menu.add_option("Max heap", submenu=menu_maxheap)


# Loop main menu
menu.do_menu()

# Finito
print ("\nThank you\n\n")