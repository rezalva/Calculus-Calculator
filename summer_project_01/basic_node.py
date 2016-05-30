"""
Basic node
"""


class Node(object):
    __slots__ = ["data","next"]

    def __init__(self, data, next):
        self.data = data
        self.next = next

