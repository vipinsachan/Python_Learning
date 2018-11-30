# calculate the sum and average of n integer numbers

item=int(input("How many numbers do you want to put in a list: "))
mylist=list()
even_num=list()
odd_num=list()

for i in range(item):
    print("num:{}".format(i), end=" ")
    odd_even = input()
    mylist.append(odd_even)

print("numbers: ", mylist)

sum=0
for i in mylist:
    sum = sum + int(i)

avg=sum/item
print("sum: ", sum)
print("Average: ", int(avg))