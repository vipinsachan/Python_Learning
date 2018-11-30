# Find the highest occurrence of the character in a string and display it

string=input("Enter the string: ")
l=list(string)

result = []

for i in l:
    if i not in result:
        result.append(i)
for val in result:
    count=l.count(val)
    cnt1=count
    print(val, count)
print(result)
print(l)