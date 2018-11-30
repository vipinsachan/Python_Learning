# s1=input("Enter the numbers in the list separated by comma..like 1,2,3,4,5: ")
n=input("How many numbers do u want in the list: ")
l1 = []

def max_num(l1):
    max = 0
    smax = 0

    for i in l1:
        if int(i) > int(max) and int(i) > int(smax):
            smax = max
            max = i
        elif int(i) > int(smax):
            smax = i
        else:
            continue
    print("Max is: {} and smax is: {}".format(max, smax))


if not n:
    print("The list is empty")
else:
    cnt = 0
    while cnt < int(n):
        x=input("Enter number: ")
        if x.isdigit():
            l1.append(x)
        cnt += 1

length=len(l1)
print(l1)

if length == 1:
    print(l1[0])
else:
    max_num(l1)
