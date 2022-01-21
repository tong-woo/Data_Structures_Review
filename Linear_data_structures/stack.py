from node import Node

# Add your Stack class below:
class Stack:
    def __init__(self, limit = 1000, size = 0):
        self.top_item = None
        self.limit = limit
        self.size = size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def has_space(self):
        if self.limit > self.size:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("The stack is empty")

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The stack is empty")

