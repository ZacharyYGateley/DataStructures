from DataStructures.BinaryMaxHeap import BinaryMaxHeap
from ExampleMenu import ExampleMenu as em

myHeap = BinaryMaxHeap()
verbose = False

def add():
    """Add a new item to the max heap"""
    print ('\nEnter new integer value: ')
    new_value = em.get_int()
    print ('\n', end='')
    myHeap.add_item(new_value, verbose=verbose)

def extract():
    """Extract an item from the max heap"""
    print ('\n', end='')
    max_value = myHeap.extract_max(verbose=verbose)
    print ('The maximum value has been extracted and is', max_value, end='')

def show():
    """Show the max heap"""
    print ('\n', end='')
    myHeap.show()

def toggle_verbose():
    """Turn max heap verbose on/off"""
    verbose = ~verbose