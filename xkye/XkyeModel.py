"""
XkyeModel.py: To perfrom Xkye language operations
"""

import sys
import os


from antlr4 import *
from .libs import *


class io:


    def __init__(self, filename):

        self.filename = filename
        self.outDict = {}


    def read(self):

        if not os.path.isfile(self.filename):
            raise Exception("File \""+self.filename+"\" is missing, kindly check the path or provide the absolute path")


        #Else perfrom xky file reading task
        input = FileStream(self.filename)
        lexer = XkyeLexer(input)
        stream = CommonTokenStream(lexer)
        parser = XkyeParser(stream)
        tree = parser.globe()
        listendX = XkyeExtendedListener(self.outDict)

        walker = ParseTreeWalker()
        walker.walk(listendX, tree)
        
        return True

#    def get(self, value):

