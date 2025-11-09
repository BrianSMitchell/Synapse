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


    # Enter a parse tree produced by SynapseParser#importStatement.
    def enterImportStatement(self, ctx:SynapseParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#importStatement.
    def exitImportStatement(self, ctx:SynapseParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#funcStatement.
    def enterFuncStatement(self, ctx:SynapseParser.FuncStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#funcStatement.
    def exitFuncStatement(self, ctx:SynapseParser.FuncStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#tryStatement.
    def enterTryStatement(self, ctx:SynapseParser.TryStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#tryStatement.
    def exitTryStatement(self, ctx:SynapseParser.TryStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#paramList.
    def enterParamList(self, ctx:SynapseParser.ParamListContext):
        pass

    # Exit a parse tree produced by SynapseParser#paramList.
    def exitParamList(self, ctx:SynapseParser.ParamListContext):
        pass


    # Enter a parse tree produced by SynapseParser#letStatement.
    def enterLetStatement(self, ctx:SynapseParser.LetStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#letStatement.
    def exitLetStatement(self, ctx:SynapseParser.LetStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#assignStatement.
    def enterAssignStatement(self, ctx:SynapseParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#assignStatement.
    def exitAssignStatement(self, ctx:SynapseParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by SynapseParser#forStatement.
    def enterForStatement(self, ctx:SynapseParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SynapseParser#forStatement.
    def exitForStatement(self, ctx:SynapseParser.ForStatementContext):
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


    # Enter a parse tree produced by SynapseParser#orExpr.
    def enterOrExpr(self, ctx:SynapseParser.OrExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#orExpr.
    def exitOrExpr(self, ctx:SynapseParser.OrExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#andExpr.
    def enterAndExpr(self, ctx:SynapseParser.AndExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#andExpr.
    def exitAndExpr(self, ctx:SynapseParser.AndExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#eqExpr.
    def enterEqExpr(self, ctx:SynapseParser.EqExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#eqExpr.
    def exitEqExpr(self, ctx:SynapseParser.EqExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#relExpr.
    def enterRelExpr(self, ctx:SynapseParser.RelExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#relExpr.
    def exitRelExpr(self, ctx:SynapseParser.RelExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#addExpr.
    def enterAddExpr(self, ctx:SynapseParser.AddExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#addExpr.
    def exitAddExpr(self, ctx:SynapseParser.AddExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#mulExpr.
    def enterMulExpr(self, ctx:SynapseParser.MulExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#mulExpr.
    def exitMulExpr(self, ctx:SynapseParser.MulExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#unaryExpr.
    def enterUnaryExpr(self, ctx:SynapseParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by SynapseParser#unaryExpr.
    def exitUnaryExpr(self, ctx:SynapseParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by SynapseParser#primary.
    def enterPrimary(self, ctx:SynapseParser.PrimaryContext):
        pass

    # Exit a parse tree produced by SynapseParser#primary.
    def exitPrimary(self, ctx:SynapseParser.PrimaryContext):
        pass


    # Enter a parse tree produced by SynapseParser#exprList.
    def enterExprList(self, ctx:SynapseParser.ExprListContext):
        pass

    # Exit a parse tree produced by SynapseParser#exprList.
    def exitExprList(self, ctx:SynapseParser.ExprListContext):
        pass



del SynapseParser