HW_SOURCE_FILE = __file__


def insert_items(lst, entry, elem):
    """Inserts elem into lst after each occurence of entry and then returns lst.

    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> double_lst = [1, 2, 1, 2, 3, 3]
    >>> double_lst = insert_items(double_lst, 3, 4)
    >>> double_lst
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    >>> # Ban creating new lists
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'insert_items',
    ...       ['List', 'ListComp', 'Slice'])
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0   #i is the index of element in lst
    while i < len(lst): #for every element of lst
        if lst[i] == entry: #if element at i index is equal to entry
            lst.insert(i+1, elem)   #we insert elem in to i+1 index
            i = i + 2   #i is incremented by 2 so that we are only running if statement for original elements of lst
        else:
            i = i + 1   #otherwise, i is incremented by 1 for next element of ist
    return lst     #return the modified lst


def count_occurrences(t, n, x):
    """Return the number of times that x appears in the first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s2, 3, 10)
    2
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(s, 1, 3)
    1
    >>> count_occurrences(s, 4, 2)
    3
    >>> next(s)
    2
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> count_occurrences(s2, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    i = 0   #i is the index of element in t
    count = 0  #count that stores the number of times that x appears 
    while i < n:    #for all the first n elements of t
        if next(t) == x:    #if the element of t is equal to x
            count += 1  #count is incremented by 1
        i +=1   #check for next element of t
    return count    #return the total number of times that x appears in the frist n elements of t


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row.
    Iterate through the items such that if the same iterator is passed into
    the function twice, it continues in the second call at the point it left
    off in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    compare = []    #compare is an array that stores previous elements of t
    for i in range(k-1):    #length of compare is set to k-1. For example, if k is 3, we compare our current element with previous and previous previous elements.
        compare.append([])   #default, it is a list with length of k-1 with empty elements.
    
    compare.append(next(t)) #initially, add the current element of t so that there are k elements in compare
    while all(elem == compare[0] for elem in compare) == False: #if all the elements of compare are not the same, so if the current elemet did not appear k times in a row
        compare.pop(0)  #remove the oldest previous element from compare
        compare.append(next(t)) #move on to next element of t 
    return compare[0] #if all the elements of compare are the same, return any element from compare which is the first element that appeared k times in a row.
