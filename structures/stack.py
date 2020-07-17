from structures.linked_list import LinkedList


class Stack:
    def __init__(self, val=None):
        self.data_list = LinkedList(val)
        self.size = 0
        if val:
            self.size = 1

    def push(self, val):
        if val:
            self.size += 1
            self.data_list.add_node_to_end(val)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.data_list.return_and_remove_head()
        else:
            return None

    def end_stack_pop(self):
        self.size -= 1
        # if self.size > 0:
        return self.data_list.return_and_remove_tail()
        # else:
        #     return None

    def print_stack(self):
        self.data_list.print_list()

    def to_array(self):
        return self.data_list.to_array()

    def __sizeof__(self):
        return self.size
