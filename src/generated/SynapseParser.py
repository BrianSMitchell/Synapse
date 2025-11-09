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
        4,1,25,142,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,3,56,
        9,3,1,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,3,3,68,8,3,1,
        4,1,4,1,4,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,4,1,4,1,5,1,5,1,5,1,
        6,1,6,1,7,1,7,1,8,1,8,1,8,5,8,91,8,8,10,8,12,8,94,9,8,1,9,1,9,1,
        9,1,9,5,9,100,8,9,10,9,12,9,103,9,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,120,8,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,5,10,137,8,10,10,10,12,10,140,9,10,1,10,0,1,20,11,0,2,4,6,8,
        10,12,14,16,18,20,0,1,1,0,12,14,151,0,25,1,0,0,0,2,35,1,0,0,0,4,
        40,1,0,0,0,6,48,1,0,0,0,8,69,1,0,0,0,10,80,1,0,0,0,12,83,1,0,0,0,
        14,85,1,0,0,0,16,87,1,0,0,0,18,95,1,0,0,0,20,119,1,0,0,0,22,24,3,
        2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,
        28,1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,36,3,4,2,
        0,31,36,3,6,3,0,32,36,3,8,4,0,33,36,3,10,5,0,34,36,3,12,6,0,35,30,
        1,0,0,0,35,31,1,0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,
        36,38,1,0,0,0,37,39,5,1,0,0,38,37,1,0,0,0,38,39,1,0,0,0,39,3,1,0,
        0,0,40,41,5,2,0,0,41,42,5,22,0,0,42,43,5,3,0,0,43,44,3,14,7,0,44,
        45,5,4,0,0,45,46,3,16,8,0,46,47,5,5,0,0,47,5,1,0,0,0,48,49,5,6,0,
        0,49,50,3,20,10,0,50,54,5,7,0,0,51,53,3,2,1,0,52,51,1,0,0,0,53,56,
        1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,57,1,0,0,0,56,54,1,0,0,0,
        57,67,5,8,0,0,58,59,5,9,0,0,59,63,5,7,0,0,60,62,3,2,1,0,61,60,1,
        0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,
        63,1,0,0,0,66,68,5,8,0,0,67,58,1,0,0,0,67,68,1,0,0,0,68,7,1,0,0,
        0,69,70,5,10,0,0,70,71,5,22,0,0,71,75,5,7,0,0,72,74,3,18,9,0,73,
        72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,
        0,77,75,1,0,0,0,78,79,5,8,0,0,79,9,1,0,0,0,80,81,5,11,0,0,81,82,
        3,20,10,0,82,11,1,0,0,0,83,84,3,20,10,0,84,13,1,0,0,0,85,86,7,0,
        0,0,86,15,1,0,0,0,87,92,3,20,10,0,88,89,5,15,0,0,89,91,3,20,10,0,
        90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,17,1,
        0,0,0,94,92,1,0,0,0,95,96,5,6,0,0,96,97,3,20,10,0,97,101,5,7,0,0,
        98,100,3,2,1,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,
        102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,8,0,0,105,
        19,1,0,0,0,106,107,6,10,-1,0,107,120,5,22,0,0,108,120,5,23,0,0,109,
        120,5,24,0,0,110,111,5,4,0,0,111,112,3,20,10,0,112,113,5,5,0,0,113,
        120,1,0,0,0,114,115,5,21,0,0,115,116,5,4,0,0,116,117,3,20,10,0,117,
        118,5,5,0,0,118,120,1,0,0,0,119,106,1,0,0,0,119,108,1,0,0,0,119,
        109,1,0,0,0,119,110,1,0,0,0,119,114,1,0,0,0,120,138,1,0,0,0,121,
        122,10,7,0,0,122,123,5,16,0,0,123,137,3,20,10,8,124,125,10,6,0,0,
        125,126,5,17,0,0,126,137,3,20,10,7,127,128,10,5,0,0,128,129,5,18,
        0,0,129,137,3,20,10,6,130,131,10,4,0,0,131,132,5,19,0,0,132,137,
        3,20,10,5,133,134,10,3,0,0,134,135,5,20,0,0,135,137,3,20,10,4,136,
        121,1,0,0,0,136,124,1,0,0,0,136,127,1,0,0,0,136,130,1,0,0,0,136,
        133,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,
        21,1,0,0,0,140,138,1,0,0,0,12,25,35,38,54,63,67,75,92,101,119,136,
        138
    ]

class SynapseParser ( Parser ):

    grammarFileName = "Synapse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'let'", "'='", "'('", "')'", "'if'", 
                     "'{'", "'}'", "'else'", "'morph'", "'goal:'", "'normal'", 
                     "'bernoulli'", "'uniform'", "','", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'sample'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letStatement = 2
    RULE_ifStatement = 3
    RULE_morphStatement = 4
    RULE_goalStatement = 5
    RULE_exprStatement = 6
    RULE_distribution = 7
    RULE_exprList = 8
    RULE_rule = 9
    RULE_expr = 10

    ruleNames =  [ "program", "statement", "letStatement", "ifStatement", 
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
    ID=22
    NUMBER=23
    STRING=24
    WS=25

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31460436) != 0):
                self.state = 22
                self.statement()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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

        def letStatement(self):
            return self.getTypedRuleContext(SynapseParser.LetStatementContext,0)


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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 30
                self.letStatement()
                pass
            elif token in [6]:
                self.state = 31
                self.ifStatement()
                pass
            elif token in [10]:
                self.state = 32
                self.morphStatement()
                pass
            elif token in [11]:
                self.state = 33
                self.goalStatement()
                pass
            elif token in [4, 21, 22, 23, 24]:
                self.state = 34
                self.exprStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 37
                self.match(SynapseParser.T__0)


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

        def distribution(self):
            return self.getTypedRuleContext(SynapseParser.DistributionContext,0)


        def exprList(self):
            return self.getTypedRuleContext(SynapseParser.ExprListContext,0)


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
        self.enterRule(localctx, 4, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(SynapseParser.T__1)
            self.state = 41
            self.match(SynapseParser.ID)
            self.state = 42
            self.match(SynapseParser.T__2)
            self.state = 43
            self.distribution()
            self.state = 44
            self.match(SynapseParser.T__3)
            self.state = 45
            self.exprList()
            self.state = 46
            self.match(SynapseParser.T__4)
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
        self.enterRule(localctx, 6, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SynapseParser.T__5)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(SynapseParser.T__6)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31460436) != 0):
                self.state = 51
                self.statement()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(SynapseParser.T__7)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 58
                self.match(SynapseParser.T__8)
                self.state = 59
                self.match(SynapseParser.T__6)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31460436) != 0):
                    self.state = 60
                    self.statement()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(SynapseParser.T__7)


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
        self.enterRule(localctx, 8, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(SynapseParser.T__9)
            self.state = 70
            self.match(SynapseParser.ID)
            self.state = 71
            self.match(SynapseParser.T__6)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 72
                self.rule_()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(SynapseParser.T__7)
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
        self.enterRule(localctx, 10, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SynapseParser.T__10)
            self.state = 81
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
        self.enterRule(localctx, 12, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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
        self.enterRule(localctx, 14, self.RULE_distribution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expr(0)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 88
                self.match(SynapseParser.T__14)
                self.state = 89
                self.expr(0)
                self.state = 94
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
        self.enterRule(localctx, 18, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(SynapseParser.T__5)
            self.state = 96
            self.expr(0)
            self.state = 97
            self.match(SynapseParser.T__6)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 31460436) != 0):
                self.state = 98
                self.statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(SynapseParser.T__7)
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.state = 107
                self.match(SynapseParser.ID)
                pass
            elif token in [23]:
                self.state = 108
                self.match(SynapseParser.NUMBER)
                pass
            elif token in [24]:
                self.state = 109
                self.match(SynapseParser.STRING)
                pass
            elif token in [4]:
                self.state = 110
                self.match(SynapseParser.T__3)
                self.state = 111
                self.expr(0)
                self.state = 112
                self.match(SynapseParser.T__4)
                pass
            elif token in [21]:
                self.state = 114
                self.match(SynapseParser.T__20)
                self.state = 115
                self.match(SynapseParser.T__3)
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(SynapseParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 136
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 121
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 122
                        self.match(SynapseParser.T__15)
                        self.state = 123
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 124
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 125
                        self.match(SynapseParser.T__16)
                        self.state = 126
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 127
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 128
                        self.match(SynapseParser.T__17)
                        self.state = 129
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 130
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 131
                        self.match(SynapseParser.T__18)
                        self.state = 132
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 133
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 134
                        self.match(SynapseParser.T__19)
                        self.state = 135
                        self.expr(4)
                        pass

             
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




