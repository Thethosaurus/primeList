number = int(raw_input("List Upper Bound?"))
def isPrime(n):
    for i in range(2, n-1):
        if n % i == 0:
            print "false"
            break
    else:
        print "true"

def primeList(n):
    primeArray = []
    for i in range(2, n):
        for j in primeArray:
            if i % j == 0:
                break
        else:
            print i
            primeArray.append(i)

primeList (number);
