#Recursion: base case + recursive step(This portion of the function is the
# step that moves us closer to the base case.)

#Iteration: When using iteration, we rely on a counting variable and a boolean condition.
# For example, when iterating through the values in a list, we would increment the counting
# variable until it exceeded the length of the dataset.

# define your sum_to_one() function above the function call
#simulating python built-in call stack
def sum_to_one(n):
    result = 1
    call_stack = []
    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")
    while call_stack != []:
        return_value = call_stack.pop()
        print(call_stack)
        print("we are adding {} result and their respective values.".format(return_value["n_value"]))
        result += return_value["n_value"]
    return result, call_stack






sum_to_one(4)