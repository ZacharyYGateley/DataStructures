from DataStructures import MaxHeap

myHeap = MaxHeap.MaxHeap()


class Options:
    """
    Main menu options
    """
    # Emulate enumerators
    EXIT = 0
    ADD = 1
    EXTRACT = 2
    SHOW = 3
    VERBOSE = 4

    # Option titles stored here
    titles = []

    def __init__(self):
        self.titles.append(str(Options.EXIT) + ': Exit')
        self.titles.append(str(Options.ADD) + ': Add an item')
        self.titles.append(str(Options.EXTRACT) + ': Extract the maximum value')
        self.titles.append(str(Options.SHOW) + ': Show the max heap')
        self.titles.append(str(Options.VERBOSE) + ': Toggle verbose on/off')

    def show(self, line_starter='\t'):
        """
        Print menu options on separate lines
        """
        print ('\n'.join(line_starter + title for title in self.titles))


def get_int():
    """
    Loop until a valid integer has been entered
    :return: valid integer
    """
    integer = 0
    while True:
        print ('\t#: ', end='')
        try:
            integer = int(input())
            break
        except:
            print ('Please enter a valid integer')
    return integer


# Loop main menu
print ('Max heap main menu:\n')
options = Options()
finish = False
verbose = False
while not finish:
    # Options:
    print ('Please select an option (Verbose ', 'on' if verbose else 'off', ')\n', sep='')
    options.show()
    selection = get_int()

    if selection == Options.ADD:
        # Add item
        print ('\nEnter new integer value: ')
        new_value = get_int()
        print ('\n', end='')
        myHeap.add_item(new_value, verbose=verbose)
    elif selection == Options.EXTRACT:
        # Pop max
        print ('\n', end='')
        max_value = myHeap.extract_max(verbose=verbose)
        print ('The maximum value has been extracted and is', max_value, '\n')
    elif selection == Options.SHOW:
        # Show heap
        print ('\n', end='')
        myHeap.show()
        print ('\n', end='')
    elif selection == Options.VERBOSE:
        # Toggle verbose on/off
        verbose = ~verbose
        print ('\n', end='')
    elif selection == Options.EXIT:
        # Exit
        finish = True
    else:
        # Invalid input
        print ("\nYour selection was invalid, please enter a different selection\n")

# Finito
print ("\nThank you\n\n")