from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from ExampleMenu import ExampleMenu
from ExampleMaxHeap import ExampleMaxHeap

myHeap = BinaryMaxHeap()


# Build menus
# Build submenus before main menu
# so that references are available
menu = ExampleMenu("""Program main menu.
Please select a data structure type.""")

# Max heap
menu_maxheap = ExampleMaxHeap.get_menu(menu)

# Build main menu
menu.add_option("Max heap", submenu=menu_maxheap)


# Loop main menu
menu.do_menu()

# Finito
print ("\nThank you\n\n")