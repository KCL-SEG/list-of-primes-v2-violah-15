"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if(number_of_primes <= 0):
        raise ValueError
    current_value = 2
    while len(list) < number_of_primes:
        for i in range(2, current_value+1):
            if(current_value == i):
                list.append(i)
                current_value +=1
            elif(current_value%i ==0):
                current_value +=1
                break
    return list
