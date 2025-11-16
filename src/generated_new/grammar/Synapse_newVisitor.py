# Generated from grammar/Synapse_new.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Synapse_newParser import Synapse_newParser
else:
    from Synapse_newParser import Synapse_newParser

# This class defines a complete generic visitor for a parse tree produced by Synapse_newParser.

class Synapse_newVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Synapse_newParser#program.
    def visitProgram(self, ctx:Synapse_newParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#statement.
    def visitStatement(self, ctx:Synapse_newParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#importStatement.
    def visitImportStatement(self, ctx:Synapse_newParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#funcStatement.
    def visitFuncStatement(self, ctx:Synapse_newParser.FuncStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#tryStatement.
    def visitTryStatement(self, ctx:Synapse_newParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#paramList.
    def visitParamList(self, ctx:Synapse_newParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#letStatement.
    def visitLetStatement(self, ctx:Synapse_newParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#assignStatement.
    def visitAssignStatement(self, ctx:Synapse_newParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#forStatement.
    def visitForStatement(self, ctx:Synapse_newParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#ifStatement.
    def visitIfStatement(self, ctx:Synapse_newParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#morphStatement.
    def visitMorphStatement(self, ctx:Synapse_newParser.MorphStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#goalStatement.
    def visitGoalStatement(self, ctx:Synapse_newParser.GoalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#exprStatement.
    def visitExprStatement(self, ctx:Synapse_newParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#rule.
    def visitRule(self, ctx:Synapse_newParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#expr.
    def visitExpr(self, ctx:Synapse_newParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#orExpr.
    def visitOrExpr(self, ctx:Synapse_newParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#andExpr.
    def visitAndExpr(self, ctx:Synapse_newParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#eqExpr.
    def visitEqExpr(self, ctx:Synapse_newParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#relExpr.
    def visitRelExpr(self, ctx:Synapse_newParser.RelExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#addExpr.
    def visitAddExpr(self, ctx:Synapse_newParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#mulExpr.
    def visitMulExpr(self, ctx:Synapse_newParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#unaryExpr.
    def visitUnaryExpr(self, ctx:Synapse_newParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#primary.
    def visitPrimary(self, ctx:Synapse_newParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Synapse_newParser#exprList.
    def visitExprList(self, ctx:Synapse_newParser.ExprListContext):
        return self.visitChildren(ctx)



del Synapse_newParser