class Node:
    def __init__(self, dataval=None):
        self.data_val = dataval
        self.next_val = None

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.next_val == other.next_val and self.data_val == other.data_val


class LinkedList:
    def __init__(self, headval=None):
        self.head_node = Node(headval)
        self.last_node = self.head_node
        self.next_out = self.head_node

    def __next__(self):
        out = self.next_out
        self.next_out = self.next_out.next_val
        return out.data_val

    def __iter__(self):
        node = self.head_node
        while node is not None:
            yield node.data_val
            node = node.next_val

    def add_node_to_end(self, val):
        node = self.head_node
        if node.data_val is None:
            node = Node(val)
            self.head_node = node
            self.last_node = node
            return
        while node.next_val is not None:
            node = node.next_val
        node.next_val = Node(val)
        self.last_node = node.next_val

    def remove_node_with_val(self, val):
        if self.head_node.data_val == val:
            self.head_node = self.head_node.next_val
        node = self.head_node
        while node.next_val is not None:
            if node.next_val.data_val == val:
                if node.next_val.next_val is None:
                    self.last_node = node
                node.next_val = node.next_val.next_val
                break
            node = node.next_val

    def search_for_val(self, val, multi_val=False):
        node_to_get = self.head_node
        while node_to_get.next_val is not None:
            if node_to_get.data_val == val:
                return True
            node_to_get = node_to_get.next_val
        if self.last_node.data_val == val:
            return True
        return False

    def insert_val_after_val(self, new_val, val_to_search):
        node_to_insert = Node(new_val)
        if self.last_node.data_val == val_to_search:
            node_to_insert.next_val = None
            self.last_node.next_val = node_to_insert
            self.last_node = node_to_insert
            return
        node = self.head_node
        while node.next_val is not None:
            if node.data_val == val_to_search:
                node_to_insert.next_val = node.next_val
                node.next_val = node_to_insert
            node = node.next_val

    def return_and_remove_head(self):
        if self.head_node:
            temp = self.head_node
            self.head_node = self.head_node.next_val
            return temp.data_val

    def print_list(self):
        for i in self.__iter__():
            print(i)

    def return_and_remove_tail(self):
        node = self.head_node
        if node == self.last_node:
            ret_val = self.head_node.data_val
            temp = Node()
            self.head_node = temp
            return ret_val
        else:

            while True:
                if node.next_val == self.last_node:
                    ret_val = node.next_val.data_val
                    node.next_val = None
                    self.last_node = node
                    return ret_val
                else:
                    node = node.next_val


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add_node_to_end("second")
    l_list.add_node_to_end("third")
    l_list.add_node_to_end("fourth")
    print(l_list.return_and_remove_tail())
    print("***")
    l_list.print_list()
