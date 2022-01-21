from LinkedList import LinkedList

my_list = LinkedList()

my_list.insert_beginning("Node 1")
my_list.insert_beginning("Node 2")
my_list.insert_beginning("Node 3")
my_list.insert_beginning("Node 4")

# Find Node iteratively:
# found_node = my_list.find_node_iteratively("Node 3")
# Print node value to the console:
# print(found_node.value)


# Add code here:
found_node = my_list.find_node_recursively("Node 2", my_list.head_node)
print(found_node)