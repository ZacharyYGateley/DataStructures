from collections import OrderedDict


class InvalidMenuOption(Exception):
    """Low priority exception for invalid menu option"""
    def __init__(self):
        pass


class Option:
    """
    One single menu option within a menu

    May either call a function or open a submenu, not both

    Attributes:
        key (int): entry number in menu
        title (str): what shows up on the line to the user
        function (obj): menu option calls function
        submenu (Menu): menu option opens submenu
    """

    def __init__(self, key, title, function=None, submenu=None):
        # Only function or submenu may be set
        # Exactly one of the two must be set
        is_function_none = function is None
        is_submenu_none  = submenu  is None
        assert(~is_function_none ^ ~is_submenu_none)

        self.key = key
        self.title = title
        self.function = function
        self.submenu = submenu

    def get_title(self):
        """Get title (practice information hiding)"""
        return self.title

    def is_submenu(self):
        """
        Check if this option leads to a submenu
        :returns: True (option leads to submenu) or False (doesn't)"""
        return self.submenu is not None

    def enact(self):
        """
        Perform action of menu option
        Call function
        Or open submenu
        """
        # If a valid option is being performed,
        # separate it from the prior interface
        print ("\n", end='')
        if self.function is not None:
            self.function()
        elif self.submenu is not None:
            self.submenu.do_menu()


class Menu:
    """
    One list of menu options that link to other functions or submenus

    Attributes:
        title (str): title of menu itself, shows above options
        options (OrderedDict): ordered list of menu options
        parent (Menu): parent menu of this
            Top level: shows "Exit"
            All sub levels: show "Back"
        exit (bool): Flag to show that exit is needed
        next_enum (int): next enum value for this menu
    """

    @staticmethod
    def get_int():
        """
        Loop until a valid integer has been entered
        :return: valid integer
        """
        integer = 0
        while True:
            print('\t#: ', end='')
            try:
                selection = input()
                if selection == '':
                    raise InvalidMenuOption
                integer = int(selection)
                break
            except InvalidMenuOption:
                print('Please enter a valid integer')
        return integer

    def get_enum(self) -> int:
        """
        Returns unique enum value
        :return:
        """
        enum = self.next_enum
        self.next_enum = self.next_enum + 1
        return enum

    def __init__(self, title, parent_menu=None):
        """
        Initializes a new menu, automatically adding a menu option
        "Exit" or "Go back" as necessary depending on whether
        there is a parent menu.
        :param title: str Title to be shown above menu options
        :param parent_menu: if not None, first option is Go Back to this menu
                            if None, first option is Exit, closes the program
        """

        # Init instance variables
        self.title = title
        self.options = OrderedDict()
        self.parent = parent_menu
        self.exit = False
        self.next_enum = 0

        # Add back/exit option
        opt_title = "Exit"
        if parent_menu is not None:
            opt_title = "Go back"
        function = self.do_exit
        submenu = None
        self.add_option(opt_title, function=function, submenu=submenu)

    def add_option(self, title, function=None, submenu=None):
        """
        Add menu option to menu
        :param title: string title of menu option
        :param function: menu option calls function
        :param submenu: menu option opens submenu
        :returns: no return value
        """

        new_enum = self.get_enum()
        new_option = Option(new_enum, title, function=function, submenu=submenu)

        self.options[new_enum] = new_option

    def do_menu(self):
        """Show menu"""

        # Get input selection
        option = None
        self.exit = False
        while True:
            # Show title of menu and options on each iteration
            print(self.title)
            for enum, option in self.options.items():
                print("\t", enum, ": ", option.get_title())

            selection = Menu.get_int()

            # Loop options to see if valid
            valid_option = False
            for key, option in self.options.items():
                if selection == key:
                    option.enact()
                    valid_option = True
                    break

            # If no option was called, print an error message
            if not valid_option:
                print ("\nPlease select a valid menu option")

            # Exit option was chosen
            if self.exit:
                break

            # Space between menus
            print ("\n", end='')

        # Previous menu is waiting

    def do_exit(self):
        """
        Flag to exit menu
        Submenu is waiting
        Or program main is waiting and will exit
        """
        self.exit = True
