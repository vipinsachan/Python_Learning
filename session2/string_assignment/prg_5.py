s=input("Enter string: ")

vowel_cnt = 0
consonant_cnt = 0
for val in s:
    if val in "aeiouAEIOU":
        vowel_cnt += 1
    elif val.isalpha() == True:
        consonant_cnt += 1

print("Total Vowels in the string: {} and total consonants in th string: {}".format(vowel_cnt,consonant_cnt))