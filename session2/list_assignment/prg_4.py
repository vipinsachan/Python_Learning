string=input("Enter the string: ")
print(string)

for val in string:
    if val not in 'PBKRQ':
        print("Invalid String")
        quit()


def chess_score(s):

    val1 = s.count('P')
    val2 = s.count('B')
    val3 = s.count('K')
    val4 = s.count('R')
    val5 = s.count('Q')

    print("The sum is: {}".format(val1 + val2*3 + val3*3 + val4*5 + val5*9))

chess_score(string)
