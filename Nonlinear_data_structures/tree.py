# Define your "TreeNode" Python class below
class TreeNode:
    def __init__(self, value):
        print("initializing node…")
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        new_children = []
        new_children = [item for item in self.children if item != child_node]
        self.children = new_children

    def traverse(self):
        print(self.value)
        # for item in self.children:
        #     print(item.value)
        nodes_to_visit = [self]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit.extend(current_node.children)



root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()