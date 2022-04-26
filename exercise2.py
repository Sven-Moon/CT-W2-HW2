# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def mergeAndSort(l1, l2):
    return sorted(l1 + l2)

print(mergeAndSort(l_1, l_2))