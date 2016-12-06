#!/bin/python


class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.keys = [data]
        self.max_keys = 2
        self.max_children = 3
        self.children = []

    def get_keys_len(self):
        return len(self.keys)

    def add_key(self, key):
        self.keys.append(key)
        self.keys.sort()


    def add_children(self, node):
        if  len(self.children) >= self.max_children:
            return False

        self.children.append(node)
        self.chilren.sort(node.keys[-1])

        return True

    def split_node (node):
        if get_keys_len(node) != 3:
            print("unable to split the node, node len is " + str(get_keys_len(node)))
            return False

        parent_key = node.keys[1]
        
        #Move the center key to parent
        parent = node.parent
        if node.parent == None:
            # reset root node after a recursive split 
            global root
            parent = Node(parent_key, None)
            root = parent
        else:
            parent.add_key(parent_key)

        # split current node into left(removing the middle/right key from cur node) and right node
        right_node = Node(node.keys(2), parent)
        del node.keys[1]
        del node.keys[2]
        # add right_node to parent's children
        parent.add_children (right_node)

        # if parents key becomes larger recursively split
        if len(parent.keys) > max_keys:
            Node.split_node(parent)

        return True

    def is_leaf(self):
        if len(self.keys) == 0:
            return True
        else:
            return False

def find_leaf(node, key):
    if node == None:
        return None

    if node.is_leaf():
        return node
    node_index = 0
    for i, k in enumerate(node.keys):
        if key > k:
            node_index += 1
        else:
            break
    child = node.children[node_index]

    return find_leaf(child)

def insert(root, key):
    leaf = find_leaf (root, key)
    leaf.add_key(key)
    return leaf


root = Node(2, None)
fo = open("/home/pchenthill/sources/fun_with_python/2_3_4_tree.txt", "w")
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
    fo.write(string)

    if node.parent != None:
        conn = "\"" + parent_label + "->" + cur_node_name
        fo.write(conn)

    node_count += 1
    for i,child in enumerate(node.children):
        make_graph (child, "\"" + cur_node_name +  "\":f" + str(i))

make_graph (root, "")
fo.write("}\n")

fo.close()
