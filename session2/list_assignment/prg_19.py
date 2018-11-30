a1 = [11,8,11,9]
a2 = [11,9,8,12]
l = []
l1 = []
for i in range(len(a1)):
    if a2[i] > a1[i]:
        l.append(i+1)
    elif a2[i] < a1[i] or a2[i] == a1[i]:
        l1.append(i+1)

# print(l)
print("a2 is better in competition: {}".format(l))
print("a2 is never better in competition: {}".format(l1))
# print("a2 is better in competition: {}".format(i+1))
