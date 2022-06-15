HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if pos == 0:    #if there is no more digit left to check, return 0
        return 0
    else:
        if pos%10 == 8:     #if the last digit of pos is equal to 8
            return 1 + num_eights(pos//10)      #return 1(the counter is incremented by 1) added by recursive function num_eights with argument of n without the last digit
        else:   #if the last digit of pos is not equal to 8
            return num_eights(pos//10)  #the counter is not incremented so just return recursive function num_eights with argument of n without the last digit



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(x, c, operation):        #define helper function. x is the ping pong value. c is the index of pingpong value. operation is true if direction is an addition. operation is false if direction is a substitution.
        if c == n:      #if the index reaches  n
            return x    #return that index's ping pong value
        elif num_eights(c) > 0 or c % 8 == 0:   #if the index contained a digit of 8 or is a multiple of 8
            if operation:   #if direction was an addition
                return helper(x-1, c+1, False)  #return recursive helper function with next ping pong value(decreased by 1), increased index, and the direction of substitution.
            else:   #if direction was a substitution
                return helper(x+1, c+1, True)    #return recursive helper function with next ping pong value(increased by 1), increased index, and the direction of addition.
        else:   #if index did not contain a digit of 8 and is not a multiple of 8
            if operation:   #if direction was an addition
                return helper(x+1, c+1, True)   #keeps the same direction with increased index and ping pong value
            else:   #if direction was a substitution
                return helper(x-1, c+1, False)  #keeps the same direction with increased index and decreased ping pong value
    return helper(1, 1, True)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4

    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:  #if n is one digit number,
        return 0    #no missing numbers between n and n
    def helper(x, last, count): #helper function. x is the number without the last digit. last is n's last digit. count is the number of missing digit.
        if x < 10:  #if number without the last digit is 1 digit
            if count > 0:   #when counter is greater than 0
                return count - x    #decrease the count by x because it is range exclusive
            else:   #when counter is 0
                return count    #output count that is 0
        elif x % 10 == last:    #if the two adjacent digits are equal
            return helper(x//10, x%10, count)   #don't decrease the counter and return recursive helper function with x without its last digit, its last digit and same counter value again
        else:    #if the present number is smaller than previous number,  
            return helper(x//10, x%10, count - 1)   #decrease count by 1 and return recursive helper function with x without its last digit, its last digit and same counter value again
    return helper(n // 10, n % 10, n % 10 - 1) #return helper with n without its last digit, its last digit and counter is initially set to last digit -1 as it is range exclusive.


def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(amount, minimum): #helper function. amount is total remaning change to calculate. minimum is minimum value of coin that can be used to produce the change.
        if amount < 0:  #if the amount is less than 0,
            return 0    #it is impossible to give a negative change, so return 0
        elif minimum == None:   #if the value of minimum coin is greater than 25 cents,
            return 0    #it is impossible to give a coin that is greater than 25 cents, so return 0
        elif amount == 0:   #if the remaining amount ot calculate for change is 0
            return 1    #we found one way to produce the change so return 1
        else:   #if there are still some remaining amounts to calculate for change
            with_minimum = helper(amount-minimum, minimum)  #check the ways of reaching the original change by using the minimum value of coin
            without_minimum = helper(amount, ascending_coin(minimum))   #check the ways of reaching the orignal change without using the minimum value of coin
            return with_minimum + without_minimum   #combin the two ways mentioned above to return the total number of ways to produce the change
    return helper(change, 1)    #initially amount is change and minimum coin is 1.


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
