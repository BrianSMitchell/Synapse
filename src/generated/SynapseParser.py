# Generated from grammar/Synapse.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,228,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,47,8,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,3,2,
        56,8,2,1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,3,1,3,1,
        3,5,3,71,8,3,10,3,12,3,74,9,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,91,8,6,10,6,12,6,94,9,6,1,6,1,6,1,
        7,1,7,1,7,1,7,5,7,102,8,7,10,7,12,7,105,9,7,1,7,1,7,1,7,1,7,5,7,
        111,8,7,10,7,12,7,114,9,7,1,7,3,7,117,8,7,1,8,1,8,1,8,1,8,5,8,123,
        8,8,10,8,12,8,126,9,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,
        12,1,12,1,12,5,12,140,8,12,10,12,12,12,143,9,12,1,13,1,13,1,13,1,
        13,5,13,149,8,13,10,13,12,13,152,9,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,180,8,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,
        14,223,8,14,10,14,12,14,226,9,14,1,14,0,1,28,15,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,0,1,1,0,16,18,251,0,33,1,0,0,0,2,46,1,0,
        0,0,4,51,1,0,0,0,6,67,1,0,0,0,8,75,1,0,0,0,10,80,1,0,0,0,12,84,1,
        0,0,0,14,97,1,0,0,0,16,118,1,0,0,0,18,129,1,0,0,0,20,132,1,0,0,0,
        22,134,1,0,0,0,24,136,1,0,0,0,26,144,1,0,0,0,28,179,1,0,0,0,30,32,
        3,2,1,0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,
        34,36,1,0,0,0,35,33,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,0,38,47,3,4,
        2,0,39,47,3,8,4,0,40,47,3,10,5,0,41,47,3,12,6,0,42,47,3,14,7,0,43,
        47,3,16,8,0,44,47,3,18,9,0,45,47,3,20,10,0,46,38,1,0,0,0,46,39,1,
        0,0,0,46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,46,43,1,0,0,0,46,
        44,1,0,0,0,46,45,1,0,0,0,47,49,1,0,0,0,48,50,5,1,0,0,49,48,1,0,0,
        0,49,50,1,0,0,0,50,3,1,0,0,0,51,52,5,2,0,0,52,53,5,34,0,0,53,55,
        5,3,0,0,54,56,3,6,3,0,55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,
        57,58,5,4,0,0,58,62,5,5,0,0,59,61,3,2,1,0,60,59,1,0,0,0,61,64,1,
        0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,65,1,0,0,0,64,62,1,0,0,0,65,
        66,5,6,0,0,66,5,1,0,0,0,67,72,5,34,0,0,68,69,5,7,0,0,69,71,5,34,
        0,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,7,
        1,0,0,0,74,72,1,0,0,0,75,76,5,8,0,0,76,77,5,34,0,0,77,78,5,9,0,0,
        78,79,3,28,14,0,79,9,1,0,0,0,80,81,5,34,0,0,81,82,5,9,0,0,82,83,
        3,28,14,0,83,11,1,0,0,0,84,85,5,10,0,0,85,86,5,34,0,0,86,87,5,11,
        0,0,87,88,3,28,14,0,88,92,5,5,0,0,89,91,3,2,1,0,90,89,1,0,0,0,91,
        94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,
        0,95,96,5,6,0,0,96,13,1,0,0,0,97,98,5,12,0,0,98,99,3,28,14,0,99,
        103,5,5,0,0,100,102,3,2,1,0,101,100,1,0,0,0,102,105,1,0,0,0,103,
        101,1,0,0,0,103,104,1,0,0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,
        116,5,6,0,0,107,108,5,13,0,0,108,112,5,5,0,0,109,111,3,2,1,0,110,
        109,1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,
        115,1,0,0,0,114,112,1,0,0,0,115,117,5,6,0,0,116,107,1,0,0,0,116,
        117,1,0,0,0,117,15,1,0,0,0,118,119,5,14,0,0,119,120,5,34,0,0,120,
        124,5,5,0,0,121,123,3,26,13,0,122,121,1,0,0,0,123,126,1,0,0,0,124,
        122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,124,1,0,0,0,127,
        128,5,6,0,0,128,17,1,0,0,0,129,130,5,15,0,0,130,131,3,28,14,0,131,
        19,1,0,0,0,132,133,3,28,14,0,133,21,1,0,0,0,134,135,7,0,0,0,135,
        23,1,0,0,0,136,141,3,28,14,0,137,138,5,7,0,0,138,140,3,28,14,0,139,
        137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,
        25,1,0,0,0,143,141,1,0,0,0,144,145,5,12,0,0,145,146,3,28,14,0,146,
        150,5,5,0,0,147,149,3,2,1,0,148,147,1,0,0,0,149,152,1,0,0,0,150,
        148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,
        154,5,6,0,0,154,27,1,0,0,0,155,156,6,14,-1,0,156,180,5,34,0,0,157,
        180,5,35,0,0,158,159,5,19,0,0,159,180,5,35,0,0,160,180,5,36,0,0,
        161,162,5,20,0,0,162,163,3,24,12,0,163,164,5,21,0,0,164,180,1,0,
        0,0,165,166,5,34,0,0,166,167,5,3,0,0,167,168,3,24,12,0,168,169,5,
        4,0,0,169,180,1,0,0,0,170,171,5,3,0,0,171,172,3,28,14,0,172,173,
        5,4,0,0,173,180,1,0,0,0,174,175,5,33,0,0,175,176,5,3,0,0,176,177,
        3,28,14,0,177,178,5,4,0,0,178,180,1,0,0,0,179,155,1,0,0,0,179,157,
        1,0,0,0,179,158,1,0,0,0,179,160,1,0,0,0,179,161,1,0,0,0,179,165,
        1,0,0,0,179,170,1,0,0,0,179,174,1,0,0,0,180,224,1,0,0,0,181,182,
        10,14,0,0,182,183,5,22,0,0,183,223,3,28,14,15,184,185,10,13,0,0,
        185,186,5,19,0,0,186,223,3,28,14,14,187,188,10,12,0,0,188,189,5,
        23,0,0,189,223,3,28,14,13,190,191,10,11,0,0,191,192,5,24,0,0,192,
        223,3,28,14,12,193,194,10,10,0,0,194,195,5,25,0,0,195,223,3,28,14,
        11,196,197,10,9,0,0,197,198,5,26,0,0,198,223,3,28,14,10,199,200,
        10,8,0,0,200,201,5,27,0,0,201,223,3,28,14,9,202,203,10,7,0,0,203,
        204,5,28,0,0,204,223,3,28,14,8,205,206,10,6,0,0,206,207,5,29,0,0,
        207,223,3,28,14,7,208,209,10,5,0,0,209,210,5,30,0,0,210,223,3,28,
        14,6,211,212,10,4,0,0,212,213,5,31,0,0,213,223,3,28,14,5,214,215,
        10,3,0,0,215,216,5,32,0,0,216,223,3,28,14,4,217,218,10,15,0,0,218,
        219,5,20,0,0,219,220,3,28,14,0,220,221,5,21,0,0,221,223,1,0,0,0,
        222,181,1,0,0,0,222,184,1,0,0,0,222,187,1,0,0,0,222,190,1,0,0,0,
        222,193,1,0,0,0,222,196,1,0,0,0,222,199,1,0,0,0,222,202,1,0,0,0,
        222,205,1,0,0,0,222,208,1,0,0,0,222,211,1,0,0,0,222,214,1,0,0,0,
        222,217,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,
        225,29,1,0,0,0,226,224,1,0,0,0,16,33,46,49,55,62,72,92,103,112,116,
        124,141,150,179,222,224
    ]

class SynapseParser ( Parser ):

    grammarFileName = "Synapse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'def'", "'('", "')'", "'{'", "'}'", 
                     "','", "'let'", "'='", "'for'", "'in'", "'if'", "'else'", 
                     "'morph'", "'goal:'", "'normal'", "'bernoulli'", "'uniform'", 
                     "'-'", "'['", "']'", "'+'", "'*'", "'/'", "'>'", "'<'", 
                     "'>='", "'<='", "'=='", "'!='", "'and'", "'or'", "'sample'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_funcStatement = 2
    RULE_paramList = 3
    RULE_letStatement = 4
    RULE_assignStatement = 5
    RULE_forStatement = 6
    RULE_ifStatement = 7
    RULE_morphStatement = 8
    RULE_goalStatement = 9
    RULE_exprStatement = 10
    RULE_distribution = 11
    RULE_exprList = 12
    RULE_rule = 13
    RULE_expr = 14

    ruleNames =  [ "program", "statement", "funcStatement", "paramList", 
                   "letStatement", "assignStatement", "forStatement", "ifStatement", 
                   "morphStatement", "goalStatement", "exprStatement", "distribution", 
                   "exprList", "rule", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    ID=34
    NUMBER=35
    STRING=36
    COMMENT=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SynapseParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SynapseParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                self.state = 30
                self.statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 36
            self.match(SynapseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcStatement(self):
            return self.getTypedRuleContext(SynapseParser.FuncStatementContext,0)


        def letStatement(self):
            return self.getTypedRuleContext(SynapseParser.LetStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(SynapseParser.AssignStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(SynapseParser.ForStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(SynapseParser.IfStatementContext,0)


        def morphStatement(self):
            return self.getTypedRuleContext(SynapseParser.MorphStatementContext,0)


        def goalStatement(self):
            return self.getTypedRuleContext(SynapseParser.GoalStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(SynapseParser.ExprStatementContext,0)


        def getRuleIndex(self):
            return SynapseParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SynapseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 38
                self.funcStatement()
                pass

            elif la_ == 2:
                self.state = 39
                self.letStatement()
                pass

            elif la_ == 3:
                self.state = 40
                self.assignStatement()
                pass

            elif la_ == 4:
                self.state = 41
                self.forStatement()
                pass

            elif la_ == 5:
                self.state = 42
                self.ifStatement()
                pass

            elif la_ == 6:
                self.state = 43
                self.morphStatement()
                pass

            elif la_ == 7:
                self.state = 44
                self.goalStatement()
                pass

            elif la_ == 8:
                self.state = 45
                self.exprStatement()
                pass


            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 48
                self.match(SynapseParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(SynapseParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_funcStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncStatement" ):
                listener.enterFuncStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncStatement" ):
                listener.exitFuncStatement(self)




    def funcStatement(self):

        localctx = SynapseParser.FuncStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(SynapseParser.T__1)
            self.state = 52
            self.match(SynapseParser.ID)
            self.state = 53
            self.match(SynapseParser.T__2)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 54
                self.paramList()


            self.state = 57
            self.match(SynapseParser.T__3)
            self.state = 58
            self.match(SynapseParser.T__4)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                self.state = 59
                self.statement()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(SynapseParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SynapseParser.ID)
            else:
                return self.getToken(SynapseParser.ID, i)

        def getRuleIndex(self):
            return SynapseParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = SynapseParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SynapseParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 68
                self.match(SynapseParser.T__6)
                self.state = 69
                self.match(SynapseParser.ID)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def getRuleIndex(self):
            return SynapseParser.RULE_letStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStatement" ):
                listener.enterLetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStatement" ):
                listener.exitLetStatement(self)




    def letStatement(self):

        localctx = SynapseParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(SynapseParser.T__7)
            self.state = 76
            self.match(SynapseParser.ID)
            self.state = 77
            self.match(SynapseParser.T__8)
            self.state = 78
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def getRuleIndex(self):
            return SynapseParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)




    def assignStatement(self):

        localctx = SynapseParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SynapseParser.ID)
            self.state = 81
            self.match(SynapseParser.T__8)
            self.state = 82
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = SynapseParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SynapseParser.T__9)
            self.state = 85
            self.match(SynapseParser.ID)
            self.state = 86
            self.match(SynapseParser.T__10)
            self.state = 87
            self.expr(0)
            self.state = 88
            self.match(SynapseParser.T__4)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                self.state = 89
                self.statement()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
            self.match(SynapseParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = SynapseParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(SynapseParser.T__11)
            self.state = 98
            self.expr(0)
            self.state = 99
            self.match(SynapseParser.T__4)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                self.state = 100
                self.statement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(SynapseParser.T__5)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 107
                self.match(SynapseParser.T__12)
                self.state = 108
                self.match(SynapseParser.T__4)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                    self.state = 109
                    self.statement()
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(SynapseParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MorphStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.RuleContext)
            else:
                return self.getTypedRuleContext(SynapseParser.RuleContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_morphStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMorphStatement" ):
                listener.enterMorphStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMorphStatement" ):
                listener.exitMorphStatement(self)




    def morphStatement(self):

        localctx = SynapseParser.MorphStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(SynapseParser.T__13)
            self.state = 119
            self.match(SynapseParser.ID)
            self.state = 120
            self.match(SynapseParser.T__4)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 121
                self.rule_()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 127
            self.match(SynapseParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def getRuleIndex(self):
            return SynapseParser.RULE_goalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoalStatement" ):
                listener.enterGoalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoalStatement" ):
                listener.exitGoalStatement(self)




    def goalStatement(self):

        localctx = SynapseParser.GoalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(SynapseParser.T__14)
            self.state = 130
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def getRuleIndex(self):
            return SynapseParser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)




    def exprStatement(self):

        localctx = SynapseParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DistributionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SynapseParser.RULE_distribution

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDistribution" ):
                listener.enterDistribution(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDistribution" ):
                listener.exitDistribution(self)




    def distribution(self):

        localctx = SynapseParser.DistributionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_distribution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.ExprContext)
            else:
                return self.getTypedRuleContext(SynapseParser.ExprContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)




    def exprList(self):

        localctx = SynapseParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expr(0)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 137
                self.match(SynapseParser.T__6)
                self.state = 138
                self.expr(0)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SynapseParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)




    def rule_(self):

        localctx = SynapseParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(SynapseParser.T__11)
            self.state = 145
            self.expr(0)
            self.state = 146
            self.match(SynapseParser.T__4)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128850646284) != 0):
                self.state = 147
                self.statement()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(SynapseParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def NUMBER(self):
            return self.getToken(SynapseParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(SynapseParser.STRING, 0)

        def exprList(self):
            return self.getTypedRuleContext(SynapseParser.ExprListContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.ExprContext)
            else:
                return self.getTypedRuleContext(SynapseParser.ExprContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SynapseParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 156
                self.match(SynapseParser.ID)
                pass

            elif la_ == 2:
                self.state = 157
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 158
                self.match(SynapseParser.T__18)
                self.state = 159
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 160
                self.match(SynapseParser.STRING)
                pass

            elif la_ == 5:
                self.state = 161
                self.match(SynapseParser.T__19)
                self.state = 162
                self.exprList()
                self.state = 163
                self.match(SynapseParser.T__20)
                pass

            elif la_ == 6:
                self.state = 165
                self.match(SynapseParser.ID)
                self.state = 166
                self.match(SynapseParser.T__2)
                self.state = 167
                self.exprList()
                self.state = 168
                self.match(SynapseParser.T__3)
                pass

            elif la_ == 7:
                self.state = 170
                self.match(SynapseParser.T__2)
                self.state = 171
                self.expr(0)
                self.state = 172
                self.match(SynapseParser.T__3)
                pass

            elif la_ == 8:
                self.state = 174
                self.match(SynapseParser.T__32)
                self.state = 175
                self.match(SynapseParser.T__2)
                self.state = 176
                self.expr(0)
                self.state = 177
                self.match(SynapseParser.T__3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 182
                        self.match(SynapseParser.T__21)
                        self.state = 183
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 185
                        self.match(SynapseParser.T__18)
                        self.state = 186
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 188
                        self.match(SynapseParser.T__22)
                        self.state = 189
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 191
                        self.match(SynapseParser.T__23)
                        self.state = 192
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 194
                        self.match(SynapseParser.T__24)
                        self.state = 195
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 196
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 197
                        self.match(SynapseParser.T__25)
                        self.state = 198
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 200
                        self.match(SynapseParser.T__26)
                        self.state = 201
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 203
                        self.match(SynapseParser.T__27)
                        self.state = 204
                        self.expr(8)
                        pass

                    elif la_ == 9:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 206
                        self.match(SynapseParser.T__28)
                        self.state = 207
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 209
                        self.match(SynapseParser.T__29)
                        self.state = 210
                        self.expr(6)
                        pass

                    elif la_ == 11:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 211
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 212
                        self.match(SynapseParser.T__30)
                        self.state = 213
                        self.expr(5)
                        pass

                    elif la_ == 12:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 215
                        self.match(SynapseParser.T__31)
                        self.state = 216
                        self.expr(4)
                        pass

                    elif la_ == 13:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 218
                        self.match(SynapseParser.T__19)
                        self.state = 219
                        self.expr(0)
                        self.state = 220
                        self.match(SynapseParser.T__20)
                        pass

             
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 15)
         




