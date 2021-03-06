#!/usr/bin/python3
"""In this module we defiine a class for a square object"""


def evaluate_size(value):
    """Checks if the value is a positive integer or raises an exception
    Args:
        value (int): The value must be an integer

    Returns:
        int: the checked integer
    """
    if not(type(value) is int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    else:
        return value


def evaluate_position(value):
    """Checks if the value is a tuple with 2 positive integers
    Args:
        value (tuple): The value must be a tuple with 2 positive integers

    Returns:
        tuple: the checked tuple
    """
    if type(value) is tuple and len(value) == 2:
        a = evaluate_size(value[0])
        b = evaluate_size(value[1])
        return a, b
    else:
        raise TypeError("position must be a tuple of 2 positive integers")


class Square:
    """This class defines a square"""
    global print

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an object for a square class.

        Args:
            size (int): The size of the square. Can be 0 if size is not
                        specified.
        """
        self.__size = evaluate_size(size)
        self.__position = evaluate_position(position)

    def __str__(self):
        """A printable representation of the class Square"""
        if self.size != 0:
            spaces = "\n" * self.position[1]
            lines = " " * self.position[0] + "#" * self.size
            sq = (lines + "\n") * (self.size - 1) + lines
            return spaces + sq
        return ""

    @property
    def size(self):
        """obj:`int`: returns o changes the value of the attribute`size`"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = evaluate_size(value)

    @property
    def position(self):
        """obj:`int`: returns o changes the value of the attribute`position`"""
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = evaluate_position(value)

    def area(self):
        """Returns the current square area.

        Returns:
            The area of a square
        """
        return self.__size ** 2

    def my_print(self):
        print(self.__str__)
