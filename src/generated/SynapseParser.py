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
        4,1,43,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,5,0,36,8,0,10,0,12,0,39,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,3,1,
        56,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,5,3,70,
        8,3,10,3,12,3,73,9,3,1,3,1,3,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,
        9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,92,8,4,10,4,12,4,95,9,4,1,4,
        1,4,1,5,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,1,6,1,6,1,6,1,6,3,
        6,111,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,126,8,8,10,8,12,8,129,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,137,8,9,
        10,9,12,9,140,9,9,1,9,1,9,1,9,1,9,5,9,146,8,9,10,9,12,9,149,9,9,
        1,9,3,9,152,8,9,1,10,1,10,1,10,1,10,5,10,158,8,10,10,10,12,10,161,
        9,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,
        5,14,175,8,14,10,14,12,14,178,9,14,1,15,1,15,1,15,1,15,5,15,184,
        8,15,10,15,12,15,187,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,215,8,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,258,8,16,
        10,16,12,16,261,9,16,1,16,0,1,32,17,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,0,1,1,0,20,22,289,0,37,1,0,0,0,2,52,1,0,0,0,4,
        57,1,0,0,0,6,60,1,0,0,0,8,76,1,0,0,0,10,98,1,0,0,0,12,106,1,0,0,
        0,14,115,1,0,0,0,16,119,1,0,0,0,18,132,1,0,0,0,20,153,1,0,0,0,22,
        164,1,0,0,0,24,167,1,0,0,0,26,169,1,0,0,0,28,171,1,0,0,0,30,179,
        1,0,0,0,32,214,1,0,0,0,34,36,3,2,1,0,35,34,1,0,0,0,36,39,1,0,0,0,
        37,35,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,
        0,0,1,41,1,1,0,0,0,42,53,3,4,2,0,43,53,3,6,3,0,44,53,3,8,4,0,45,
        53,3,12,6,0,46,53,3,14,7,0,47,53,3,16,8,0,48,53,3,18,9,0,49,53,3,
        20,10,0,50,53,3,22,11,0,51,53,3,24,12,0,52,42,1,0,0,0,52,43,1,0,
        0,0,52,44,1,0,0,0,52,45,1,0,0,0,52,46,1,0,0,0,52,47,1,0,0,0,52,48,
        1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,0,52,51,1,0,0,0,53,55,1,0,0,0,
        54,56,5,1,0,0,55,54,1,0,0,0,55,56,1,0,0,0,56,3,1,0,0,0,57,58,5,2,
        0,0,58,59,5,41,0,0,59,5,1,0,0,0,60,61,5,3,0,0,61,62,5,39,0,0,62,
        64,5,4,0,0,63,65,3,10,5,0,64,63,1,0,0,0,64,65,1,0,0,0,65,66,1,0,
        0,0,66,67,5,5,0,0,67,71,5,6,0,0,68,70,3,2,1,0,69,68,1,0,0,0,70,73,
        1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,
        74,75,5,7,0,0,75,7,1,0,0,0,76,77,5,8,0,0,77,81,5,6,0,0,78,80,3,2,
        1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,
        1,0,0,0,83,81,1,0,0,0,84,85,5,7,0,0,85,86,5,9,0,0,86,87,5,4,0,0,
        87,88,5,39,0,0,88,89,5,5,0,0,89,93,5,6,0,0,90,92,3,2,1,0,91,90,1,
        0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,
        93,1,0,0,0,96,97,5,7,0,0,97,9,1,0,0,0,98,103,5,39,0,0,99,100,5,10,
        0,0,100,102,5,39,0,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,103,1,0,0,0,106,107,5,11,
        0,0,107,110,5,39,0,0,108,109,5,12,0,0,109,111,5,38,0,0,110,108,1,
        0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,13,0,0,113,114,3,
        32,16,0,114,13,1,0,0,0,115,116,5,39,0,0,116,117,5,13,0,0,117,118,
        3,32,16,0,118,15,1,0,0,0,119,120,5,14,0,0,120,121,5,39,0,0,121,122,
        5,15,0,0,122,123,3,32,16,0,123,127,5,6,0,0,124,126,3,2,1,0,125,124,
        1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,
        1,0,0,0,129,127,1,0,0,0,130,131,5,7,0,0,131,17,1,0,0,0,132,133,5,
        16,0,0,133,134,3,32,16,0,134,138,5,6,0,0,135,137,3,2,1,0,136,135,
        1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,141,
        1,0,0,0,140,138,1,0,0,0,141,151,5,7,0,0,142,143,5,17,0,0,143,147,
        5,6,0,0,144,146,3,2,1,0,145,144,1,0,0,0,146,149,1,0,0,0,147,145,
        1,0,0,0,147,148,1,0,0,0,148,150,1,0,0,0,149,147,1,0,0,0,150,152,
        5,7,0,0,151,142,1,0,0,0,151,152,1,0,0,0,152,19,1,0,0,0,153,154,5,
        18,0,0,154,155,5,39,0,0,155,159,5,6,0,0,156,158,3,30,15,0,157,156,
        1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,162,
        1,0,0,0,161,159,1,0,0,0,162,163,5,7,0,0,163,21,1,0,0,0,164,165,5,
        19,0,0,165,166,3,32,16,0,166,23,1,0,0,0,167,168,3,32,16,0,168,25,
        1,0,0,0,169,170,7,0,0,0,170,27,1,0,0,0,171,176,3,32,16,0,172,173,
        5,10,0,0,173,175,3,32,16,0,174,172,1,0,0,0,175,178,1,0,0,0,176,174,
        1,0,0,0,176,177,1,0,0,0,177,29,1,0,0,0,178,176,1,0,0,0,179,180,5,
        16,0,0,180,181,3,32,16,0,181,185,5,6,0,0,182,184,3,2,1,0,183,182,
        1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,188,
        1,0,0,0,187,185,1,0,0,0,188,189,5,7,0,0,189,31,1,0,0,0,190,191,6,
        16,-1,0,191,215,5,39,0,0,192,215,5,40,0,0,193,194,5,23,0,0,194,215,
        5,40,0,0,195,215,5,41,0,0,196,197,5,24,0,0,197,198,3,28,14,0,198,
        199,5,25,0,0,199,215,1,0,0,0,200,201,5,39,0,0,201,202,5,4,0,0,202,
        203,3,28,14,0,203,204,5,5,0,0,204,215,1,0,0,0,205,206,5,4,0,0,206,
        207,3,32,16,0,207,208,5,5,0,0,208,215,1,0,0,0,209,210,5,37,0,0,210,
        211,5,4,0,0,211,212,3,32,16,0,212,213,5,5,0,0,213,215,1,0,0,0,214,
        190,1,0,0,0,214,192,1,0,0,0,214,193,1,0,0,0,214,195,1,0,0,0,214,
        196,1,0,0,0,214,200,1,0,0,0,214,205,1,0,0,0,214,209,1,0,0,0,215,
        259,1,0,0,0,216,217,10,14,0,0,217,218,5,26,0,0,218,258,3,32,16,15,
        219,220,10,13,0,0,220,221,5,23,0,0,221,258,3,32,16,14,222,223,10,
        12,0,0,223,224,5,27,0,0,224,258,3,32,16,13,225,226,10,11,0,0,226,
        227,5,28,0,0,227,258,3,32,16,12,228,229,10,10,0,0,229,230,5,29,0,
        0,230,258,3,32,16,11,231,232,10,9,0,0,232,233,5,30,0,0,233,258,3,
        32,16,10,234,235,10,8,0,0,235,236,5,31,0,0,236,258,3,32,16,9,237,
        238,10,7,0,0,238,239,5,32,0,0,239,258,3,32,16,8,240,241,10,6,0,0,
        241,242,5,33,0,0,242,258,3,32,16,7,243,244,10,5,0,0,244,245,5,34,
        0,0,245,258,3,32,16,6,246,247,10,4,0,0,247,248,5,35,0,0,248,258,
        3,32,16,5,249,250,10,3,0,0,250,251,5,36,0,0,251,258,3,32,16,4,252,
        253,10,15,0,0,253,254,5,24,0,0,254,255,3,32,16,0,255,256,5,25,0,
        0,256,258,1,0,0,0,257,216,1,0,0,0,257,219,1,0,0,0,257,222,1,0,0,
        0,257,225,1,0,0,0,257,228,1,0,0,0,257,231,1,0,0,0,257,234,1,0,0,
        0,257,237,1,0,0,0,257,240,1,0,0,0,257,243,1,0,0,0,257,246,1,0,0,
        0,257,249,1,0,0,0,257,252,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,
        0,259,260,1,0,0,0,260,33,1,0,0,0,261,259,1,0,0,0,19,37,52,55,64,
        71,81,93,103,110,127,138,147,151,159,176,185,214,257,259
    ]

class SynapseParser ( Parser ):

    grammarFileName = "Synapse.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'import'", "'def'", "'('", "')'", 
                     "'{'", "'}'", "'try'", "'catch'", "','", "'let'", "':'", 
                     "'='", "'for'", "'in'", "'if'", "'else'", "'morph'", 
                     "'goal:'", "'normal'", "'bernoulli'", "'uniform'", 
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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TYPE", "ID", "NUMBER", 
                      "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_importStatement = 2
    RULE_funcStatement = 3
    RULE_tryStatement = 4
    RULE_paramList = 5
    RULE_letStatement = 6
    RULE_assignStatement = 7
    RULE_forStatement = 8
    RULE_ifStatement = 9
    RULE_morphStatement = 10
    RULE_goalStatement = 11
    RULE_exprStatement = 12
    RULE_distribution = 13
    RULE_exprList = 14
    RULE_rule = 15
    RULE_expr = 16

    ruleNames =  [ "program", "statement", "importStatement", "funcStatement", 
                   "tryStatement", "paramList", "letStatement", "assignStatement", 
                   "forStatement", "ifStatement", "morphStatement", "goalStatement", 
                   "exprStatement", "distribution", "exprList", "rule", 
                   "expr" ]

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
    T__34=35
    T__35=36
    T__36=37
    TYPE=38
    ID=39
    NUMBER=40
    STRING=41
    COMMENT=42
    WS=43

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
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 34
                self.statement()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
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


        def tryStatement(self):
            return self.getTypedRuleContext(SynapseParser.TryStatementContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 42
                self.importStatement()
                pass

            elif la_ == 2:
                self.state = 43
                self.funcStatement()
                pass

            elif la_ == 3:
                self.state = 44
                self.tryStatement()
                pass

            elif la_ == 4:
                self.state = 45
                self.letStatement()
                pass

            elif la_ == 5:
                self.state = 46
                self.assignStatement()
                pass

            elif la_ == 6:
                self.state = 47
                self.forStatement()
                pass

            elif la_ == 7:
                self.state = 48
                self.ifStatement()
                pass

            elif la_ == 8:
                self.state = 49
                self.morphStatement()
                pass

            elif la_ == 9:
                self.state = 50
                self.goalStatement()
                pass

            elif la_ == 10:
                self.state = 51
                self.exprStatement()
                pass


            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 54
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
            self.state = 57
            self.match(SynapseParser.T__1)
            self.state = 58
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
            self.state = 60
            self.match(SynapseParser.T__2)
            self.state = 61
            self.match(SynapseParser.ID)
            self.state = 62
            self.match(SynapseParser.T__3)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 63
                self.paramList()


            self.state = 66
            self.match(SynapseParser.T__4)
            self.state = 67
            self.match(SynapseParser.T__5)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 68
                self.statement()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(SynapseParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SynapseParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SynapseParser.StatementContext)
            else:
                return self.getTypedRuleContext(SynapseParser.StatementContext,i)


        def getRuleIndex(self):
            return SynapseParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = SynapseParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(SynapseParser.T__7)
            self.state = 77
            self.match(SynapseParser.T__5)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(SynapseParser.T__6)
            self.state = 85
            self.match(SynapseParser.T__8)
            self.state = 86
            self.match(SynapseParser.T__3)
            self.state = 87
            self.match(SynapseParser.ID)
            self.state = 88
            self.match(SynapseParser.T__4)
            self.state = 89
            self.match(SynapseParser.T__5)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 90
                self.statement()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
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
        self.enterRule(localctx, 10, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(SynapseParser.ID)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 99
                self.match(SynapseParser.T__9)
                self.state = 100
                self.match(SynapseParser.ID)
                self.state = 105
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


        def TYPE(self):
            return self.getToken(SynapseParser.TYPE, 0)

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
        self.enterRule(localctx, 12, self.RULE_letStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SynapseParser.T__10)
            self.state = 107
            self.match(SynapseParser.ID)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 108
                self.match(SynapseParser.T__11)
                self.state = 109
                self.match(SynapseParser.TYPE)


            self.state = 112
            self.match(SynapseParser.T__12)
            self.state = 113
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
        self.enterRule(localctx, 14, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(SynapseParser.ID)
            self.state = 116
            self.match(SynapseParser.T__12)
            self.state = 117
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
        self.enterRule(localctx, 16, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SynapseParser.T__13)
            self.state = 120
            self.match(SynapseParser.ID)
            self.state = 121
            self.match(SynapseParser.T__14)
            self.state = 122
            self.expr(0)
            self.state = 123
            self.match(SynapseParser.T__5)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 124
                self.statement()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
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
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(SynapseParser.T__15)
            self.state = 133
            self.expr(0)
            self.state = 134
            self.match(SynapseParser.T__5)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 135
                self.statement()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(SynapseParser.T__6)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 142
                self.match(SynapseParser.T__16)
                self.state = 143
                self.match(SynapseParser.T__5)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                    self.state = 144
                    self.statement()
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
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
        self.enterRule(localctx, 20, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(SynapseParser.T__17)
            self.state = 154
            self.match(SynapseParser.ID)
            self.state = 155
            self.match(SynapseParser.T__5)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 156
                self.rule_()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
        self.enterRule(localctx, 22, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(SynapseParser.T__18)
            self.state = 165
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
        self.enterRule(localctx, 24, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 26, self.RULE_distribution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
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
        self.enterRule(localctx, 28, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr(0)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 172
                self.match(SynapseParser.T__9)
                self.state = 173
                self.expr(0)
                self.state = 178
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
        self.enterRule(localctx, 30, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(SynapseParser.T__15)
            self.state = 180
            self.expr(0)
            self.state = 181
            self.match(SynapseParser.T__5)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3985755687196) != 0):
                self.state = 182
                self.statement()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(SynapseParser.ID)
                pass

            elif la_ == 2:
                self.state = 192
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 193
                self.match(SynapseParser.T__22)
                self.state = 194
                self.match(SynapseParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 195
                self.match(SynapseParser.STRING)
                pass

            elif la_ == 5:
                self.state = 196
                self.match(SynapseParser.T__23)
                self.state = 197
                self.exprList()
                self.state = 198
                self.match(SynapseParser.T__24)
                pass

            elif la_ == 6:
                self.state = 200
                self.match(SynapseParser.ID)
                self.state = 201
                self.match(SynapseParser.T__3)
                self.state = 202
                self.exprList()
                self.state = 203
                self.match(SynapseParser.T__4)
                pass

            elif la_ == 7:
                self.state = 205
                self.match(SynapseParser.T__3)
                self.state = 206
                self.expr(0)
                self.state = 207
                self.match(SynapseParser.T__4)
                pass

            elif la_ == 8:
                self.state = 209
                self.match(SynapseParser.T__36)
                self.state = 210
                self.match(SynapseParser.T__3)
                self.state = 211
                self.expr(0)
                self.state = 212
                self.match(SynapseParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 216
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 217
                        self.match(SynapseParser.T__25)
                        self.state = 218
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 219
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 220
                        self.match(SynapseParser.T__22)
                        self.state = 221
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 222
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 223
                        self.match(SynapseParser.T__26)
                        self.state = 224
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 225
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 226
                        self.match(SynapseParser.T__27)
                        self.state = 227
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 228
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 229
                        self.match(SynapseParser.T__28)
                        self.state = 230
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 232
                        self.match(SynapseParser.T__29)
                        self.state = 233
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 234
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 235
                        self.match(SynapseParser.T__30)
                        self.state = 236
                        self.expr(9)
                        pass

                    elif la_ == 8:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 237
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 238
                        self.match(SynapseParser.T__31)
                        self.state = 239
                        self.expr(8)
                        pass

                    elif la_ == 9:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 240
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 241
                        self.match(SynapseParser.T__32)
                        self.state = 242
                        self.expr(7)
                        pass

                    elif la_ == 10:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 243
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 244
                        self.match(SynapseParser.T__33)
                        self.state = 245
                        self.expr(6)
                        pass

                    elif la_ == 11:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 246
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 247
                        self.match(SynapseParser.T__34)
                        self.state = 248
                        self.expr(5)
                        pass

                    elif la_ == 12:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 249
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 250
                        self.match(SynapseParser.T__35)
                        self.state = 251
                        self.expr(4)
                        pass

                    elif la_ == 13:
                        localctx = SynapseParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 252
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 253
                        self.match(SynapseParser.T__23)
                        self.state = 254
                        self.expr(0)
                        self.state = 255
                        self.match(SynapseParser.T__24)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self._predicates[16] = self.expr_sempred
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
         




