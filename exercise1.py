# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

l_1 = [1,11,14,5,8,9]

def lessThan10(l):
    return [x for x in l if x < 10]

print (lessThan10(l_1))