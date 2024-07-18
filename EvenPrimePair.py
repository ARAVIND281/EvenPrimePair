import time
import random

def miller_rabin_test(n, k=5):
    if n in (2, 3):
        return True
    if n <= 1 or n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True
    return miller_rabin_test(n)

def find_prime_pair(even_number):
    if even_number <= 2 or even_number % 2 != 0:
        return None
    limit = 10**6
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit, i):
                sieve[j] = False
    small_primes = [x for x in range(limit) if sieve[x]]
    for prime in small_primes:
        if prime >= even_number:
            break
        if is_prime(even_number - prime):
            return (prime, even_number - prime)
    for i in range(small_primes[-1], even_number // 2 + 1, 2):
        if is_prime(i) and is_prime(even_number - i):
            return (i, even_number - i)
    return None

def benchmark(even_number):
    start_time = time.time()
    prime_pair = find_prime_pair(even_number)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, prime_pair

def main():
    try:
        even_number_str = input("Enter an even number greater than 2: ")
        even_number = int(even_number_str)
        if even_number <= 2 or even_number % 2 != 0:
            print("Please enter an even number greater than 2.")
            return
        
        elapsed_time, prime_pair = benchmark(even_number)
        print(f"Time taken: {elapsed_time} seconds")
        
        if prime_pair:
            print(f"The two prime numbers that sum up to {even_number} are: {prime_pair[0]} and {prime_pair[1]}")
        else:
            print(f"No prime pair found for the number {even_number}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
