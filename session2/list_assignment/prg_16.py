wordy = [['impala','malibu','camry','jetta'],['zebra','impala','lion','impala','malibu','zebra'],['tiger','lion','cowboy','jet','49er'],[ ],['five','seven','nine']]

print(wordy[2][1])
print(wordy[1][2][3])
print(len(wordy))
print(len(wordy[1]))

for i in wordy:
    if len(i) == 0:
        break
    else:
        print(i[-1])