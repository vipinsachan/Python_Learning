s1=input("Enter first month and year..for eg to enter august 2018, type 8,2018: ")
s2=input("Enter second month and year..for eg to enter september 2018, type 9,2018: ")

l1=list(s1)
l2=list(s2)

def compare_date(l1, l2):
    m1=l1[0]
    y1=l1[1]

    m2=l2[0]
    y2=l2[1]

    if y1 > y2:
        return 1
    elif y1 < y2:
        return -1
    else:
        if m1 > m2:
            return 1
        elif m1 < m2:
            return -1
        else:
            return 0

print(compare_date(l1,l2))