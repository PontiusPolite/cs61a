# UC Berkeley CS61A: Structure and Interpretation of Computer Programs
https://inst.eecs.berkeley.edu/~cs61a/fa20/

Course Notes

## The Basics
Base of most languages:
    -primitive expressions and statements, which represent the simplest building blocks that the language provides,
    -means of combination, by which compound elements are built from simpler ones, and
    -means of abstraction, by which compound elements can be named and manipulated as units.
    ```
    from _typeshed import SupportsTrunc
    from operator import floordiv, mod, add

    def divide_exact(n, d):
        """Return the quotient and remainder of dividing N by D.

        >>> q, r = divide_exact(2013, 10)
        >>> q
        201
        >>> r
        3
        """
        return floordiv(n, d), mod(n, d)
    ```

## Higher Order Functions
- a function that returns a function
- for example, currying - converting f(x, y) to f(x)(y)
- curry(f) returns a function g that takes in x. g(x) returns a function h that takes in y
- h(y) returns f(x, y) 
```
def curry(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
```

## Lambda Functions
lambda x: f(g(x))
- A function that    takes x    and returns     f(g(x))

lambda x: x + 5 is equivalent to
    
    def a_function(x):
        return x + 5

- the lambda function has no intrinsic name, but can be given a bound name:
`f = lambda x, y: x * y`
```
    def lambda_curry(f):
        return lambda x: lambda y: f(x, y)
        # return a function that takes x and returns: a function that takes y and returns: f(x, y)
        # add(2, 3) = curry_add(2)(3)

    curry_add = lambda_curry(add)
    def split(n):
        return n // 10, n % 10
```

## Decorators 
- use higher order functions
- The below line binds remove to the return value of trace1(remove). It's equivalent to saying remove = trace1(remove)

```
def trace1(f):
    """returns a version of function f that prints it's name and arguments when called"""
    def traced_function(x, y):
        print(f"{f}({x}, {y}) -> {f(x,y)}")
        return f(x, y)
    return traced_function

@trace1
def remove(n, digit):
    """Remove the specified digit from non-negative n
    
    >>> remove(231, 3)
    21
    >>> remove(243132742, 2)
    431374
    """

    kept, digits = 0, 0
    while n > 0:
        n, last  = n // 10, n % 10
        if last != digit:
            kept += (last * 10 ** digits)
            digits += 1
    return kept
```

## Recursive Functions
- always includes the base case, and the recursive case
- iteration is a special case of recursion

```
def sum_digits(n):
    if n < 10: # base case, always in recursive functions
        return n
    else: # recursive case
        all_but_last, last = split()
        return sum_digits(all_but_last) + last

def factorial(n):
    #assert n >= 0, "n should be a positive integer"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```


## Tree Recursion
- arises whenever the recursive function makes more than one call to itself
```
@trace1
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n-2) + fibonnaci(n-1)

def count_partitions(n, m):
    """Return the number of partitions of n using a maximum partition size of m
    
    Example of 5, 3:
    1 + 1 + 3           } partitions with m included
    2 + 3               }

    1 + 2 + 2           } partitions without m included  
    1 + 1 + 1 + 2       }      
    1 + 1 + 1 + 1 + 1   } 

    >>> count_partitions(5, 3)
    5    
    """
    # base cases
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    # recursive case
    else:
        with_m = count_partitions(n-m, m) # count the partitions that include m in the partition
        without_m = count_partitions(n, m-1) # count the partitions that don't have m included
        return with_m + without_m

```

## CONTAINERS

```
list_ex = [1, 2, 3]
list_ex[0]
# This is a call expression, so the argument is evaluated, then the whole expression 
```

## FOR STATEMENT
```
    for <name> in <expression>:
        <suite>
```
Execution procedure
1. Evaluate the header <expression>, which must yield an iterable
2. For each element in the sequence:
    a. Bind <name> to that element in the current frame
    b. Execute the entire suite

```
def count(s, value):
    total = 0
    # Sequence Iteration
    for element in s: # the name element is bound in the firt frame of current environment
        if element == value: # then the suite of the For statement is executed
            total += 1
    return total

# Sequence unpacking
#   -only works for sequence of fixed-length sequences
pairs = [[1, 2], [2, 2], [4, 4], [3, 4]]
for x, y in pairs: # x and y are bound to elements in each nested sequence
    pass

# List constructor
x = list(range(-2, 2))
# x = [-2, -1, 0, 1]

def recursive_sum(a_list):
    if a_list == []:
        return 0
    else:
        return recursive_sum(a_list[0:-1]) + a_list[-1]

# List Comprehensions
odds = [1, 3, 5, 7, 9]
evens = [x+1 for x in odds] # [2, 4, 6, 8, 10]
factor_of_25 = [x for x in odds if 25 % x == 0] # [1, 5]

```

## STRINGS
- strings are sequences

```
# String execution
exec("g = lambda y: y + 2") # g(2) -> 4

def recursive_string_reverse(s):
    if len(s) == 1:
        return s
    else:
        return recursive_string_reverse(s[1:]) + s[0]
```

## DATA ABSTRACTION
- a methodology by which functions enforce an abstraction barrier between
representation and use
Example: rational numbers
```
rational(n, d) returns a rational number x   } constructor
numer(x) returns the numerator of x          } selectors
denom(x) returns the denominator             }
```
- These three functions implement an abstract data type
- Arithmetic implementation, in terms of constructor and selectors
```
def mul_rational(x, y):
    return rational(numer(x) * numer(y),
                    denom(x) * denom(y))



# rational data implemented as functions, rather than say a list
def rational(n, d):
    def select(name):
        if name == "n":
            return n
        elif name == "d":
            return d
    return select

def numer(x):
    return x("n")

def denom(x):
    return x("d")
```

## TREES
- A Tree has a root label, and a list of branches
- Each branch is itself another Tree (with a label and a list of branches)
- If a Tree has no branches, (i.e., branches = []), it is called a Leaf

Implementing a tree abstraction below:
```

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "One of your branches is not a tree!"
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

test_tree = tree(1, [tree(5, [tree(7)]), tree(6)])

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(t)]
        return sum(branch_counts) 

def leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        leaf_list = [leaves(b) for b in branches(t)]
        return sum(leaf_list, [])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        new_branches = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), new_branches) 

def increment(t):
    """Returns a tree with all labels incremented"""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])
    # We don't need a base case, because when branches[t] is [], no recursive call is made

def print_tree(t, indent=0):
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
    
```

## BINARY NUMBERS

Negative Numbers
- Represented with two's complement 
1. Start with unsigned binary number where left-most bit is 0 
    - 0110 = 6
2. Complement your binary number (flip bits)
    - 1001
3. Add one to your binary number
    - 1010

n-bit signed binary numbers: -2^(n-1)...2^(n-1)-1

0 000 -> 111 -> 000  0 
1 001 -> 110 -> 111 -1
2 010 -> 101 -> 110 -2
3 011 -> 100 -> 101 -3
                100 -4 

Two's Complement is nice for the computer, less nice for human eyes

Fractional Numbers
(+/- mantissa) * base ^ (+/- exponent)


## MUTABLE FUNCTIONS
- function with behavior that changes over time
    - object methods behave differently based on object attribute values

- Expressions that can be replaced with its values and not change the program are
  'referentially transparent', i.e. mul(3, 5) -> 15
    - mutable functions can not be referentially transparent

```
def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""

    def withdraw(amount):
        nonlocal balance 
        # All assignments of balance will be applied to balance in the first non-local frame
        # First non-local frame also called "enclosing scope" in Python docs
        # Before we could look up values in the parent frame - now we can change them
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        return balance

    return withdraw

def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    
    >>> combo(531, 432)
    45312
    """
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10
    return min(combo(a // 10, b) * 10 + a % 10, combo(a, b // 10) * 10 + b % 10)

    

```

## ITERATORS
- a container can provide an iterator that provides access to its elements in some order
    - think of an iterator as a marker that moves forward when next() is called
        - the marker starts at 0, and the iterator contains everything after the marker
    - multiple iterators can be created from the same container

- in Python 3, dictionaries are ordered according to order in which items were added
    - if you change the size of a dictionary while iterating, you must construct a new iterator

Built-In Functions:
- These are lazy, in that they're only called when used (not immediately) 
    - map(func, iterable): Iterate over func(x) for x in iterable. Returns an iterator.
    - filter(func, iterable)
    - zip(iterable_1, iterable_2)
    - reverse(sequence)

    - list(iterable)
    - tuple(iterable)
    - sorted(iterable)

```
s = [3, 4, 5]
t = iter(s)
next(t) # 3
next(t) # 4
```

## GENERATOR FUNCTIONS
- return an iterator using 'yield' statements
    - can yield multiple times

- the body of a generator is not executed until next() is called, where it executes until a yield
  statement is reached. The it pauses until the next value is needed
    -this is lazy, in that the computation isn't done until needed

- a 'yield from' statement can yield from an iterator/iterable. The following are equivalent:

```
for x in a:     |     yield from a
    yield x     |

def plus_minus(x):
    yield x
    yield -x

t = plus_minus(3)
next(t) # 3
next(t)

def prefixes(s):
    if s: # if s is non-empty
        yield from prefixes(s[:-1])
        yield s

list[prefixes('both')] # ['b', 'bo', 'bot', 'both']

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
```


## OBJECTS

- A Class combines and abstracts data and functions
- Object is instantiation of a class

- A class statement creates a new class and binds the class to the given name in the first frame
  of the current environment
- Assigment and def statements in the class create attributes, not names in frames
- Objects receive messages via dot notation
    Dot expression: <expression>.<name>
                    <expression>.<method-name>
- A Method is an attribute that is a function
    - tom_account.deposit(100) is a method, where tom_account is  passed in as the first
      argument in deposit

```
class Account:
    interest = 0.02 # a class attribute
    def __init__(self, account_holder): # class constructor
        self.balance = 0 # this will be an attribute of the instance. The instance is bound to self. 
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        self.balance -= amount
        return self.balance
```

## INHERITANCE
```
class <name>(<base class>):
    <suite>
```
- This new class inherits from the base class
- base class attributes aren't copied into subclasses!

- Inheritance is best to represent an 'is-a' relationship
- Composition (when one object has another one as an attribute) is best when they have
  a 'has-a' relationship

```
class CheckingAccount(Account):
    """A bank account that charges for withdrawals"""
    withdraw_fee = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
    """A bank 'has' accounts.
    
    >>> bank = Bank()
    >>> john = bank.open_account("John", 10)
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return Account
    
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1 

```
## MULTIPLE INHERITANCE

```
class SavingsAccount(Account):
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)

class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1
```

### STRING REPRESENTATIONS
- In python, all objects produce two string representations
    - str is legible to humans
    - repr is legible to the interpreter
        - calling repr is what is displayed in the python console
        - evel(repr(expression)) will usually return the expression
    - these are often the same
    - print() will invoke the str method, which invoes __str__() see below



POLYMORPHIC FUNCTIONS
- can be applied to many types of data
- str and repr are both polymorphic
    - invoke __repr__() and __str__() respectively
    - these are implented as class attributes
    - str is technically a class, not a function 

- an Interface is a set of shared attribute names that elicit similar behavior from different classes

```
def repr(x):
    return type(x).__repr__(x) # this makes sure the instance attribute is ignored
```

## SPECIAL METHOD NAMES IN PYTHON
- start and end with two underscores, and interact with built in python stuff

__init__, __repr__, __add__, __bool__, __float__
__radd__ (this reverse the order of addition when you're working with non-commutative stuff)

Ratio(1, 3) + Ratio(1, 6) is eqivalent to 
Ratio(1, 3).__add__(Ratio(1, 6))
    - This allows us to customize what these special methods to in user-created classes


Side note: isInstance() is different than type(). isInstance will see if that object is any
    of the subclasses as well. 

```
from math import gcd

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d
    
    def __add__(self, other): # this will be invoked when using '+' between ratios
        n = self.numer * other.denom + self.denom * other.numer
        d = self.denom * other.denom
        g = gcd(n, d)
        return Ratio(n // g, d // g)
```

## LINKED-LISTS
- either empty, or a first value and the rest of the linked list

Link(3, Link(4, Link(5, Link.empty)))

```
class Link:
    
    empty = () # some zero-length sequence

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

s = Link(3, Link(4, Link(5, Link.empty)))
s.first # 3
s.rest.first # 4
s.rest.rest.first # 5
s.rest.rest.rest is Link.empty # True
```

Recursion is very common for processing linked list

```
def range_link(start, end):
    """Return a Link containing consecutive ints from start to end."""
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))

def map_link(f, s):
    """Return a Link that contains f(x) for each x in Link s."""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link that contains only the elements of x of Link s for which f(x) is True"""
    if s is Link.empty:
        return s
    elif f(s.first):
        return Link(s.first, filter_link(f, s.rest))
    else:
        return filter_link(f, s.rest)

def add(s, v):
    """Add v to an ordered list s with no repeats, returning modified s."""
    assert s is not Link.empty
    if s.first > v:
        s.rest = Link(s.first, s.rest)
        s.first = v
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v, Link.empty)
    elif s.first < v:
        s.rest = add(s.rest, v)
    return s
```

## MODULAR DESIGN
- Separation of Concerns: isolate different parts of a program that address different concerns
- modular components can be developed/tested independently


## MANIPULATING ITERABABLES EXAMPLE PROBLEMS

```
def get_smallest_indices(s):
    """Return a list of indices of all the elements in s with the smallest absolute value.
    >>> get_smallest_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    """
    return [i for i in range(len(s)) if min(map(abs, s)) == abs(s[i])]
    # could also use filter

def get_largest_adjacent_sum(s):
    """Return the largest sum of two adjacent elements in s.
    >>> get_largest_adjacent_sum([-4, -3, -2, 3, 2, 4])
    6
    """
    return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    return max(x + y for x, y in zip(s[:-1], s[1:]))

def create_digit_dictionary(s):
    """Create a dictionary mapping each digit d to a list of elements in s that end with d."""
    # dic = {}
    # for x in s:
    #     if x % 10 not in dic:
    #         dic[x % 10] = [x]
    #     else:
    #         dic[x % 10].append(x)
    # return dic
    return {d: [x for x in s if x % 10 ==d] for d in [y % 10 for y in s]}

def elements_equal(s):
    """Return True if every element is equal to some other element in s."""
    # counts = {}
    # for x in s:
    #     if x not in counts:
    #         counts[x] = 1
    #     else: 
    #         counts[x] += 1
    # for c in counts:
    #     if counts[x] < 2:
    #         return False
    # return True
    return all([s[i] in s[:i] + s[i + 1:] for i in range(len(s) - 1)])
```

## EXCEPTIONS
- a built in mechanism to declare and respond to exceptional conditions.
- Python raises an exception when an error occurs.
- Unhandled exceptions will cause Python to halt excecution and print a stack trace.

Exceptions are objects.
They enable non-local continuations of control.
    - if f calls g and g calls h, exceptions can shift control from h to f without waiting for g

Assert Statement
    - assert <expresssion>, string
    - raises an AssertionError
    - designed to be used liberally, can be ignored by python -0 command
    - the bool __debug__ determines if assertions are raised

Raise Statement
    - raise <expression>
    - <expression> must evaluate to a subclass of BaseException
    - I.e., TypeError, NameError, KeyError, RuntimeError
        - Constructed like object - TypeError("Bad argument")

Try Statements

```
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```

- the try suite is executed first
- if during execution an exception is raised and the exception inherits from 
    the <exception class>, the except suite is executed
    - the exception message is bound to name


```
try:
    x = 1/0
except ZeroDivisionError as e:
    print("Handling a",  type(e))
    x = 0

def invert(x):
    y = 1/x
    print("Never printed if x is 0")
    return y

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        print("handled", e)
        return 0

# >>> invert_safe(2)
# 0.5
# >>> invert_safe(0)
# handled division by zero
# 0

def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.
    
    >>> reduce(mul, [2, 4, 8], 1)
    64
    """
    for x in s:
        initial = f(initial, x)
    return initial
```

## INTERPRETERS

- Programming Languages are like trees, with lists of sub expressions
    - Syntax: the legal statements and expressions
    - Semantics: the evaluation rules for those statements and expressions

Parsing
- a parser takes text and returns expressions
TEXT -> LEXICAL ANALYSIS -> TOKENS -> SYNTACTIC ANALYSIS -> EXPRESSIONS

- Lexical analysis: iterative process, checks one line at a time and determines
the types of tokens
- Syntactic analysis: tree-recursive process, balances parentheses, processes multiple lines
    - Base case: symbols and numbers
    - Recursive call: read sub-expressions and combine them

Read-Eval-Print-Loop
    - Print a prompt
    - Read text input
    - Parse the input into an expression
    - Evaluate the expression
    - If any errors occur, report them
    - Print the value of the expression and repeat

Exceptions are raised everywhere in an interpreter

## DECLARITIVE PROGRAMMING LANGUAGES
- A program is a description of the desired result
- versus imperative languages, which descibe a computational process

Database Management Systems
- SQL

create table cities as
    select 38 as latitude, 122 as longitude, "Berkeley" as name union
    select 42,             71,               "Cambridge"        union
    select 45,             93,               "Minneapolis";

Joining Tables
- Two tables A & B are joined by a comma to yield all combos of a row from A & a row from B

select * from parents, dogs where child=name;

Aliases and Dot Expressions
- Two tables may share a column name, but these help disambiguate

    select [columns] from [table] where [condition] order by [order];

```
Ex.: selecting pairs of siblings from dog table:
    select a.child as first, b.child as second
        from parents as a, parents as b
        where a.parents = b.parents and a.child < b.child

        FIRST             SECOND
        barack            clinton
        abraham           delano
        abraham           grover
        delano            grover

```
Numerical Expressions


## AGGREGATION
 - an aggregate function in the [columns] clause computes a value from a group of rows
```
create table animals as
    select "dog" as kind, 4 as legs, 20 as weight union
    select "cat"        , 4        , 10           union
    select "ferret"     , 4        , 10           union
    select "parrot"     , 2        , 6            union
    select "penguin"    , 2        , 10           union
    select "t-rex"      , 2        , 12000;

> select max(legs) from animals; 
4
> select max(legs-weight) + 5 from animals;
1
> select count(*) from animals;
6
> select count(distinct legs) from animals;
2   # there's 2 legs and 4 legs, 2 kinds

 - Aggregate functions also select a row in the table, which may be meaningful

> select max(weight), kind from animals;
12000|t-rex
> select min(kind), kind from animals;
cat|cat
> select avg(weight), kind from animals;
2009.333333|t-rex   # an arbitrary row, not meaningful
```

## GROUPING

```
select [columns] from [table] group by [expression] having [expression];
    - the number of groups is the number of unique values in group by expression
    - having clause filters set of groups that are aggregated

> select legs, max(weight) from animals group by legs;
4|20
2|12000

> select max(kind), weight/legs from animals group by weight/legs;
ferret|2
parrot|3
penguin|5
t-rex|6000
```

## CREATE TABLE OVERVIEW
- using column constraints instead of AS SELECT statements
> CREATE TABLE numbers (n, note);
> CREATE TABLE numbers (n UNIQUE, note);   # will raise an error if same n is in table twice
> CREATE TABLE numbers (n, note DEFAULT "No comment");   # default value


## DROP TABLE
- if exists is optional, but will prevent an error if table doesn't exist
> DROP TABLE IF EXISTS [name];

## MODIFYING TABLES
- insert a value into one column. Default values will be used for other columns in row.
> INSERT INTO table(column) VALUES (value);
- insert into all columns:
> INSERT INTO table VALUES (value0, value1, ...);

## UPDATE [table] SET [column=value] WHERE [expression]
```
Example:

> create table primes(n, prime);
> drop table if exists primes;
> select * from primes
Error
> create table primes(n UNIQUE, prime DEFAULT 1);
> select * from primes;
> INSERT INTO primes VALUES (2, 1), (3, 1);
> select * from primes;
2|1
3|1
> INSERT INTO primes(n) SELECT n+2 FROM primes;
> select * from primes;
2|1
3|1
4|1
5|1
> UPDATE primes SET prime = 0 WHERE n > 2 AND n%2==0;
> select * from primes;
2|1
3|1
4|0
5|1
```

## PYTHON AND SQL
```
import sqlite3

# Won't work because we need external database file n.db
def doDatabaseThing():
    db = sqlite3.Connection("n.db")
    db.execute("INSERT INTO nums VALUES (?), (?), (?);", range(4, 7))
    table = db.execute("SELECT * FROM nums;").fetchall() # returns a list of tuples, each tuple is a row
    db.commit()  # commits changes to file

```
## SQL INJECTION ATTACK
```

def injectionAttack(db):
    name = "Robert'); DROP TABLE Students; --"
    cmd = "INSERT INTO Students VALUES ('" + name + "');"
    db.executescript(cmd)
# -- signifies a comment in SQL
# > INSERT INTO Students VALUES ('Robert'); DROP TABLE Students; --')

```
The problem is string concatenation was used to create sql statement
Instead, use ? template
```
    # db.execute("INSERT INTO Students VALUES (?)", [name])
```

## TAIL CALLS

Functional Programming
- All functions are pure functions
- No re-addignment and no mutable data types
- Name-value bindings are permanent

Python Recursion vs. Iteration:
- recursive calls always create new active frames
    - Thus a recursive factorial function requires linear space O(n), but an iterative factorial uses constant space O(1)
    - Tail recursion can solve this space problem

A Tail Call is a call expression in a tail context:
- the last body sub-expression in a lambda expression
- sub-expressions 2 & 3 in a tail context 'if' expression
- all non-predicate sub-expressions in a tail context cond
- the last sub-expression in a tail context 'and' or 'or'
- the last sub-expression in a tail context 'begin' 

A Tail Call frame doesn't remain active, and doesn't increase the environment size. 

```
This is not tail recursive, since more computation (adding 1) has to be done after 
the recurse call (the recursive length call is not in a tail context):
(define (length s)
    (if (null? s) 0
        (+ 1 (length (cdr s)))))

This is tail recursive:
(define (length-tail s)
    (define (length-iter s n)
        (if (null? s) n
            (length-iter (cdr s) (+ 1 n))))
    (length-iter s 0))

REDUCE: combines elements of list using procedure
    - The recursive call to reduce is a tail call, but the call to procedure is not,
so the size depends on the size that procedure takes up.
(define (reduce procedure s start)
    (if (null? s) start
        (reduce procedure
            (cdr s)
            (procedure start (car s)))))

MAP: applies procedure to every element and construct list with results
    - this one below is not tail recursive, since the map call is not in a tail context
(define (map procedure s)
    (if (null? s)
        nil
        (cons (procdure (car s))
            (map procedure (cdr s)))))

```


SCHEME MACROS
    - allows user-defined special forms
    - a macro is an operation performed on source code before evaluation

- The body gets evaluated before the argument expression
(define-macro (twice expr)
    (list 'begin expr expr))

Evaluation Procedure:
- Evaluate the operator sub-expression, which evaluates to a macro
- Call the macro procedure on the operand expressions without evaluating them first
- Evaluate the expression returned from the macro procedure

```
Example:
(define (check val) (if val 'passed 'failed))

- The macro can tell you the expression that failed:
(define-macro (check expr) 
    (list 'if expr ''passed 
        (list 'quote (list 'failed: expr))))

FOR MACRO

(define (map fn vals)
    (if (null? vals)
        ()
        (cons (fn (car vals))
            (map fn (cdr vals)))))

(define-macro (for sym vals expr)
    (list 'map (list 'lambda (list sym) expr) vals))

```


## DESIGNING FUNCTIONS
1. From Problem Analysis to Data Definitions
 - Identify the information that must be represented and how it is represented
in the chosen programming language. Formulate data definitions and illustrate them 
with examples.
2. Signature, Purpose Statement, Header 
 - State what kind of data the desired function consumes and produces. Formulate a concise answer
to the question what the function computes. Define a stub that lives up to the signature. 
3. Functional Examples
 - Work through examples that illustrate the function's purpose. 
4. Function Template
 - Translate the data definitions into an outline of the function.
5. Function Definition
 - Fill in the gaps in the function template. Exploit the purpose statement and the examples. 
6. Testing
 - Use the examples as tests and ensure that the function passes all. Tests also supplement
 examples in that they help others read and understand the definition when the need arises. 

Examples are important!
"""