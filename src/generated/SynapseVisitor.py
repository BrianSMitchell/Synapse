# Generated from grammar/Synapse.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SynapseParser import SynapseParser
else:
    from SynapseParser import SynapseParser

# This class defines a complete generic visitor for a parse tree produced by SynapseParser.

class SynapseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SynapseParser#program.
    def visitProgram(self, ctx:SynapseParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#statement.
    def visitStatement(self, ctx:SynapseParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#importStatement.
    def visitImportStatement(self, ctx:SynapseParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#funcStatement.
    def visitFuncStatement(self, ctx:SynapseParser.FuncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#tryStatement.
    def visitTryStatement(self, ctx:SynapseParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#paramList.
    def visitParamList(self, ctx:SynapseParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#letStatement.
    def visitLetStatement(self, ctx:SynapseParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#assignStatement.
    def visitAssignStatement(self, ctx:SynapseParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#forStatement.
    def visitForStatement(self, ctx:SynapseParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#ifStatement.
    def visitIfStatement(self, ctx:SynapseParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#morphStatement.
    def visitMorphStatement(self, ctx:SynapseParser.MorphStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#goalStatement.
    def visitGoalStatement(self, ctx:SynapseParser.GoalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#exprStatement.
    def visitExprStatement(self, ctx:SynapseParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#rule.
    def visitRule(self, ctx:SynapseParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#expr.
    def visitExpr(self, ctx:SynapseParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#orExpr.
    def visitOrExpr(self, ctx:SynapseParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#andExpr.
    def visitAndExpr(self, ctx:SynapseParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#eqExpr.
    def visitEqExpr(self, ctx:SynapseParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#relExpr.
    def visitRelExpr(self, ctx:SynapseParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#addExpr.
    def visitAddExpr(self, ctx:SynapseParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#mulExpr.
    def visitMulExpr(self, ctx:SynapseParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#unaryExpr.
    def visitUnaryExpr(self, ctx:SynapseParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#primary.
    def visitPrimary(self, ctx:SynapseParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynapseParser#exprList.
    def visitExprList(self, ctx:SynapseParser.ExprListContext):
        return self.visitChildren(ctx)



del SynapseParser