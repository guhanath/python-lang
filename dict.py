msg = 'hello world'
print(msg)

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for fruit,count in basket_items.items():
#if the key is in the list of fruits, add the value (number of fruits) to result
    if fruit in fruits : result+= count

print(result)