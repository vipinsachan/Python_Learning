
def rec_fun(n):
    if n <= 1:
        return n
    else:
        return rec_fun(n-1) + rec_fun(n-2)


nterms = int(input("Enter the number till what you want to get Fibonacci series: "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(rec_fun(i))
