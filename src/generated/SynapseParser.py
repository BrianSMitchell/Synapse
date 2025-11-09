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
        4,1,29,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,39,8,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,57,
        8,4,10,4,12,4,60,9,4,1,4,1,4,1,4,1,4,5,4,66,8,4,10,4,12,4,69,9,4,
        1,4,3,4,72,8,4,1,5,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,1,
        5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,95,8,9,10,9,12,9,98,
        9,9,1,10,1,10,1,10,1,10,5,10,104,8,10,10,10,12,10,107,9,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,128,8,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,151,8,11,10,11,12,11,154,9,11,1,11,0,1,22,12,
        0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,10,12,168,0,27,1,0,0,0,2,
        38,1,0,0,0,4,43,1,0,0,0,6,48,1,0,0,0,8,52,1,0,0,0,10,73,1,0,0,0,
        12,84,1,0,0,0,14,87,1,0,0,0,16,89,1,0,0,0,18,91,1,0,0,0,20,99,1,
        0,0,0,22,127,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,29,1,0,0,0,27,
        25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,5,0,0,
        1,31,1,1,0,0,0,32,39,3,4,2,0,33,39,3,6,3,0,34,39,3,8,4,0,35,39,3,
        10,5,0,36,39,3,12,6,0,37,39,3,14,7,0,38,32,1,0,0,0,38,33,1,0,0,0,
        38,34,1,0,0,0,38,35,1,0,0,0,38,36,1,0,0,0,38,37,1,0,0,0,39,41,1,
        0,0,0,40,42,5,1,0,0,41,40,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,
        44,5,2,0,0,44,45,5,26,0,0,45,46,5,3,0,0,46,47,3,22,11,0,47,5,1,0,
        0,0,48,49,5,26,0,0,49,50,5,3,0,0,50,51,3,22,11,0,51,7,1,0,0,0,52,
        53,5,4,0,0,53,54,3,22,11,0,54,58,5,5,0,0,55,57,3,2,1,0,56,55,1,0,
        0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,61,1,0,0,0,60,58,
        1,0,0,0,61,71,5,6,0,0,62,63,5,7,0,0,63,67,5,5,0,0,64,66,3,2,1,0,
        65,64,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,
        0,0,0,69,67,1,0,0,0,70,72,5,6,0,0,71,62,1,0,0,0,71,72,1,0,0,0,72,
        9,1,0,0,0,73,74,5,8,0,0,74,75,5,26,0,0,75,79,5,5,0,0,76,78,3,20,
        10,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,
        82,1,0,0,0,81,79,1,0,0,0,82,83,5,6,0,0,83,11,1,0,0,0,84,85,5,9,0,
        0,85,86,3,22,11,0,86,13,1,0,0,0,87,88,3,22,11,0,88,15,1,0,0,0,89,
        90,7,0,0,0,90,17,1,0,0,0,91,96,3,22,11,0,92,93,5,13,0,0,93,95,3,
        22,11,0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,
        97,19,1,0,0,0,98,96,1,0,0,0,99,100,5,4,0,0,100,101,3,22,11,0,101,
        105,5,5,0,0,102,104,3,2,1,0,103,102,1,0,0,0,104,107,1,0,0,0,105,
        103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,
        109,5,6,0,0,109,21,1,0,0,0,110,111,6,11,-1,0,111,128,5,26,0,0,112,
        128,5,27,0,0,113,128,5,28,0,0,114,115,5,14,0,0,115,116,3,18,9,0,
        116,117,5,15,0,0,117,128,1,0,0,0,118,119,5,23,0,0,119,120,3,22,11,
        0,120,121,5,24,0,0,121,128,1,0,0,0,122,123,5,25,0,0,123,124,5,23,
        0,0,124,125,3,22,11,0,125,126,5,24,0,0,126,128,1,0,0,0,127,110,1,
        0,0,0,127,112,1,0,0,0,127,113,1,0,0,0,127,114,1,0,0,0,127,118,1,
        0,0,0,127,122,1,0,0,0,128,152,1,0,0,0,129,130,10,9,0,0,130,131,5,
        16,0,0,131,151,3,22,11,10,132,133,10,8,0,0,133,134,5,17,0,0,134,
        151,3,22,11,9,135,136,10,7,0,0,136,137,5,18,0,0,137,151,3,22,11,
        8,138,139,10,6,0,0,139,140,5,19,0,0,140,151,3,22,11,7,141,142,10,
        5,0,0,142,143,5,20,0,0,143,151,3,22,11,6,144,145,10,4,0,0,145,146,
        5,21,0,0,146,151,3,22,11,5,147,148,10,3,0,0,148,149,5,22,0,0,149,
        151,3,22,11,4,150,129,1,0,0,0,150,132,1,0,0,0,150,135,1,0,0,0,150,
        138,1,0,0,0,150,141,1,0,0,0,150,144,1,0,0,0,150,147,1,0,0,0,151,
        154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,23,1,0,0,0,154,152,
        1,0,0,0,12,27,38,41,58,67,71,79,96,105,127,150,152
    ]

class SynapseParser ( Parser ):

    grammarFileName = "Synapse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'let'", "'='", "'if'", "'{'", 
                     "'}'", "'else'", "'morph'", "'goal:'", "'normal'", 
                     "'bernoulli'", "'uniform'", "','", "'['", "']'", "'+'", 
                     "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'('", "')'", 
                     "'sample'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letStatement = 2
    RULE_assignStatement = 3
    RULE_ifStatement = 4
    RULE_morphStatement = 5
    RULE_goalStatement = 6
    RULE_exprStatement = 7
    RULE_distribution = 8
    RULE_exprList = 9
    RULE_rule = 10
    RULE_expr = 11

    ruleNames =  [ "program", "statement", "letStatement", "assignStatement", 
                   "ifStatement", "morphStatement", "goalStatement", "exprStatement", 
                   "distribution", "exprList", "rule", "expr" ]

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
    ID=26
    NUMBER=27
    STRING=28
    WS=29

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 511722260) != 0):
                self.state = 24
                self.statement()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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


        def assignStatement(self):
            return self.getTypedRuleContext(SynapseParser.AssignStatementContext,0)


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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 32
                self.letStatement()
                pass

            elif la_ == 2:
                self.state = 33
                self.assignStatement()
                pass

            elif la_ == 3:
                self.state = 34
                self.ifStatement()
                pass

            elif la_ == 4:
                self.state = 35
                self.morphStatement()
                pass

            elif la_ == 5:
                self.state = 36
                self.goalStatement()
                pass

            elif la_ == 6:
                self.state = 37
                self.exprStatement()
                pass


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 40
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
        self.enterRule(localctx, 4, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(SynapseParser.T__1)
            self.state = 44
            self.match(SynapseParser.ID)
            self.state = 45
            self.match(SynapseParser.T__2)
            self.state = 46
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
        self.enterRule(localctx, 6, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SynapseParser.ID)
            self.state = 49
            self.match(SynapseParser.T__2)
            self.state = 50
            self.expr(0)
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
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SynapseParser.T__3)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(SynapseParser.T__4)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 511722260) != 0):
                self.state = 55
                self.statement()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(SynapseParser.T__5)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 62
                self.match(SynapseParser.T__6)
                self.state = 63
                self.match(SynapseParser.T__4)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 511722260) != 0):
                    self.state = 64
                    self.statement()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
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
        self.enterRule(localctx, 10, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SynapseParser.T__7)
            self.state = 74
            self.match(SynapseParser.ID)
            self.state = 75
            self.match(SynapseParser.T__4)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 76
                self.rule_()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
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
        self.enterRule(localctx, 12, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SynapseParser.T__8)
            self.state = 85
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
        self.enterRule(localctx, 14, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 16, self.RULE_distribution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
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
        self.enterRule(localctx, 18, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.expr(0)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 92
                self.match(SynapseParser.T__12)
                self.state = 93
                self.expr(0)
                self.state = 98
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
        self.enterRule(localctx, 20, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(SynapseParser.T__3)
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(SynapseParser.T__4)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 511722260) != 0):
                self.state = 102
                self.statement()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 111
                self.match(SynapseParser.ID)
                pass
            elif token in [27]:
                self.state = 112
                self.match(SynapseParser.NUMBER)
                pass
            elif token in [28]:
                self.state = 113
                self.match(SynapseParser.STRING)
                pass
            elif token in [14]:
                self.state = 114
                self.match(SynapseParser.T__13)
                self.state = 115
                self.exprList()
                self.state = 116
                self.match(SynapseParser.T__14)
                pass
            elif token in [23]:
                self.state = 118
                self.match(SynapseParser.T__22)
                self.state = 119
                self.expr(0)
                self.state = 120
                self.match(SynapseParser.T__23)
                pass
            elif token in [25]:
                self.state = 122
                self.match(SynapseParser.T__24)
                self.state = 123
                self.match(SynapseParser.T__22)
                self.state = 124
                self.expr(0)
                self.state = 125
                self.match(SynapseParser.T__23)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 130
                        self.match(SynapseParser.T__15)
                        self.state = 131
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 133
                        self.match(SynapseParser.T__16)
                        self.state = 134
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 136
                        self.match(SynapseParser.T__17)
                        self.state = 137
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 139
                        self.match(SynapseParser.T__18)
                        self.state = 140
                        self.expr(7)
                        pass

                    elif la_ == 5:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 142
                        self.match(SynapseParser.T__19)
                        self.state = 143
                        self.expr(6)
                        pass

                    elif la_ == 6:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 145
                        self.match(SynapseParser.T__20)
                        self.state = 146
                        self.expr(5)
                        pass

                    elif la_ == 7:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 148
                        self.match(SynapseParser.T__21)
                        self.state = 149
                        self.expr(4)
                        pass

             
                self.state = 154
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
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




