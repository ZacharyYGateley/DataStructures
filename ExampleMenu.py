from collections import OrderedDict


class InvalidMenuOption(Exception):
    """Low priority exception for invalid menu option"""
    def __init__(self):
        pass


class MenuOption:
    """
    One single menu option within a menu

    May either call a function or open a submenu, not both

    Attributes:
        key (int): entry number in menu
        title (str): what shows up on the line to the user
        function (obj): menu option calls function
        submenu (ExampleMenu): menu option opens submenu
    """

    key = 0
    title = ""
    # Either function set
    function = None
    # Or submenu set
    submenu = None

    def __init__(self, key, title, function=None, submenu=None):
        assert(title != "", "Menu option must have a title")
        # Only function or submenu may be set
        # Exactly one of the two must be set
        is_function_none =
        assert(function is not None or submenu is not None)
        assert(~(function is None) ^ ~(submenu is None), "Only function or submenu may be set")

        self.key = key
        self.title = title
        self.function = function
        self.submenu = submenu

    def get_title(self):
        """Get title (practice information hiding)"""
        return self.title

    def enact(self):
        """
        Perform action of menu option
        Call function
        Or open submenu
        """
        if self.function is not None:
            self.function()

        if self.submenu is not None:
            self.submenu.do_menu()


class ExampleMenu:
    """
    One list of menu options that link to other functions or submenus

    Attributes:
        title (str): title of menu itself, shows above options
        options (OrderedDict): ordered list of menu options
        parent (ExampleMenu): parent menu of this
            Top level: shows "Exit"
            All sub levels: show "Back"
        exit (bool): Flag to show that exit is needed
        next_enum (int): next enum value for this menu
    """

    title = ""
    options = OrderedDict()
    parent = None
    exit = False
    next_enum = 0

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
                integer = int(input())
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

    def __init__(self, title="", parent=None):
        assert(title != "", "ExampleMenus must have titles")
        self.title = title

        # Add back/exit option
        optttl = ""
        function = None
        submenu = None
        if parent is not None:
            optttl = "Go back"
            submenu = parent
        else:
            optttl = "Exit"
            function = self.do_exit
        self.add_option(optttl, function=function, submenu=submenu)

    def add_option(self, title, function=None, submenu=None):
        """
        Add menu option to menu
        :param title: string title of menu option
        :param function: menu option calls function
        :param submenu: menu option opens submenu
        :returns: no return value
        """

        new_enum = self.get_enum()
        new_option = MenuOption(new_enum, title, function=function, submenu=submenu)

        self.options[new_enum] = new_option

    def do_menu(self):
        """Show menu"""

        # Show title of menu
        print (self.title)

        # Print options
        for enum, option in self.options.items():
            print ("\t", enum, ": ", option.get_title())

        # Get input selection
        self.exit = False
        while True:
            selection = ExampleMenu.get_int()

            # Loop options to see if valid
            valid_option = False
            for option in self.options:
                if selection == option.key():
                    option.enact()
                    valid_option = True

            # Exit option was chosen
            if self.exit:
                break

        # Previous menu is waiting

    def do_exit(self):
        """
        Flag to exit menu
        Submenu is waiting
        Or program main is waiting and will exit
        """
        self.exit = True
