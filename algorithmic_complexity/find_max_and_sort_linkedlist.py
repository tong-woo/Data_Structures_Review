from linkedlist import LinkedList


# Fill in Function
def find_max(linked_list):
    print("--------------------------")
    print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
    # Write Code Here
    current_node = linked_list.get_head_node()
    max = current_node.get_value()
    while current_node.get_next_node():
        tmp = current_node.get_next_node().get_value()
        if max < tmp:
            max = tmp
        current_node = current_node.get_next_node()
    return max


# Fill in Function
def sort_linked_list(linked_list):
    print("\n---------------------------")
    print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
    new_linked_list = LinkedList()
    # Write Code Here!
    while linked_list.get_head_node().get_next_node() is not None:
        current_max_val = find_max(linked_list)
        new_linked_list.insert_beginning(current_max_val)
        linked_list.remove_node(current_max_val)
    new_linked_list.insert_beginning(linked_list.get_head_node().get_value())
    return new_linked_list


# Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

# Runtime
runtime = "REPLACE"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))
