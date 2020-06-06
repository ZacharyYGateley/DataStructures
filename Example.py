from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from ConsoleMenu import Menu
from ExampleFunctions import MaxHeap, BST

myHeap = BinaryMaxHeap()


# Build menus
# Build submenus before main menu
# so that references are available
menu = Menu("""Program main menu.
Please select a data structure type.""")

# Max heap
menu_maxheap = MaxHeap.get_menu(menu)
menu_bst = BST.get_menu(menu)

# Build main menu
menu.add_option("Binary max heap", submenu=menu_maxheap)
menu.add_option("Binary search tree", submenu=menu_bst)


# Loop main menu
menu.do_menu()

# Finito
print ("\nThank you\n\n")