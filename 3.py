# prime factors of 13195 are 5,7,13,29

# what is the largest prime factpr of 600851475143?

def is_it_prime(N):
        for i in range(2, N):
                if (N % i) ==0: 
                        print(N, "is not a prime number")
                        print(i, "times",num//i,"is",N)
                        break   
        else:   
                print(N, "is a prime number")


is_it_prime(29)
