# what is the first fibonacci number to have 1000 digits

def nextTerm(a, b):
    return a + b

fibonacciNumbers = [1, 1]

def listFibonacciNumbers(fibonacciNumbers, N):
    for i in range(N):
        newTerm = nextTerm(fibonacciNumbers[i], fibonacciNumbers[i + 1])
        if len(str(abs(newTerm))) == 1000:
            print(i+3)
            break
        fibonacciNumbers.append(newTerm)

listFibonacciNumbers(fibonacciNumbers, 100000)
