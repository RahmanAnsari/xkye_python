"""
XkyeModel.py: To perfrom Xkye language operations
"""

import sys
import os


from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from multipledispatch import dispatch


from .libs import XkyeLexer, XkyeParser, XkyeExtendedListener


class io:

    # To initiate the read write operation
    def __init__(self, filename):

        self.filename = filename
        self.outDict = {}

    # To convert the input file into the outdictionary
    def read(self):

        if not os.path.isfile(self.filename):
            raise Exception(
                'File "'
                + self.filename
                + '" is missing, kindly check the path or provide the absolute path'
            )

        # Else perfrom xky file reading task
        inputFile = FileStream(self.filename)
        lexer = XkyeLexer(inputFile)
        stream = CommonTokenStream(lexer)
        parser = XkyeParser(stream)
        tree = parser.globe()
        listendX = XkyeExtendedListener(self.outDict)

        walker = ParseTreeWalker()
        walker.walk(listendX, tree)

        return True

    # To read the values
    @dispatch(str)
    def get(self, entity):

        dictList = list(self.outDict["global"].keys())

        if entity not in dictList:
            raise Exception(
                'Requested entity "'
                + entity
                + '" not declared above. kindly check your input .xky file'
            )

        result = self.outDict["global"][entity]
        return result

    @dispatch(str, str)
    def get(self, entity, substr):
        dictList = list(self.outDict.keys())

        if substr not in dictList:
            raise Exception(
                'Requested clutch "'
                + substr
                + '" is not declared above. kindly check your input .xky file'
            )

        if entity not in list(self.outDict[substr].keys()):
            raise Exception(
                'Requested entity "'
                + entity
                + '" not declared above. kindly check your input .xky file'
            )

        result = self.outDict[substr][entity]
        return result

    @dispatch(str, str, int)
    def get(self, entity, substr, subnumber):
        subnumber = str(subnumber)
        substrnew = substr + subnumber

        dictList = list(self.outDict.keys())

        if substrnew not in dictList:
            if substr in dictList:
                if entity in list(self.outDict[substr].keys()):
                    result = self.outDict[substr][entity]
                    return result

                raise Exception(
                        'Requested entity "'
                        + entity
                        + '" not declared above. kindly check your input .xky file'
                    )

            else:
                raise Exception(
                    'Requested clutch "'
                    + substr
                    + '" is not declared above. kindly check your input .xky file'
                )

        else:
            if entity not in list(self.outDict[substrnew].keys()):
                if entity in list(self.outDict[substr].keys()):
                    result = self.outDict[substr][entity]
                    return result

                
                raise Exception(
                        'Requested entity "'
                        + entity
                        + '" not declared above. kindly check your input .xky file'
                    )

            else:
                result = self.outDict[substrnew][entity]
                return result
