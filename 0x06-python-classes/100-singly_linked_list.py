#!/usr/bin/python3 

class Node:
    """
    A class used to represent node of a linkedList

    Attributes
    ----------
    data : int
        data stored in the Node
    next_node : int
        reference to the next node in a list

    methods
    -------
    data()
       getter method that return value of data attribute
    data(value)
       setter method that reset value of data attribute
    next_node()
      getter method that return value of next_node attribute
    next_node(value)
       setter method that reset value of data attribute
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value)!= int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.size = 0

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            self.size += 1
        else:
            actual = self.__head
            prev = actual
            idx = 0
            while actual is not None:
                if idx == 0:
                    if new_node.data < actual.data:
                        self.__head = new_node
                        new_node.next_node = actual
                        self.size += 1
                        actual = None
                        break
                else:
                    if new_node.data < actual.data:
                        prev.next_node = new_node
                        new_node.next_node = actual
                        self.size += 1
                        actual = None
                        break
                idx += 1
                prev = actual
                actual = actual.next_node

            if actual is None and new_node.next_node is None:
                prev.next_node = new_node
                self.size += 1

    def __str__(self):
        current = self.__head
        to_print = ""
        while current is not None:
            to_print += str(current.data)
            if current.next_node:
                to_print += "\n"
            current = current.next_node
        return to_print
