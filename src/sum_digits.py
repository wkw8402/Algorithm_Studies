def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    ff = 1     #ff stands for the value of falling factorial. Since it is of multiplication, it needs to start from 1
    while k > 0:    #unitl the depth is 0
        ff *= n    #multiply n: repetition will cumulatively find the falling factorial
        n, k = n-1, k-1 #depth k is falling as well as the factorial value n
    return ff     #return the final falling factorial


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    sd = 0  #sd stands for sum_digits, starts with 0 as it will be the result of addition
    while y != 0:   #until y has a digit that is 0
        sd += y % 10    #add the last digit to sd
        y //= 10    #remove the last digit from y
    return sd   #return the sum_digits




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    determine = False   #determine is a boolean that is only true if the digits contain two adjacent 8s. It is set to False as a default value.
    while n > 10:   #n has to have a minimum of two digits for determine to be true
        current = n % 10    #current is the last digit of current n
        next = ((n // 10) % 10) #next is the second last digit of current n
        if current == 8 and current == next:    #if current is equal to 8 and if current and next are equal
            determine = True    #determine becomes true
        n //= 10    #moving on to next n by removing the last digit of current n
    return determine    #finally return the determine's boolean value
