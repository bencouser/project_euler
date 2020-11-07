# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13

#What is the 10 001st prime number?

def all_factors(N):
        factors = []
        for i in range(1, int(np.sqrt(N) + 1)): #we only need to check up to the root of ur number
                if N % i == 0:
                        factors.append(i)
        factors.append(N)
        return factors

def is_it_prime(n):
        return len(all_factors(n)) == 2
