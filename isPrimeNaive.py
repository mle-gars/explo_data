#!/usr/bin/env python3

def isPrime(num):
    """Check if a number is prime and return True or False."""
    # Handle numbers less than or equal to 1
    if type(num) is not int:
        return False
    elif num <= 1:
        return False
    # Check for factors from 2 to the square root of num
    else:
        for i in range(2, int(num**0.5) + 1):
            # If num is divisible by i, it's not prime
            if num % i == 0:
                return False
        else:
            return True
        
print(isPrime(11))

