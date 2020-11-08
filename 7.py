# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13

#What is the 10 001st prime number?

def all_factors(N):
        factors = []
        for i in range(1, int(np.sqrt(N) + 1)):
                if N % i == 0:
                        factors.append(i)
        factors.append(N)
        return factors

def is_it_prime(n):
        return len(all_factors(n)) == 2

primes = []
number = 2

def finding_primes(n):
        while (len(primes) < 10002):
                if is_it_prime(n):      
                        primes.append(n)
                        n += 1
                else:
                        n += 1

finding_primes(number)

print(primes[10000])
