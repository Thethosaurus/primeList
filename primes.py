# def countPrimes(n):
#     # for i in range(2, n+1):
#     #     for j in range(2, n // 2):
#     #         if i % j == 0:
#     #             break
#     #         else:
#     #             print i
#     for i in range(2, n-1):
#         primeVerify = n/i
#         if type(primeVerify)==int:
#             if primeVerify>1:
#                 print i
#                 print "hello"
# countPrimes(100);



number = raw_input("List Upper Bound?")
def isPrime(n):
    for i in range(n, n-1):
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
            # isPrime(i);
        # print "hello"

primeList(int(number));
