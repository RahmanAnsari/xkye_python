import sys
import ipaddress

#from antlr4 import *
from .XkyeParser import XkyeParser
from .XkyeListener import XkyeListener


class XkyeExtendedListener(XkyeListener):
    def __init__(self, outDict):
        self.outDict = outDict
        self.spanList = []

    # Enter a parse tree produced by XkyeParser#clutch.
    def enterGlobe(self, ctx: XkyeParser.GlobeContext):
        self.outDict["global"] = {}
        self.spanList.append(("global", "1"))

    # Enter a parse tree produced by XkyeParser#globalgroup.
    def enterGlobalgroup(self, ctx: XkyeParser.GlobalgroupContext):
        for child in ctx.children:
            child.parent_Ctx = "global"
            child.clutch_Set = 1

    # Enter a parse tree produced by XkyeParser#clutchspan.
    def enterClutchspan(self, ctx: XkyeParser.ClutchspanContext):
        entity = ctx.entity().getText()

        setList = []

        for i in self.spanList:
            setList.append(i[0])

        if entity not in setList:
            number = ctx.number().getText()
            spanPair = (entity, number)

            self.spanList.append(spanPair)
            self.outDict[entity] = {}

        else:
            raise Exception(
                'Clutch span for "'
                + entity
                + '" is already declared, kindly check your input .xky file'
            )
            # exit()

    # Enter a parse tree produced by XkyeParser#pairgroup.
    def enterPairgroup(self, ctx: XkyeParser.PairgroupContext):
        for child in ctx.children:
            child.parent_Ctx = ctx.parent_Ctx
            child.clutch_Set = ctx.clutch_Set

    # Enter a parse tree produced by XkyeParser#pair.
    def enterPair(self, ctx: XkyeParser.PairContext):
        key = ctx.key().entity().getText()
        value = ctx.value().getText()

        if ctx.clutch_Set > 1:
            ctx.parent_Ctx = ctx.parent_Ctx + str(ctx.clutch_Set)

        keyList = list(self.outDict[ctx.parent_Ctx].keys())

        first = value[0]
        last = value[-1]

        if first == "'" and last == "'":
            value = value[1:-1]

        elif value == "TRUE" or value == "FALSE":
            value = bool(value)

        elif value.isdigit():
            value = int(value)

        elif value.replace(".", "", 1).isdigit():
            value = float(value)

        elif (value.replace(".", "").isdigit()) is False:
            value = ipaddress.ip_network(value, False)

        else:
            value = ipaddress.ip_address(value)

        if key not in keyList:
            self.outDict[ctx.parent_Ctx][key] = value
        else:
            raise Exception(
                "Entity "
                + key
                + " for "
                + ctx.parent_Ctx
                + " is already declared, kindly check your input .xky file"
            )
            # exit()

    # Enter a parse tree produced by XkyeParser#pairgroupset.
    def enterPairgroupset(self, ctx: XkyeParser.PairgroupsetContext):

        if ctx.clutchdefheader() is not None:
            childCtx = ctx.clutchdefheader().entity().getText()
            clutchSet = 1

        if ctx.clutchsetheader() is not None:
            childCtx = ctx.clutchsetheader().entity().getText()
            clutchSet = int(ctx.clutchsetheader().number().getText())

        ctx.pairgroup().clutch_Set = clutchSet
        ctx.pairgroup().parent_Ctx = childCtx

    # Enter a parse tree produced by XkyeParser#clutchdefheader.
    def enterClutchdefheader(self, ctx: XkyeParser.ClutchdefheaderContext):
        entity = ctx.entity().getText()
        dictList = list(self.outDict.keys())

        if entity not in dictList:
            number = "1"
            spanPair = (entity, number)

            self.spanList.append(spanPair)
            self.outDict[entity] = {}

    # Enter a parse tree produced by XkyeParser#clutchsetheader.
    def enterClutchsetheader(self, ctx: XkyeParser.ClutchsetheaderContext):
        entity = ctx.entity().getText()
        clutchSet = int(ctx.number().getText())
        dictList = list(self.outDict.keys())
        setList = []

        entitystr = entity + str(clutchSet)

        for i in self.spanList:
            setList.append(i[0])

        if entity in setList:
            # Testing set count value
            index = setList.index(entity)
            count = self.spanList[index][1]

            if int(clutchSet) > int(count):
                raise Exception(
                    'Clutch set for "'
                    + entity
                    + '" is exceeding declared span limit, kindly check your input .xky file'
                )
                # exit()

            # Adding in outDict
            # if entitystr not in dictList:
            self.outDict[entitystr] = {}

        else:
            raise Exception(
                'Clutch set for "'
                + entity
                + '" is not declared with span limit, kindly check your input .xky file'
            )
            # exit()

    # Enter a parse tree produced by XkyeParser#subclutchset.
    def enterSubclutchset(self, ctx: XkyeParser.SubclutchsetContext):
        if ctx.clutchdefheader() is not None:
            childCtx = ctx.clutchdefheader().entity().getText()
            clutchSet = 1
        else:
            childCtx = ctx.clutchsetheader().entity().getText()
            clutchSet = int(ctx.clutchsetheader().number().getText())

        ctx.subclutchgroup().clutch_Set = clutchSet
        ctx.subclutchgroup().parent_Ctx = childCtx

    # Enter a parse tree produced by XkyeParser#subclutchgroup.
    def enterSubclutchgroup(self, ctx: XkyeParser.SubclutchgroupContext):
        for child in ctx.children:
            child.parent_Ctx = ctx.parent_Ctx
            child.clutch_Set = ctx.clutch_Set

    # Enter a parse tree produced by XkyeParser#subclutch.
    def enterSubclutch(self, ctx: XkyeParser.SubclutchContext):
        subclutch = ctx.entity().getText()
        parent_Ctx = ctx.parent_Ctx
        parent_Set = ctx.clutch_Set

        clutchSet = ""
        dictSuffix = ""

        if ctx.number() is not None:
            clutchSet = ctx.number().getText()
            dictSuffix = ctx.number().getText()
        else:
            clutchSet = "1"

        setList = []
        setCount = []

        subclutchstr = subclutch + str(clutchSet)

        for i in self.spanList:
            setList.append(i[0])
            setCount.append(i[1])

        if subclutch not in setList:
            raise Exception(
                'Clutch set for "'
                + subclutch
                + '" is not defined, kindly check your input .xky file'
            )
            # exit()

        indexNo = setList.index(subclutch)

        if int(setCount[indexNo]) < int(clutchSet):
            raise Exception(
                'Clutch set for "'
                + subclutch
                + '" is exceeding declared span limit, kindly check your input .xky file'
            )
            # exit()

        dictKey = subclutch + dictSuffix
        dictList = list(self.outDict.keys())

        if parent_Set < 2:
            parent_Set = ""

        resultDictKey = parent_Ctx + str(parent_Set)

        tmpDictKeys = list(self.outDict[dictKey].keys())
        tmpDictValues = list(self.outDict[dictKey].values())

        # print(resultDictKey,dictKey)

        for key in tmpDictKeys:
            self.outDict[resultDictKey][key] = self.outDict[dictKey][key]

    # Enter a parse tree produced by XkyeParser#outstring.
    def enterOutstring(self, ctx: XkyeParser.OutstringContext):
        entity = ctx.entity().getText()
        substr = ""
        subnumber = ""

        if ctx.outstringsubset() is not None:
            substr = ctx.outstringsubset().entity().getText()

            if ctx.outstringsubset().number() is not None:
                subnumber = ctx.outstringsubset().number().getText()

        if substr == "" and subnumber == "":

            dictList = list(self.outDict["global"].keys())

            if entity not in dictList:
                raise Exception(
                    'Requested entity "'
                    + entity
                    + '" not declared above. kindly check your input .xky file'
                )
                # exit()

            result = self.outDict["global"][entity]
            print(result)

        elif subnumber == "":

            dictList = list(self.outDict.keys())

            if substr not in dictList:
                raise Exception(
                    'Requested clutch "'
                    + substr
                    + '" is not declared above. kindly check your input .xky file'
                )
                # exit()

            if entity not in list(self.outDict[substr].keys()):
                raise Exception(
                    'Requested entity "'
                    + entity
                    + '" not declared above. kindly check your input .xky file'
                )
                # exit()

            result = self.outDict[substr][entity]
            print(result)

        else:
            substrnew = substr + subnumber

            dictList = list(self.outDict.keys())

            if substrnew not in dictList:
                if substr in dictList:

                    if entity in list(self.outDict[substr].keys()):
                        result = self.outDict[substr][entity]
                        print(result)

                    else:
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
                    # exit()

            else:
                if entity not in list(self.outDict[substrnew].keys()):
                    if entity in list(self.outDict[substr].keys()):
                        result = self.outDict[substr][entity]
                        print(result)
                    else:
                        raise Exception(
                            'Requested entity "'
                            + entity
                            + '" not declared above. kindly check your input .xky file'
                        )

                else:
                    result = self.outDict[substrnew][entity]
                    print(result)
