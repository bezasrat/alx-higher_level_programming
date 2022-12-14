#!/usr/bin/python3
"""
File: 4-square.py
Description: a script that can instantiate an object
Author: Bezahun Asrat Bekele
Date: Oct 12, 2022
"""


class Square():
    """
    this class contains methods and constractors that can instantiate
    object
    """
    def __init__(self, size=0):
        self.__size = size
        
    @property
    def size(self):
        """
        getter method
        """
        return(self.__size)
    
    @size.setter
    def size(self, value):
        """
        setter method
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        
    def area(self):
        """
        returns the squared size
        """
        return(self.__size ** 2)
