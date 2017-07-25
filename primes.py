number = int(raw_input("List Upper Bound?"))

def isPrime(n):
    test = True
    for i in range(2, n-1):
        if n % i == 0:
            test = False
            return test
    return test

def distinctPrimes(n):
    primeList = []
    for i in range (1, n):
        primeTestNumberOne = 2*i +1
        primeTestNumberTwo = 2*i +3
        if isPrime(primeTestNumberOne) == True:
            primeList.append(primeTestNumberOne)
        elif isPrime(primeTestNumberTwo) == True:
            primeList.append(primeTestNumberTwo)
    return primeList


def primeList(n):
    primeArray = []
    for i in range(2, n):
        for j in primeArray:
            if i % j == 0:
                break
        else:
            primeArray.append(i)

primeList (number);
