from typing import List

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Perform the Sieve of Eratosthenes algorithm to find all prime numbers up to a given limit.

    Parameters:
    limit (int): The upper limit to find prime numbers.

    Returns:
    List[int]: A list of prime numbers up to the given limit.
    """
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number*number, limit + 1, number):
                is_prime[multiple] = False

    return [number for number, prime in enumerate(is_prime) if prime]

