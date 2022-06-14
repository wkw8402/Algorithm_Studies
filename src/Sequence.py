def gen_perms(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = gen_perms([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(gen_perms([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(gen_perms((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(gen_perms("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if len(seq) == 1:   #if the length of seq argument is 1
            yield [seq[0]]  #there is only one possible permutation for a single element of seq
    else:   #if seq argument has more than one elements
        for i in range(len(seq)):   #for each and every elements of the seq list. i becomes the index of element that we just used to form a permutation
            for gp in gen_perms(seq[:i]+seq[i+1:]): #for each and every recursive gen_perms function on new seq argument which is without the previously used element. As we are popping the element at index i from seq list, gen_perms recursion is now creating a permutation without the used elements.
                yield [seq[i]] + gp #we are able to yield a list containing a possible permutation of elements from the original seq as we yielded and popped all the elements until the lastly remainng element. The last element remaining is also finally yielded by recursion of line 24 and 25 inside the same list.


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label
    value as a list.

    >>> t1 = tree(1, [tree(2, [tree(3), tree(4, [tree(6)]), tree(5)]), tree(5)])
    >>> print_tree(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = tree(0, [tree(2, [t1])])
    >>> print_tree(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** YOUR CODE HERE ***"
    step = label(t) #step indicates our current phase in a potential path that might lead us to our wanted value, hence step is always the label or root of a tree
    if step == value:   #if step is equal to the value, so if this step is the last phase of a path
        yield [step]    #yield the list containing this step as we found a path to value 
    for b in branches(t):   #for each and every branches of t
        for py in path_yielder(b, value):   #for each and every path_yielders on each and every branch
                yield [step] + py #yield the list containing all the previous steps we passed through to find a value. in short, we are yielding one possible path at a time by using the two yield statements.

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    outcome = []    #outcome is the list that stores all the entries in the tree     
    if Tree.is_leaf(t): #if t is a leaf
        return label(t) #return its label/root of tree
    else:
        outcome.append(label(t))    #if t has branches, first add the label of t to the outcome 
        for b in branches(t):   #for each and every branches of t
            if isinstance(preorder(b), int):   #if the return value from recursive preorder function on any branch is an integer, so if a branch of t is a leaf
                outcome.append(preorder(b)) #add that returning integer to outcome by append 
            else:   #if the return value from recursive preorder function on any branch is a list, so if a branch of t is also a branch 
                outcome.extend(preorder(b)) #add that returning list to outcome by extend
    return outcome  #finally, return the list containing every entries of tree in the preorder traversal order

def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    if Tree.is_leaf(t):     
        yield label(t)  #if t is a leaf, yield t's label directly
    else:
        yield label(t)  #if t is not a leaf, first yield its label
        for b in branches(t):   #for each and every branches of t
            yield from generate_preorder(b) #since the recursive generate_preorder function on each branch becomes the iterable, yielding from this recursion enables us to yield the label of all existing trees(including both branches and leaves) by using the two yield statements above. 

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


tree = lambda label, branches=[]: Tree(label, branches)
label = lambda t: t.label
branches = lambda t: t.branches
print_tree = lambda t: print(t)


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1
