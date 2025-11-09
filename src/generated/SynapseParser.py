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
        4,1,39,234,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,1,3,1,53,8,1,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,3,3,62,8,3,1,3,1,3,1,3,5,3,67,8,3,10,3,12,
        3,70,9,3,1,3,1,3,1,4,1,4,1,4,5,4,77,8,4,10,4,12,4,80,9,4,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,97,8,7,10,
        7,12,7,100,9,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,108,8,8,10,8,12,8,111,
        9,8,1,8,1,8,1,8,1,8,5,8,117,8,8,10,8,12,8,120,9,8,1,8,3,8,123,8,
        8,1,9,1,9,1,9,1,9,5,9,129,8,9,10,9,12,9,132,9,9,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,5,13,146,8,13,10,13,12,13,
        149,9,13,1,14,1,14,1,14,1,14,5,14,155,8,14,10,14,12,14,158,9,14,
        1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,186,8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,5,15,229,8,15,10,15,12,15,232,9,15,1,15,
        0,1,30,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,1,1,0,17,
        19,257,0,35,1,0,0,0,2,49,1,0,0,0,4,54,1,0,0,0,6,57,1,0,0,0,8,73,
        1,0,0,0,10,81,1,0,0,0,12,86,1,0,0,0,14,90,1,0,0,0,16,103,1,0,0,0,
        18,124,1,0,0,0,20,135,1,0,0,0,22,138,1,0,0,0,24,140,1,0,0,0,26,142,
        1,0,0,0,28,150,1,0,0,0,30,185,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,
        0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,
        1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,50,3,4,2,0,41,50,3,6,3,0,42,
        50,3,10,5,0,43,50,3,12,6,0,44,50,3,14,7,0,45,50,3,16,8,0,46,50,3,
        18,9,0,47,50,3,20,10,0,48,50,3,22,11,0,49,40,1,0,0,0,49,41,1,0,0,
        0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,
        1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,52,1,0,0,0,51,53,5,1,0,0,
        52,51,1,0,0,0,52,53,1,0,0,0,53,3,1,0,0,0,54,55,5,2,0,0,55,56,5,37,
        0,0,56,5,1,0,0,0,57,58,5,3,0,0,58,59,5,35,0,0,59,61,5,4,0,0,60,62,
        3,8,4,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,5,0,0,
        64,68,5,6,0,0,65,67,3,2,1,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,
        0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,7,0,0,72,
        7,1,0,0,0,73,78,5,35,0,0,74,75,5,8,0,0,75,77,5,35,0,0,76,74,1,0,
        0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,9,1,0,0,0,80,78,
        1,0,0,0,81,82,5,9,0,0,82,83,5,35,0,0,83,84,5,10,0,0,84,85,3,30,15,
        0,85,11,1,0,0,0,86,87,5,35,0,0,87,88,5,10,0,0,88,89,3,30,15,0,89,
        13,1,0,0,0,90,91,5,11,0,0,91,92,5,35,0,0,92,93,5,12,0,0,93,94,3,
        30,15,0,94,98,5,6,0,0,95,97,3,2,1,0,96,95,1,0,0,0,97,100,1,0,0,0,
        98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,102,
        5,7,0,0,102,15,1,0,0,0,103,104,5,13,0,0,104,105,3,30,15,0,105,109,
        5,6,0,0,106,108,3,2,1,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,
        1,0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,112,122,
        5,7,0,0,113,114,5,14,0,0,114,118,5,6,0,0,115,117,3,2,1,0,116,115,
        1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,
        1,0,0,0,120,118,1,0,0,0,121,123,5,7,0,0,122,113,1,0,0,0,122,123,
        1,0,0,0,123,17,1,0,0,0,124,125,5,15,0,0,125,126,5,35,0,0,126,130,
        5,6,0,0,127,129,3,28,14,0,128,127,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,133,1,0,0,0,132,130,1,0,0,0,133,134,
        5,7,0,0,134,19,1,0,0,0,135,136,5,16,0,0,136,137,3,30,15,0,137,21,
        1,0,0,0,138,139,3,30,15,0,139,23,1,0,0,0,140,141,7,0,0,0,141,25,
        1,0,0,0,142,147,3,30,15,0,143,144,5,8,0,0,144,146,3,30,15,0,145,
        143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        27,1,0,0,0,149,147,1,0,0,0,150,151,5,13,0,0,151,152,3,30,15,0,152,
        156,5,6,0,0,153,155,3,2,1,0,154,153,1,0,0,0,155,158,1,0,0,0,156,
        154,1,0,0,0,156,157,1,0,0,0,157,159,1,0,0,0,158,156,1,0,0,0,159,
        160,5,7,0,0,160,29,1,0,0,0,161,162,6,15,-1,0,162,186,5,35,0,0,163,
        186,5,36,0,0,164,165,5,20,0,0,165,186,5,36,0,0,166,186,5,37,0,0,
        167,168,5,21,0,0,168,169,3,26,13,0,169,170,5,22,0,0,170,186,1,0,
        0,0,171,172,5,35,0,0,172,173,5,4,0,0,173,174,3,26,13,0,174,175,5,
        5,0,0,175,186,1,0,0,0,176,177,5,4,0,0,177,178,3,30,15,0,178,179,
        5,5,0,0,179,186,1,0,0,0,180,181,5,34,0,0,181,182,5,4,0,0,182,183,
        3,30,15,0,183,184,5,5,0,0,184,186,1,0,0,0,185,161,1,0,0,0,185,163,
        1,0,0,0,185,164,1,0,0,0,185,166,1,0,0,0,185,167,1,0,0,0,185,171,
        1,0,0,0,185,176,1,0,0,0,185,180,1,0,0,0,186,230,1,0,0,0,187,188,
        10,14,0,0,188,189,5,23,0,0,189,229,3,30,15,15,190,191,10,13,0,0,
        191,192,5,20,0,0,192,229,3,30,15,14,193,194,10,12,0,0,194,195,5,
        24,0,0,195,229,3,30,15,13,196,197,10,11,0,0,197,198,5,25,0,0,198,
        229,3,30,15,12,199,200,10,10,0,0,200,201,5,26,0,0,201,229,3,30,15,
        11,202,203,10,9,0,0,203,204,5,27,0,0,204,229,3,30,15,10,205,206,
        10,8,0,0,206,207,5,28,0,0,207,229,3,30,15,9,208,209,10,7,0,0,209,
        210,5,29,0,0,210,229,3,30,15,8,211,212,10,6,0,0,212,213,5,30,0,0,
        213,229,3,30,15,7,214,215,10,5,0,0,215,216,5,31,0,0,216,229,3,30,
        15,6,217,218,10,4,0,0,218,219,5,32,0,0,219,229,3,30,15,5,220,221,
        10,3,0,0,221,222,5,33,0,0,222,229,3,30,15,4,223,224,10,15,0,0,224,
        225,5,21,0,0,225,226,3,30,15,0,226,227,5,22,0,0,227,229,1,0,0,0,
        228,187,1,0,0,0,228,190,1,0,0,0,228,193,1,0,0,0,228,196,1,0,0,0,
        228,199,1,0,0,0,228,202,1,0,0,0,228,205,1,0,0,0,228,208,1,0,0,0,
        228,211,1,0,0,0,228,214,1,0,0,0,228,217,1,0,0,0,228,220,1,0,0,0,
        228,223,1,0,0,0,229,232,1,0,0,0,230,228,1,0,0,0,230,231,1,0,0,0,
        231,31,1,0,0,0,232,230,1,0,0,0,16,35,49,52,61,68,78,98,109,118,122,
        130,147,156,185,228,230
    ]

class SynapseParser ( Parser ):

    grammarFileName = "Synapse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'import'", "'def'", "'('", "')'", 
                     "'{'", "'}'", "','", "'let'", "'='", "'for'", "'in'", 
                     "'if'", "'else'", "'morph'", "'goal:'", "'normal'", 
                     "'bernoulli'", "'uniform'", "'-'", "'['", "']'", "'+'", 
                     "'*'", "'/'", "'>'", "'<'", "'>='", "'<='", "'=='", 
                     "'!='", "'and'", "'or'", "'sample'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_importStatement = 2
    RULE_funcStatement = 3
    RULE_paramList = 4
    RULE_letStatement = 5
    RULE_assignStatement = 6
    RULE_forStatement = 7
    RULE_ifStatement = 8
    RULE_morphStatement = 9
    RULE_goalStatement = 10
    RULE_exprStatement = 11
    RULE_distribution = 12
    RULE_exprList = 13
    RULE_rule = 14
    RULE_expr = 15

    ruleNames =  [ "program", "statement", "importStatement", "funcStatement", 
                   "paramList", "letStatement", "assignStatement", "forStatement", 
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
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    ID=35
    NUMBER=36
    STRING=37
    COMMENT=38
    WS=39

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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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

        def importStatement(self):
            return self.getTypedRuleContext(SynapseParser.ImportStatementContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 40
                self.importStatement()
                pass

            elif la_ == 2:
                self.state = 41
                self.funcStatement()
                pass

            elif la_ == 3:
                self.state = 42
                self.letStatement()
                pass

            elif la_ == 4:
                self.state = 43
                self.assignStatement()
                pass

            elif la_ == 5:
                self.state = 44
                self.forStatement()
                pass

            elif la_ == 6:
                self.state = 45
                self.ifStatement()
                pass

            elif la_ == 7:
                self.state = 46
                self.morphStatement()
                pass

            elif la_ == 8:
                self.state = 47
                self.goalStatement()
                pass

            elif la_ == 9:
                self.state = 48
                self.exprStatement()
                pass


            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 51
                self.match(SynapseParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SynapseParser.STRING, 0)

        def getRuleIndex(self):
            return SynapseParser.RULE_importStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStatement" ):
                listener.enterImportStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStatement" ):
                listener.exitImportStatement(self)




    def importStatement(self):

        localctx = SynapseParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SynapseParser.T__1)
            self.state = 55
            self.match(SynapseParser.STRING)
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
        self.enterRule(localctx, 6, self.RULE_funcStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SynapseParser.T__2)
            self.state = 58
            self.match(SynapseParser.ID)
            self.state = 59
            self.match(SynapseParser.T__3)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 60
                self.paramList()


            self.state = 63
            self.match(SynapseParser.T__4)
            self.state = 64
            self.match(SynapseParser.T__5)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                self.state = 65
                self.statement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(SynapseParser.T__6)
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
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SynapseParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 74
                self.match(SynapseParser.T__7)
                self.state = 75
                self.match(SynapseParser.ID)
                self.state = 80
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
        self.enterRule(localctx, 10, self.RULE_letStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SynapseParser.T__8)
            self.state = 82
            self.match(SynapseParser.ID)
            self.state = 83
            self.match(SynapseParser.T__9)
            self.state = 84
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
        self.enterRule(localctx, 12, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SynapseParser.ID)
            self.state = 87
            self.match(SynapseParser.T__9)
            self.state = 88
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
        self.enterRule(localctx, 14, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(SynapseParser.T__10)
            self.state = 91
            self.match(SynapseParser.ID)
            self.state = 92
            self.match(SynapseParser.T__11)
            self.state = 93
            self.expr(0)
            self.state = 94
            self.match(SynapseParser.T__5)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                self.state = 95
                self.statement()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(SynapseParser.T__6)
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
        self.enterRule(localctx, 16, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(SynapseParser.T__12)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(SynapseParser.T__5)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                self.state = 106
                self.statement()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(SynapseParser.T__6)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 113
                self.match(SynapseParser.T__13)
                self.state = 114
                self.match(SynapseParser.T__5)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                    self.state = 115
                    self.statement()
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                self.match(SynapseParser.T__6)


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
        self.enterRule(localctx, 18, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SynapseParser.T__14)
            self.state = 125
            self.match(SynapseParser.ID)
            self.state = 126
            self.match(SynapseParser.T__5)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 127
                self.rule_()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 133
            self.match(SynapseParser.T__6)
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
        self.enterRule(localctx, 20, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(SynapseParser.T__15)
            self.state = 136
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
        self.enterRule(localctx, 22, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
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
        self.enterRule(localctx, 24, self.RULE_distribution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
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
        self.enterRule(localctx, 26, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.expr(0)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 143
                self.match(SynapseParser.T__7)
                self.state = 144
                self.expr(0)
                self.state = 149
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
        self.enterRule(localctx, 28, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(SynapseParser.T__12)
            self.state = 151
            self.expr(0)
            self.state = 152
            self.match(SynapseParser.T__5)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 257701292572) != 0):
                self.state = 153
                self.statement()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(SynapseParser.T__6)
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(SynapseParser.ID)
                pass

            elif la_ == 2:
                self.state = 163
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 164
                self.match(SynapseParser.T__19)
                self.state = 165
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 166
                self.match(SynapseParser.STRING)
                pass

            elif la_ == 5:
                self.state = 167
                self.match(SynapseParser.T__20)
                self.state = 168
                self.exprList()
                self.state = 169
                self.match(SynapseParser.T__21)
                pass

            elif la_ == 6:
                self.state = 171
                self.match(SynapseParser.ID)
                self.state = 172
                self.match(SynapseParser.T__3)
                self.state = 173
                self.exprList()
                self.state = 174
                self.match(SynapseParser.T__4)
                pass

            elif la_ == 7:
                self.state = 176
                self.match(SynapseParser.T__3)
                self.state = 177
                self.expr(0)
                self.state = 178
                self.match(SynapseParser.T__4)
                pass

            elif la_ == 8:
                self.state = 180
                self.match(SynapseParser.T__33)
                self.state = 181
                self.match(SynapseParser.T__3)
                self.state = 182
                self.expr(0)
                self.state = 183
                self.match(SynapseParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 187
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 188
                        self.match(SynapseParser.T__22)
                        self.state = 189
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 191
                        self.match(SynapseParser.T__19)
                        self.state = 192
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 194
                        self.match(SynapseParser.T__23)
                        self.state = 195
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 196
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 197
                        self.match(SynapseParser.T__24)
                        self.state = 198
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 200
                        self.match(SynapseParser.T__25)
                        self.state = 201
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 203
                        self.match(SynapseParser.T__26)
                        self.state = 204
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 206
                        self.match(SynapseParser.T__27)
                        self.state = 207
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 209
                        self.match(SynapseParser.T__28)
                        self.state = 210
                        self.expr(8)
                        pass

                    elif la_ == 9:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 211
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 212
                        self.match(SynapseParser.T__29)
                        self.state = 213
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 215
                        self.match(SynapseParser.T__30)
                        self.state = 216
                        self.expr(6)
                        pass

                    elif la_ == 11:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 218
                        self.match(SynapseParser.T__31)
                        self.state = 219
                        self.expr(5)
                        pass

                    elif la_ == 12:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 220
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 221
                        self.match(SynapseParser.T__32)
                        self.state = 222
                        self.expr(4)
                        pass

                    elif la_ == 13:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 224
                        self.match(SynapseParser.T__20)
                        self.state = 225
                        self.expr(0)
                        self.state = 226
                        self.match(SynapseParser.T__21)
                        pass

             
                self.state = 232
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
        self._predicates[15] = self.expr_sempred
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
         




