#!/bin/python3

#l = [int(x) for x in input().split()]
elements = list(map(int, input().split()))


class Node:
  def __init__(self, data):
    self.right = None
    self.left = None
    self.data= data


  def insert_node (node, data):
    if node == None:
      return True
    
    parent = None	
    if data > node.data:
      ret = Node.insert_node(node.right, data)
      if ret == True:
        new_node = Node(data)
        node.right = new_node
        return False

    if data <= node.data:
      ret = Node.insert_node(node.left, data)
      if ret == True:
        new_node = Node(data)
        node.left = new_node
        return False
    return False
 

root = None
for i, value in enumerate(elements):
  if i == 0:
    root = Node(value)
  else:
    Node.insert_node(root, value)

def find_inorder_predecessor(node):
  if (node == None):
    return None, None
  find_inorder_predecessor(node.left)
  n, p = find_inorder_predecessor(node.right)
  if (n == None):
    n = node
  if (node != None and n == node.right):
    p = node	  
  return n, p

node, parent = find_inorder_predecessor(root.left)
print(node.data)	
print(parent.data)	

fo = open("/home/pchenthill/practice/bst.txt", "w")
fo.write("@startuml\n")
fo.write("digraph binary_search_tree {\n")

def make_graph (node):
  if node == None:
    return
  
  if node.left != None: fo.write("	" + str(node.data) + " -> " + str(node.left.data) + " [label=L]\n" )   
  if node.right != None:  fo.write("	" + str(node.data) + " -> " + str(node.right.data) + " [label=R]\n" ) 
  make_graph (node.left)
  make_graph (node.right)

make_graph (root)

fo.write("}\n")
fo.close()
