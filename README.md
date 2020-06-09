# DataStructures

This is a command-line program to implement fundamental data structures in Python. 
It contains both a DataStructures package (DataStructures/) 
as well as an example program (Example.py).
\
\
The main goal of this program was not to be a useful package for fundamental 
data structures in python. Instead, it was created as an exercise to practice
the implementation of data structures as well as to practice encapsulation,
data hiding, and other good programming practices. Among other consequences,
only integers are allowed as values.
\
\
**Recommended: Turn on verbose in each submenu to observe the actions of the 
data structures.**

### The Example Program

The example program has a module called ConsoleMenu.py, which allows for the easy
implementation of embedded menus in a console program in Python. Its primary classes 
and methods are the following.

    class ConsoleMenu.Menu:
        def __init__(self, title, parent_menu=None):
            # Create a new menu
           
        # Instance method
        def add_option(self, title, function=None, submenu=None):
            # Create a new menu option for this menu
            # enumerated entry values are automatically set        
            # function or submenu may be set
            #       function == reference to method
            #       submenu == reference to Menu
        
        def do_menu(self):
            # Start the menu
\
There is more to this class, but it was designed so that the internal structure is
hidden, and the only pertinent information to the programmer are these options 
<br />

### The Data Structures

The classes have the following inheritance structure

    BinaryHeap
        BinaryMaxHeap
    
    BinaryTree
        BinarySearchTree
        
    Node
        BinaryNode
            BinarySearchNode 

#### Binary Heap

The binary heap is like a binary tree that is stored contiguously in memory. 
The heap may be traversed using these rules

    # 1-indexed elements...
    
    parent(i) == i // 2;
    left(i)   == 2 * i;
    right(i)  == 2 * i + 1;
 
It may utilize a *static array* (array of fixed, finite size) or an *array list* / *dynamic array* 
(array of fixed size that doubles its allocated memory when it is full). 
For this package, the heap was implemented by mimicking an *array list*. 
This was accomplished using NumPy ndarrays of fixed length. 
When the NumPy arrays are full, double the current space is allocated.
\
\
The binary heap itself is not very helpful. If this were written in Java, 
the BinaryHeap class would be implemented as an Interface. 

#### Binary Max Heap

The binary max heap, is a very useful implementation of the binary heap that self balances
to store the largest number at the top of the heap. More explicitly, every point in the
tree must have a value greater than the values to its left and to its right. 
A similar concept is the binary min heap, which has the lowest number on the top.
This max heap property is updated when an item is added to the heap or 
when the maximum number is extracted.

    # Pseudocode: Add number
    heap[next_index] = this_value
    next_index++
    (check and update memory allocation as necessary)
    loop up tree to first element
        if parent_value < this_value
            swap(parent_value, this_value)
            this_index = parent_index
        else
            break
            
    # Pseudocode: Extract maximum number
    max_number = heap[1]        # first element (1-indexed)
    heap[1] = heap[next_index - 1]
    next_index--
    loop down tree until left and right are empty or out of bounds
        if left_value > this_value
            swap(left_value, this_value)
            this_index = left_index
        else if right_value > this_value
            swap(right_value, this_value)
            this_index = right_index
        else
            break

##### Example

With verbose on, the element in question is highlighted and shown as it traverses 
the heap. 

    Binary max heap main menu.
    Please select an option below.

	 0 :  Go back
	 1 :  Add an item to the binary max heap
	 2 :  Extract the maximum value
	 3 :  Show the heap
	 4 :  Toggle verbose on/off
	 5 :  Empty the heap
	#: 1

    Enter new integer value: 
        #: 12
    
    Before action performed.
    ********
       8    
     3   4  
    ********
    
    Value added to end of heap. Max-heap property not necessarily satisfied.
    ********************
             8          
        3         4     
     *12* 
    ********************
    
    Intermediate heap. Max-heap property not necessarily satisfied.
    ********************
             8          
       *12*       4     
      3  
    ********************
    
    Final heap. Max-heap property satisfied.
    ********************
            *12*         
        8         4     
      3  
    ********************
    
    Item 12 was added to the heap.

#### BinaryTree

A binary tree is composed of nodes, each with a key value and references to its
parent, its left child, and its right child, which are themselves nodes. The most 
interesting part about BinaryTree.py is its show() method. Unlike a heap,
whose height can be determined mathematically, the height of a binary tree is
hidden behind its web of nodes. Because the head of the tree is output first, 
we need to know how many levels there will be so that the nodes can be aligned.

The following options to output the structure were considered:
1) Keep track of the height as items are added and removed.
    * While this would work, the add and remove methods are in the classes that extend BinaryTree, not BinaryTree itself. In other words, there is a lot of potential for bugs.
    * Furthermore, while it would be quicker than determining the height at runtime, .show() is still O(n), just with lowered constants.
2) Convert to a heap-like structure and use heap .show() method.
    * This would work, but it requires O(n) time to convert to heap and worst case O(2^n) additional space!
    * Besides, the output would still be amortized O(n) with worst case O(2^n).
3) **Crawl tree for height at runtime.** 
Output tree using queue, feeding None children into None nodes, and 
stopping when all non-None nodes are printed.
    * Crawling the tree takes O(n) time.
    * Outputting the tree: amortized O(n), worst case O(2^n).

#### Binary Search Tree

Binary search trees have the property that if node is a left child, its key is 
less than this key and if the node is a right child, its key is greater than or
equal to this key. This property must be upheld when items are added or removed
from the tree.

    #Pseudocode: Add node to tree
    # Find new parent of this node
    loop through tree downwards
        if key < node.key
            if node.left is not None
                node = node.left
            else 
                new_node.parent = node
                node.left = new_node
        if key >= node.key
            if node.right is not None
                node = node.right
            else
                new_node.parent = node
                node.right = new_node
     
    #Pseudocode: Remove node from tree
    # Given node
    if node.right is None
        replace node with node.left
    else if node.left is None
        replace node with node.right
    else
        get subtree_successor, value with next highest value in node's subtree
        # Importantly, subtree_successor.left is always None, 
        # due to the binary search tree property 
        if subtree_successor == node.right
            replace node with node.right 
        else
            replace subtree_successor with subtree_successor.right
            replace node with subtree successor

##### Example

    Binary search tree main menu.
    Please select an option below.
    
         0 :  Go back
         1 :  Add an item to the tree
         2 :  Find an item in the tree
         3 :  Delete an item from the tree
         4 :  Show the tree
         5 :  Toggle verbose on/off
         6 :  Empty the tree
        #: 1
    
    Enter new integer value: 
        #: 6
    
    # Search for new parent
    ********
      _3_   
     1   4  
    ********
    ********
       3    
     1  _4_ 
    ********
    # New parent found, add key
    ****************
           3        
       1       4    
                *6*  
    ****************
    Item 6 was added to the tree
