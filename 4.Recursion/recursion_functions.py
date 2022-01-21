# Define sum_to_one() below...
def sum_to_one(n):
    if n==1:
        return n
    print("Recursing with input: {0}".format(n))
    return n+sum_to_one(n-1)
# uncomment when you're ready to test

# Define factorial() below:
def factorial(n):
    if n < 2:
        return 1

    return n*factorial(n-1)


#power set with recursion
def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first

universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
    print(set)
