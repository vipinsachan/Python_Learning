# prints all Italian restaurants in the restaurants list that have no ratings of value 1 and at least one rating of value 5

restaurants = [['Acme', 'Italian', 2, 4, 3, 5], ['Flintstone', 'Italian', 1, 5, 2, 4, 3, 3, 4],['Bella', 'Italian', 4, 5]]

for value in range(len(restaurants)):
    if restaurants[value][1] == 'Italian' and 1 not in restaurants[value][2:] and 5 in restaurants[value][2:]:
        print(restaurants[value][0])
