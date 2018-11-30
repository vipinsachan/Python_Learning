words = [ 'aardvark' , 'abaka', 'expedite', 'experience', 'shoetrees', 'tastetest', 'test' , 'meramerm' , 'vipin']
print(words)
l = []

for i in words:
    # print(i)
    # print(len(i),end=" ")
    if len(i) >= 8 and i[0] == i[-1]:
        l.append(i)

print(l[0],l[-1])