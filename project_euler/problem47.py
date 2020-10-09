'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have
four distinct prime factors each. What is the first of these numbers?
'''
# Slow brute-force. Go back and optimize later. :(


def trial_division(n: int):
    """Return a list of the prime factors for a natural number."""
    a = set()            # Prepare an empty list.
    f = 2                # The first possible factor.
    while n > 1:         # While n still has remaining factors...
        if n % f == 0:   # The remainder of n divided by f might be zero.
            a.add(f)     # If so, it divides n. Add f to the list.
            n /= f       # Divide that factor out of n.
        else:            # But if f is not a factor of n,
            f += 1       # Add one to f and try again.
    return a             # Prime factors may be repeated: 12 factors to 2,2,3.


def findDistinctPrimeFactors():
    n = 30
    while True:
        n_factors = trial_division(n)
        if len(n_factors) == 4:
            if (len(trial_division(n + 1)) + len(trial_division(n + 2))
                    + len(trial_division(n + 3))) == 12:
                return n
            else:
                n += 1
        else:
            n += 1


print(findDistinctPrimeFactors())
