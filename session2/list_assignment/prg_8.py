
v = [ 17, -5, 15, -3, 12, -5, 0, 12, 22, -1, 22 ]
#v = [ -17, -5, -15, -3, -12, -5, 0, -12, -22, -1, -22 ]
pos_list = []

for val in v:
    if val > 0:
        pos_list.append(val)
pos_list.sort()

length=len(pos_list)

if length == 0:
    print("None")
else:
    print(pos_list)