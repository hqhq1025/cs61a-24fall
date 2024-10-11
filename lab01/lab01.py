def digit(n, k):
    """Return the digit that is k from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    return (n//(pow(10,k)))%10


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return int(a*b*c/(min(a,b,c)*max(a,b,c)))


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
    mul = 1
    for _ in range(k):
        mul = mul*n
        n -= 1
    return mul






def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    "*** YOUR CODE HERE ***"
    counts = 1
    if n > k:
        while True:

            if n-k <= 0:
                break
            n  -= k
            counts += 1
        for _ in range(counts):
            print(n)
            n += k
        return counts
    else:
        return 0

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
    i = 0
    sum = 0
    while True:
        if y // pow(10,i) != 0:
            i += 1
        else:
            break
    for h in range(i):
        sum += (y // pow(10,h))%10
    return sum
            

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
    wei = 0
    while True:
        if n // pow(10,wei) == 0:
            break
        else:
            wei += 1
    for i in range(wei):
        if (n // pow(10,i)) % 10 == 8:
            if (n // pow(10,i + 1)) % 10 == 8:
                return True
    return False