item=int(input("How many items do you want to put in a list: "))
mylist=list()
even_num=list()
odd_num=list()

for i in range(item):
    odd_even = input()
    mylist.append(odd_even)

print(mylist)

for i in mylist:
    if int(i) % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)

print("Number of even numbers :", len(even_num))
print("Number of odd numbers :", len(odd_num))