#v = [ 10, 12, 3, -5, 5, 6 ]
v = [ 1, 10, 0, 3, -6, 5, 0 ]

#cnt = 0
sum = 0
#while cnt < len(v):

for val in v:
    if val < 0 or val == 0:
        break
    else:
        sum = sum + val
#cnt += 1
print(sum)