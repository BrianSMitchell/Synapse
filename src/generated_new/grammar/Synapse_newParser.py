# Generated from grammar/Synapse_new.g4 by ANTLR 4.13.2
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
        4,1,45,293,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,1,
        3,1,70,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,1,3,5,
        3,84,8,3,10,3,12,3,87,9,3,1,3,1,3,1,4,1,4,1,4,5,4,94,8,4,10,4,12,
        4,97,9,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,106,8,4,10,4,12,4,109,9,
        4,1,4,1,4,1,5,1,5,1,5,5,5,116,8,5,10,5,12,5,119,9,5,1,6,1,6,1,6,
        1,6,3,6,125,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,
        1,8,5,8,140,8,8,10,8,12,8,143,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,151,
        8,9,10,9,12,9,154,9,9,1,9,1,9,1,9,1,9,5,9,160,8,9,10,9,12,9,163,
        9,9,1,9,3,9,166,8,9,1,10,1,10,1,10,1,10,5,10,172,8,10,10,10,12,10,
        175,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,
        1,13,5,13,189,8,13,10,13,12,13,192,9,13,1,13,1,13,1,14,1,14,1,15,
        1,15,1,15,5,15,201,8,15,10,15,12,15,204,9,15,1,16,1,16,1,16,5,16,
        209,8,16,10,16,12,16,212,9,16,1,17,1,17,1,17,5,17,217,8,17,10,17,
        12,17,220,9,17,1,18,1,18,1,18,5,18,225,8,18,10,18,12,18,228,9,18,
        1,19,1,19,1,19,5,19,233,8,19,10,19,12,19,236,9,19,1,20,1,20,1,20,
        5,20,241,8,20,10,20,12,20,244,9,20,1,21,3,21,247,8,21,1,21,1,21,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,273,8,22,1,22,
        1,22,1,22,1,22,1,22,5,22,280,8,22,10,22,12,22,283,9,22,1,23,1,23,
        1,23,5,23,288,8,23,10,23,12,23,291,9,23,1,23,0,1,44,24,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,
        31,32,1,0,33,36,1,0,37,38,1,0,39,40,2,0,38,38,41,41,306,0,51,1,0,
        0,0,2,66,1,0,0,0,4,71,1,0,0,0,6,74,1,0,0,0,8,90,1,0,0,0,10,112,1,
        0,0,0,12,120,1,0,0,0,14,129,1,0,0,0,16,133,1,0,0,0,18,146,1,0,0,
        0,20,167,1,0,0,0,22,178,1,0,0,0,24,182,1,0,0,0,26,184,1,0,0,0,28,
        195,1,0,0,0,30,197,1,0,0,0,32,205,1,0,0,0,34,213,1,0,0,0,36,221,
        1,0,0,0,38,229,1,0,0,0,40,237,1,0,0,0,42,246,1,0,0,0,44,272,1,0,
        0,0,46,284,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,
        49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,
        1,55,1,1,0,0,0,56,67,3,4,2,0,57,67,3,6,3,0,58,67,3,8,4,0,59,67,3,
        12,6,0,60,67,3,14,7,0,61,67,3,16,8,0,62,67,3,18,9,0,63,67,3,20,10,
        0,64,67,3,22,11,0,65,67,3,24,12,0,66,56,1,0,0,0,66,57,1,0,0,0,66,
        58,1,0,0,0,66,59,1,0,0,0,66,60,1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,
        0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,69,1,0,0,0,68,70,
        5,1,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,3,1,0,0,0,71,72,5,11,0,0,
        72,73,5,42,0,0,73,5,1,0,0,0,74,75,5,12,0,0,75,76,5,42,0,0,76,78,
        5,2,0,0,77,79,3,10,5,0,78,77,1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,
        80,81,5,3,0,0,81,85,5,4,0,0,82,84,3,2,1,0,83,82,1,0,0,0,84,87,1,
        0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,
        89,5,5,0,0,89,7,1,0,0,0,90,91,5,13,0,0,91,95,5,4,0,0,92,94,3,2,1,
        0,93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,
        1,0,0,0,97,95,1,0,0,0,98,99,5,5,0,0,99,100,5,14,0,0,100,101,5,2,
        0,0,101,102,5,42,0,0,102,103,5,3,0,0,103,107,5,4,0,0,104,106,3,2,
        1,0,105,104,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,
        0,0,108,110,1,0,0,0,109,107,1,0,0,0,110,111,5,5,0,0,111,9,1,0,0,
        0,112,117,5,42,0,0,113,114,5,6,0,0,114,116,5,42,0,0,115,113,1,0,
        0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,11,1,0,0,
        0,119,117,1,0,0,0,120,121,5,15,0,0,121,124,5,42,0,0,122,123,5,7,
        0,0,123,125,5,28,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,126,1,0,
        0,0,126,127,5,8,0,0,127,128,3,28,14,0,128,13,1,0,0,0,129,130,3,28,
        14,0,130,131,5,8,0,0,131,132,3,28,14,0,132,15,1,0,0,0,133,134,5,
        16,0,0,134,135,5,42,0,0,135,136,5,17,0,0,136,137,3,28,14,0,137,141,
        5,4,0,0,138,140,3,2,1,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,
        5,5,0,0,145,17,1,0,0,0,146,147,5,18,0,0,147,148,3,28,14,0,148,152,
        5,4,0,0,149,151,3,2,1,0,150,149,1,0,0,0,151,154,1,0,0,0,152,150,
        1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,165,
        5,5,0,0,156,157,5,19,0,0,157,161,5,4,0,0,158,160,3,2,1,0,159,158,
        1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,164,
        1,0,0,0,163,161,1,0,0,0,164,166,5,5,0,0,165,156,1,0,0,0,165,166,
        1,0,0,0,166,19,1,0,0,0,167,168,5,20,0,0,168,169,5,42,0,0,169,173,
        5,4,0,0,170,172,3,26,13,0,171,170,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,176,1,0,0,0,175,173,1,0,0,0,176,177,
        5,5,0,0,177,21,1,0,0,0,178,179,5,21,0,0,179,180,5,7,0,0,180,181,
        3,28,14,0,181,23,1,0,0,0,182,183,3,28,14,0,183,25,1,0,0,0,184,185,
        5,18,0,0,185,186,3,28,14,0,186,190,5,4,0,0,187,189,3,2,1,0,188,187,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,190,1,0,0,0,193,194,5,5,0,0,194,27,1,0,0,0,195,196,3,
        30,15,0,196,29,1,0,0,0,197,202,3,32,16,0,198,199,5,29,0,0,199,201,
        3,32,16,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,
        1,0,0,0,203,31,1,0,0,0,204,202,1,0,0,0,205,210,3,34,17,0,206,207,
        5,30,0,0,207,209,3,34,17,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,
        1,0,0,0,210,211,1,0,0,0,211,33,1,0,0,0,212,210,1,0,0,0,213,218,3,
        36,18,0,214,215,7,0,0,0,215,217,3,36,18,0,216,214,1,0,0,0,217,220,
        1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,35,1,0,0,0,220,218,1,
        0,0,0,221,226,3,38,19,0,222,223,7,1,0,0,223,225,3,38,19,0,224,222,
        1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,37,1,
        0,0,0,228,226,1,0,0,0,229,234,3,40,20,0,230,231,7,2,0,0,231,233,
        3,40,20,0,232,230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,234,235,
        1,0,0,0,235,39,1,0,0,0,236,234,1,0,0,0,237,242,3,42,21,0,238,239,
        7,3,0,0,239,241,3,42,21,0,240,238,1,0,0,0,241,244,1,0,0,0,242,240,
        1,0,0,0,242,243,1,0,0,0,243,41,1,0,0,0,244,242,1,0,0,0,245,247,7,
        4,0,0,246,245,1,0,0,0,246,247,1,0,0,0,247,248,1,0,0,0,248,249,3,
        44,22,0,249,43,1,0,0,0,250,251,6,22,-1,0,251,252,5,42,0,0,252,253,
        5,2,0,0,253,254,3,46,23,0,254,255,5,3,0,0,255,273,1,0,0,0,256,257,
        5,22,0,0,257,258,5,2,0,0,258,259,3,28,14,0,259,260,5,3,0,0,260,273,
        1,0,0,0,261,273,5,42,0,0,262,273,5,43,0,0,263,273,5,44,0,0,264,265,
        5,9,0,0,265,266,3,46,23,0,266,267,5,10,0,0,267,273,1,0,0,0,268,269,
        5,2,0,0,269,270,3,28,14,0,270,271,5,3,0,0,271,273,1,0,0,0,272,250,
        1,0,0,0,272,256,1,0,0,0,272,261,1,0,0,0,272,262,1,0,0,0,272,263,
        1,0,0,0,272,264,1,0,0,0,272,268,1,0,0,0,273,281,1,0,0,0,274,275,
        10,2,0,0,275,276,5,9,0,0,276,277,3,28,14,0,277,278,5,10,0,0,278,
        280,1,0,0,0,279,274,1,0,0,0,280,283,1,0,0,0,281,279,1,0,0,0,281,
        282,1,0,0,0,282,45,1,0,0,0,283,281,1,0,0,0,284,289,3,28,14,0,285,
        286,5,6,0,0,286,288,3,28,14,0,287,285,1,0,0,0,288,291,1,0,0,0,289,
        287,1,0,0,0,289,290,1,0,0,0,290,47,1,0,0,0,291,289,1,0,0,0,25,51,
        66,69,78,85,95,107,117,124,141,152,161,165,173,190,202,210,218,226,
        234,242,246,272,281,289
    ]

class Synapse_newParser ( Parser ):

    grammarFileName = "Synapse_new.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "'{'", "'}'", "','", 
                     "':'", "'='", "'['", "']'", "'import'", "'def'", "'try'", 
                     "'catch'", "'let'", "'for'", "'in'", "'if'", "'else'", 
                     "'morph'", "'goal'", "'sample'", "'int'", "'float'", 
                     "'list'", "'string'", "'await'", "<INVALID>", "'or'", 
                     "'and'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'+'", "'-'", "'*'", "'/'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IMPORT", "DEF", 
                      "TRY", "CATCH", "LET", "FOR", "IN", "IF", "ELSE", 
                      "MORPH", "GOAL", "SAMPLE", "INT", "FLOAT", "LIST", 
                      "STRING_TYPE", "AWAIT", "TYPE", "OR", "AND", "EQUAL", 
                      "NOT_EQUAL", "GREATER", "LESS", "GREATER_EQUAL", "LESS_EQUAL", 
                      "PLUS", "MINUS", "MULT", "DIV", "NOT", "ID", "NUMBER", 
                      "STRING", "WS" ]

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
    RULE_rule = 13
    RULE_expr = 14
    RULE_orExpr = 15
    RULE_andExpr = 16
    RULE_eqExpr = 17
    RULE_relExpr = 18
    RULE_addExpr = 19
    RULE_mulExpr = 20
    RULE_unaryExpr = 21
    RULE_primary = 22
    RULE_exprList = 23

    ruleNames =  [ "program", "statement", "importStatement", "funcStatement", 
                   "tryStatement", "paramList", "letStatement", "assignStatement", 
                   "forStatement", "ifStatement", "morphStatement", "goalStatement", 
                   "exprStatement", "rule", "expr", "orExpr", "andExpr", 
                   "eqExpr", "relExpr", "addExpr", "mulExpr", "unaryExpr", 
                   "primary", "exprList" ]

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
    IMPORT=11
    DEF=12
    TRY=13
    CATCH=14
    LET=15
    FOR=16
    IN=17
    IF=18
    ELSE=19
    MORPH=20
    GOAL=21
    SAMPLE=22
    INT=23
    FLOAT=24
    LIST=25
    STRING_TYPE=26
    AWAIT=27
    TYPE=28
    OR=29
    AND=30
    EQUAL=31
    NOT_EQUAL=32
    GREATER=33
    LESS=34
    GREATER_EQUAL=35
    LESS_EQUAL=36
    PLUS=37
    MINUS=38
    MULT=39
    DIV=40
    NOT=41
    ID=42
    NUMBER=43
    STRING=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Synapse_newParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = Synapse_newParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(Synapse_newParser.EOF)
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
            return self.getTypedRuleContext(Synapse_newParser.ImportStatementContext,0)


        def funcStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.FuncStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.TryStatementContext,0)


        def letStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.LetStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.AssignStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.ForStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.IfStatementContext,0)


        def morphStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.MorphStatementContext,0)


        def goalStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.GoalStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprStatementContext,0)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = Synapse_newParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 56
                self.importStatement()
                pass

            elif la_ == 2:
                self.state = 57
                self.funcStatement()
                pass

            elif la_ == 3:
                self.state = 58
                self.tryStatement()
                pass

            elif la_ == 4:
                self.state = 59
                self.letStatement()
                pass

            elif la_ == 5:
                self.state = 60
                self.assignStatement()
                pass

            elif la_ == 6:
                self.state = 61
                self.forStatement()
                pass

            elif la_ == 7:
                self.state = 62
                self.ifStatement()
                pass

            elif la_ == 8:
                self.state = 63
                self.morphStatement()
                pass

            elif la_ == 9:
                self.state = 64
                self.goalStatement()
                pass

            elif la_ == 10:
                self.state = 65
                self.exprStatement()
                pass


            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 68
                self.match(Synapse_newParser.T__0)


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

        def IMPORT(self):
            return self.getToken(Synapse_newParser.IMPORT, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_importStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStatement" ):
                return visitor.visitImportStatement(self)
            else:
                return visitor.visitChildren(self)




    def importStatement(self):

        localctx = Synapse_newParser.ImportStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(Synapse_newParser.IMPORT)
            self.state = 72
            self.match(Synapse_newParser.ID)
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

        def DEF(self):
            return self.getToken(Synapse_newParser.DEF, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(Synapse_newParser.ParamListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_funcStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncStatement" ):
                return visitor.visitFuncStatement(self)
            else:
                return visitor.visitChildren(self)




    def funcStatement(self):

        localctx = Synapse_newParser.FuncStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(Synapse_newParser.DEF)
            self.state = 75
            self.match(Synapse_newParser.ID)
            self.state = 76
            self.match(Synapse_newParser.T__1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 77
                self.paramList()


            self.state = 80
            self.match(Synapse_newParser.T__2)
            self.state = 81
            self.match(Synapse_newParser.T__3)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 82
                self.statement()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(Synapse_newParser.T__4)
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

        def TRY(self):
            return self.getToken(Synapse_newParser.TRY, 0)

        def CATCH(self):
            return self.getToken(Synapse_newParser.CATCH, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_tryStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryStatement" ):
                return visitor.visitTryStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryStatement(self):

        localctx = Synapse_newParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(Synapse_newParser.TRY)
            self.state = 91
            self.match(Synapse_newParser.T__3)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 92
                self.statement()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(Synapse_newParser.T__4)
            self.state = 99
            self.match(Synapse_newParser.CATCH)
            self.state = 100
            self.match(Synapse_newParser.T__1)
            self.state = 101
            self.match(Synapse_newParser.ID)
            self.state = 102
            self.match(Synapse_newParser.T__2)
            self.state = 103
            self.match(Synapse_newParser.T__3)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 104
                self.statement()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self.match(Synapse_newParser.T__4)
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
                return self.getTokens(Synapse_newParser.ID)
            else:
                return self.getToken(Synapse_newParser.ID, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = Synapse_newParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(Synapse_newParser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 113
                self.match(Synapse_newParser.T__5)
                self.state = 114
                self.match(Synapse_newParser.ID)
                self.state = 119
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

        def LET(self):
            return self.getToken(Synapse_newParser.LET, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def TYPE(self):
            return self.getToken(Synapse_newParser.TYPE, 0)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_letStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStatement" ):
                return visitor.visitLetStatement(self)
            else:
                return visitor.visitChildren(self)




    def letStatement(self):

        localctx = Synapse_newParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_letStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(Synapse_newParser.LET)
            self.state = 121
            self.match(Synapse_newParser.ID)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 122
                self.match(Synapse_newParser.T__6)
                self.state = 123
                self.match(Synapse_newParser.TYPE)


            self.state = 126
            self.match(Synapse_newParser.T__7)
            self.state = 127
            self.expr()
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.ExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.ExprContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = Synapse_newParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expr()
            self.state = 130
            self.match(Synapse_newParser.T__7)
            self.state = 131
            self.expr()
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

        def FOR(self):
            return self.getToken(Synapse_newParser.FOR, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def IN(self):
            return self.getToken(Synapse_newParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = Synapse_newParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(Synapse_newParser.FOR)
            self.state = 134
            self.match(Synapse_newParser.ID)
            self.state = 135
            self.match(Synapse_newParser.IN)
            self.state = 136
            self.expr()
            self.state = 137
            self.match(Synapse_newParser.T__3)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 138
                self.statement()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(Synapse_newParser.T__4)
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

        def IF(self):
            return self.getToken(Synapse_newParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(Synapse_newParser.ELSE, 0)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = Synapse_newParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(Synapse_newParser.IF)
            self.state = 147
            self.expr()
            self.state = 148
            self.match(Synapse_newParser.T__3)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 149
                self.statement()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(Synapse_newParser.T__4)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 156
                self.match(Synapse_newParser.ELSE)
                self.state = 157
                self.match(Synapse_newParser.T__3)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                    self.state = 158
                    self.statement()
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 164
                self.match(Synapse_newParser.T__4)


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

        def MORPH(self):
            return self.getToken(Synapse_newParser.MORPH, 0)

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.RuleContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.RuleContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_morphStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMorphStatement" ):
                return visitor.visitMorphStatement(self)
            else:
                return visitor.visitChildren(self)




    def morphStatement(self):

        localctx = Synapse_newParser.MorphStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_morphStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(Synapse_newParser.MORPH)
            self.state = 168
            self.match(Synapse_newParser.ID)
            self.state = 169
            self.match(Synapse_newParser.T__3)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 170
                self.rule_()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            self.match(Synapse_newParser.T__4)
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

        def GOAL(self):
            return self.getToken(Synapse_newParser.GOAL, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_goalStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoalStatement" ):
                return visitor.visitGoalStatement(self)
            else:
                return visitor.visitChildren(self)




    def goalStatement(self):

        localctx = Synapse_newParser.GoalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_goalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(Synapse_newParser.GOAL)
            self.state = 179
            self.match(Synapse_newParser.T__6)
            self.state = 180
            self.expr()
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
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_exprStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)




    def exprStatement(self):

        localctx = Synapse_newParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.expr()
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

        def IF(self):
            return self.getToken(Synapse_newParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.StatementContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.StatementContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_rule

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = Synapse_newParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(Synapse_newParser.IF)
            self.state = 185
            self.expr()
            self.state = 186
            self.match(Synapse_newParser.T__3)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33260234455556) != 0):
                self.state = 187
                self.statement()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
            self.match(Synapse_newParser.T__4)
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

        def orExpr(self):
            return self.getTypedRuleContext(Synapse_newParser.OrExprContext,0)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = Synapse_newParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.AndExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.OR)
            else:
                return self.getToken(Synapse_newParser.OR, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_orExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = Synapse_newParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.andExpr()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 198
                self.match(Synapse_newParser.OR)
                self.state = 199
                self.andExpr()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eqExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.EqExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.EqExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.AND)
            else:
                return self.getToken(Synapse_newParser.AND, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_andExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = Synapse_newParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.eqExpr()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 206
                self.match(Synapse_newParser.AND)
                self.state = 207
                self.eqExpr()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.RelExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.RelExprContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.EQUAL)
            else:
                return self.getToken(Synapse_newParser.EQUAL, i)

        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.NOT_EQUAL)
            else:
                return self.getToken(Synapse_newParser.NOT_EQUAL, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_eqExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqExpr" ):
                return visitor.visitEqExpr(self)
            else:
                return visitor.visitChildren(self)




    def eqExpr(self):

        localctx = Synapse_newParser.EqExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_eqExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.relExpr()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.relExpr()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.AddExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.AddExprContext,i)


        def GREATER(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.GREATER)
            else:
                return self.getToken(Synapse_newParser.GREATER, i)

        def LESS(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.LESS)
            else:
                return self.getToken(Synapse_newParser.LESS, i)

        def GREATER_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.GREATER_EQUAL)
            else:
                return self.getToken(Synapse_newParser.GREATER_EQUAL, i)

        def LESS_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.LESS_EQUAL)
            else:
                return self.getToken(Synapse_newParser.LESS_EQUAL, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_relExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)




    def relExpr(self):

        localctx = Synapse_newParser.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_relExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.addExpr()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0):
                self.state = 222
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.addExpr()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.MulExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.MulExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.PLUS)
            else:
                return self.getToken(Synapse_newParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.MINUS)
            else:
                return self.getToken(Synapse_newParser.MINUS, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_addExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)




    def addExpr(self):

        localctx = Synapse_newParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.mulExpr()
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    _la = self._input.LA(1)
                    if not(_la==37 or _la==38):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.mulExpr() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.UnaryExprContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.MULT)
            else:
                return self.getToken(Synapse_newParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(Synapse_newParser.DIV)
            else:
                return self.getToken(Synapse_newParser.DIV, i)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_mulExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)




    def mulExpr(self):

        localctx = Synapse_newParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.unaryExpr()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39 or _la==40:
                self.state = 238
                _la = self._input.LA(1)
                if not(_la==39 or _la==40):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 239
                self.unaryExpr()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(Synapse_newParser.PrimaryContext,0)


        def MINUS(self):
            return self.getToken(Synapse_newParser.MINUS, 0)

        def NOT(self):
            return self.getToken(Synapse_newParser.NOT, 0)

        def getRuleIndex(self):
            return Synapse_newParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = Synapse_newParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==41:
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==38 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 248
            self.primary(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Synapse_newParser.ID, 0)

        def exprList(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprListContext,0)


        def SAMPLE(self):
            return self.getToken(Synapse_newParser.SAMPLE, 0)

        def expr(self):
            return self.getTypedRuleContext(Synapse_newParser.ExprContext,0)


        def NUMBER(self):
            return self.getToken(Synapse_newParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(Synapse_newParser.STRING, 0)

        def primary(self):
            return self.getTypedRuleContext(Synapse_newParser.PrimaryContext,0)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)



    def primary(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Synapse_newParser.PrimaryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_primary, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 251
                self.match(Synapse_newParser.ID)
                self.state = 252
                self.match(Synapse_newParser.T__1)
                self.state = 253
                self.exprList()
                self.state = 254
                self.match(Synapse_newParser.T__2)
                pass

            elif la_ == 2:
                self.state = 256
                self.match(Synapse_newParser.SAMPLE)
                self.state = 257
                self.match(Synapse_newParser.T__1)
                self.state = 258
                self.expr()
                self.state = 259
                self.match(Synapse_newParser.T__2)
                pass

            elif la_ == 3:
                self.state = 261
                self.match(Synapse_newParser.ID)
                pass

            elif la_ == 4:
                self.state = 262
                self.match(Synapse_newParser.NUMBER)
                pass

            elif la_ == 5:
                self.state = 263
                self.match(Synapse_newParser.STRING)
                pass

            elif la_ == 6:
                self.state = 264
                self.match(Synapse_newParser.T__8)
                self.state = 265
                self.exprList()
                self.state = 266
                self.match(Synapse_newParser.T__9)
                pass

            elif la_ == 7:
                self.state = 268
                self.match(Synapse_newParser.T__1)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(Synapse_newParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = Synapse_newParser.PrimaryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_primary)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    self.match(Synapse_newParser.T__8)
                    self.state = 276
                    self.expr()
                    self.state = 277
                    self.match(Synapse_newParser.T__9) 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Synapse_newParser.ExprContext)
            else:
                return self.getTypedRuleContext(Synapse_newParser.ExprContext,i)


        def getRuleIndex(self):
            return Synapse_newParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = Synapse_newParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 285
                self.match(Synapse_newParser.T__5)
                self.state = 286
                self.expr()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.primary_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def primary_sempred(self, localctx:PrimaryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




