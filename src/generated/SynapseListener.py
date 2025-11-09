# Generated from grammar/Synapse.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SynapseParser import SynapseParser
else:
    from SynapseParser import SynapseParser

# This class defines a complete listener for a parse tree produced by SynapseParser.
class SynapseListener(ParseTreeListener):

    # Enter a parse tree produced by SynapseParser#program.
    def enterProgram(self, ctx:SynapseParser.ProgramContext):
        pass

    # Exit a parse tree produced by SynapseParser#program.
    def exitProgram(self, ctx:SynapseParser.ProgramContext):
        pass


    # Enter a parse tree produced by SynapseParser#statement.
    def enterStatement(self, ctx:SynapseParser.StatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#statement.
    def exitStatement(self, ctx:SynapseParser.StatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#letStatement.
    def enterLetStatement(self, ctx:SynapseParser.LetStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#letStatement.
    def exitLetStatement(self, ctx:SynapseParser.LetStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#ifStatement.
    def enterIfStatement(self, ctx:SynapseParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#ifStatement.
    def exitIfStatement(self, ctx:SynapseParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#morphStatement.
    def enterMorphStatement(self, ctx:SynapseParser.MorphStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#morphStatement.
    def exitMorphStatement(self, ctx:SynapseParser.MorphStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#goalStatement.
    def enterGoalStatement(self, ctx:SynapseParser.GoalStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#goalStatement.
    def exitGoalStatement(self, ctx:SynapseParser.GoalStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#exprStatement.
    def enterExprStatement(self, ctx:SynapseParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#exprStatement.
    def exitExprStatement(self, ctx:SynapseParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#distribution.
    def enterDistribution(self, ctx:SynapseParser.DistributionContext):
        pass

    # Exit a parse tree produced by SynapseParser#distribution.
    def exitDistribution(self, ctx:SynapseParser.DistributionContext):
        pass


    # Enter a parse tree produced by SynapseParser#exprList.
    def enterExprList(self, ctx:SynapseParser.ExprListContext):
        pass

    # Exit a parse tree produced by SynapseParser#exprList.
    def exitExprList(self, ctx:SynapseParser.ExprListContext):
        pass


    # Enter a parse tree produced by SynapseParser#rule.
    def enterRule(self, ctx:SynapseParser.RuleContext):
        pass

    # Exit a parse tree produced by SynapseParser#rule.
    def exitRule(self, ctx:SynapseParser.RuleContext):
        pass


    # Enter a parse tree produced by SynapseParser#expr.
    def enterExpr(self, ctx:SynapseParser.ExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#expr.
    def exitExpr(self, ctx:SynapseParser.ExprContext):
        pass



del SynapseParser