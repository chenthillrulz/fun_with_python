#!/bin/python

from enum import Enum

class Color(Enum):
    red = 1
    black = 2

values = list(map (int, input().split()))

class Node:
    def __init__(self, data, parent):
        self.right = None
        self.left = None
        self.data = data
        self.parent = parent
        self.color = Color.black


def insertNode ()
