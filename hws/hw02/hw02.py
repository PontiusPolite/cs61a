HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

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
    if x == 0:
        return 0
    elif x % 10 == 8: # if 8 is last digit
        return 1 + num_eights(x//10)
    else: # if 8 is not last digit
        return num_eights(x//10)



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
    # pingpong(n) = pingpong(n-1) + inc(n)
    # inc(n) = inc(n-1) * -1 if n-1 meets the pingpong criteria
    def inc(n):
        if n == 1:
            return 1
        elif num_eights(n-1) >= 1 or (n-1) % 8 == 0:
            return inc(n-1) * -1
        else:
            return inc(n-1)

    if n == 1:
        return 1
    else:
        return pingpong(n-1) + inc(n) 


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
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
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    
    if n // 10 == 0: # Single digit has nothing missing
        return 0
    elif n // 10 % 10 + 1 < n % 10: # If last two digits have something missing (ie, same or not sequential)
        # print(n % 10 - 1) # this line prints the missing digits
        return 1 + missing_digits(n-1) # increment last digit down and check again (+1 missing digits)
    else: # if the last two digits are the same
        return missing_digits(n//10) # remove last digit and continue
    



def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """

    # counts the coin combinations of total using at least the smallest coin or higher
    def count_parts(total, smallest_coin):
        if total < 0: # can't count negative coins
            return 0
        elif smallest_coin == None: # can't count with nothing
            return 0
        elif smallest_coin == total: # 1 way to count something when coin is the same
            return 1
        else:
            with_smallest = count_parts(total - smallest_coin, smallest_coin) # 2
            without_smallest = count_parts(total, next_largest_coin(smallest_coin)) # 0
            return with_smallest + without_smallest
    
    return count_parts(total, 1)


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
    helper = (lambda f: lambda n: f(f, n))
    # helper takes as arguments a function f that takes itself and a number n as arguments,
    # and then returns f applied to itself and n
    # We can pass in a function into helper that, since the helper applies this function to itself, 
    # will be called recursively 
    # helper(h)(n) = h(h, n) where h = a function with arguments of itself and a number, 
    # i.e.: h = g(g, x)
    recursive_function = lambda g, x: 1 if x == 1 else mul(x, g(g, sub(x-1)))


    return helper(recursive_function) # can be substituted with lambda expressions

print(make_anonymous_factorial()(5)) # 120

    # return a function that takes in n and returns factorial of n

    # (lambda f: lambda n: f(f, n))(f) -> (lambda n: f(f, n))(n) -> f(f, n)




(lambda f: lambda n: f(f, n))(lambda g, x: 1 if x == 0 else x * g(g, x-1))