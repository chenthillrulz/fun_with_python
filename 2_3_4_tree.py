#!/bin/python


class Node (self):
    def __init__(data, parent):
        self.parent = parent
        self.keys = [data]
        self.max_keys = 3
        self.max_children = 4
        self.children = []

    def get_keys_len(self):
        return len(self.keys)

    def add_key(self, key):
        if get_keys_len() >= 3:
            return False

        self.keys.append(key)
        self.keys.sort()
        return True

    def add_children(self, node):
        if  len(self.children) >= 4:
            return False

        self.children.append(node)
        self.chilren.sort(node.keys[-1])

        return True

    def split_node (node):
        if get_keys_len(self) != 3:
            return False

        parent_key = node.keys[1]

        parent = node.parent
        if node.parent == None:
            parent = Node(parent_key, None)
        else:
            parent.add_key(parent_key)

        left_node = Node(node.keys(0), parent)
        right_node = Node(node.keys(2), parent)


        return True
