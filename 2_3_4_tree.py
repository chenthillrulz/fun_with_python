#!/bin/python

def last_key(node):
    return node.keys[-1]

class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.keys = [data]
        self.max_keys = 2
        self.max_children = 3
        self.children = []

    def add_key(self, key):
        self.keys.append(key)
        self.keys.sort()

        if len(self.keys) > self.max_keys:
            Node.split_node(self)


    def add_children(self, node):
        if len(self.children) > self.max_children:
            print ("Cannot to add more children")
            return

        self.children.append(node)
        self.children.sort(key = last_key)

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        else:
            return False

    def split_node (node):
        if len(node.keys) <= node.max_keys:
            print("unable to split the node, node len is " + str(len(node.keys)))
            return False

        parent_key = node.keys[1]

        #Move the center key to parent
        parent = node.parent
        key_added_to_parent = False
        if node.parent == None:
            # reset root node after a recursive split 
            global root
            parent = Node(parent_key, None)
            root = parent
            key_added_to_parent = True
            parent.add_children (node)

        # split current node into left(removing the middle/right key from cur node) and right node
        right_node = Node(node.keys[2], parent)
        node.parent = parent # to counter the case of root node split
        del node.keys[1:]
        # add right_node to parent's children
        parent.add_children (right_node)

        if node.is_leaf() == False:
            right_node.add_children(node.children[2])
            right_node.add_children(node.children[3])
            del node.children[2:]

        if key_added_to_parent == False:
            parent.add_key(parent_key)

        return True


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

    return find_leaf(child, key)

def insert(root, key):
    leaf = find_leaf (root, key)
    leaf.add_key(key)
    return leaf


root = Node(3, None)
insert(root, 4)
insert(root, 5)
insert(root, 6)
insert(root, 7)
insert(root, 8)
insert(root, 9)
insert(root, 10)

fo = open("/home/pchenthill/sources/fun_with_python/2_3_4_tree.dot", "w")
fo.write("digraph g {\n")
fo.write("node [shape = record,height=.1];\n")

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
    string += "\"];\n"
    fo.write(string)

    if node.parent != None:
        conn = parent_label + " -> \"" + cur_node_name + "\"\n"
        fo.write(conn)

    node_count += 1
    for i,child in enumerate(node.children):
        make_graph (child, "\"" + cur_node_name +  "\":f" + str(i))

make_graph (root, "")
fo.write("}\n")

fo.close()
