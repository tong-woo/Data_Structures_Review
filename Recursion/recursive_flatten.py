"""
Remember our tools for recursive functions.
We want to identify a base case, and we need
to think about a recursive step that takes us
closer to achieving the base case
"""

def flatten(my_list):
    result = []
    for i in range(len(my_list)):
        if isinstance(my_list[i], list):
            print("List found!")
            flat_list = flatten(my_list[i])
            result.extend(flat_list)
        else:
            result.append(my_list[i])
    return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))

