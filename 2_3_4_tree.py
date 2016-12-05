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

fo = open("/home/pchenthill/practice/bst.txt", "w")
fo.write("@startuml\n")
fo.write("digraph 2_3_4_tree {\n")
fo.write("node [shape = record,height=.1];")

node_count = 0

def make_graph (node, parent_label):
    if node == None:
        return
    global node_count

    cur_node_name = "node" + str(node_count)
    fo.write(cur_node_name + "[label = \"")
    string = "<f0> "
    i = 1
    for key in node.keys:
        string += "|" +  str(key) +  "|" + "<f" + str (i) + ">"
        i = i + 1
    string += "];"

    if node.parent != None:
        conn = "\"" + parent_label + "->" + cur_node_name

    node_count += 1
    for i, child in enumerate(node.children)
        make_graph (child, "\"" + cur_node_name +  "\":f" + str(i))

make_graph (root)
fo.write("}\n")

fo.close()
