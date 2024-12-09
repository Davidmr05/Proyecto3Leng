# Generated from DSL_ML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DSL_MLParser import DSL_MLParser
else:
    from DSL_MLParser import DSL_MLParser

# This class defines a complete generic visitor for a parse tree produced by DSL_MLParser.

class DSL_MLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DSL_MLParser#program.
    def visitProgram(self, ctx:DSL_MLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#statement.
    def visitStatement(self, ctx:DSL_MLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:DSL_MLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#assignment.
    def visitAssignment(self, ctx:DSL_MLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#arithmeticOperation.
    def visitArithmeticOperation(self, ctx:DSL_MLParser.ArithmeticOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#expression.
    def visitExpression(self, ctx:DSL_MLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#functionCall.
    def visitFunctionCall(self, ctx:DSL_MLParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#conditional.
    def visitConditional(self, ctx:DSL_MLParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#loop.
    def visitLoop(self, ctx:DSL_MLParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#condition.
    def visitCondition(self, ctx:DSL_MLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:DSL_MLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#block.
    def visitBlock(self, ctx:DSL_MLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#range.
    def visitRange(self, ctx:DSL_MLParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#matrixOperation.
    def visitMatrixOperation(self, ctx:DSL_MLParser.MatrixOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#matrixRow.
    def visitMatrixRow(self, ctx:DSL_MLParser.MatrixRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#graphOperation.
    def visitGraphOperation(self, ctx:DSL_MLParser.GraphOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#fileOperation.
    def visitFileOperation(self, ctx:DSL_MLParser.FileOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#mlOperation.
    def visitMlOperation(self, ctx:DSL_MLParser.MlOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#printStatement.
    def visitPrintStatement(self, ctx:DSL_MLParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DSL_MLParser#argumentList.
    def visitArgumentList(self, ctx:DSL_MLParser.ArgumentListContext):
        return self.visitChildren(ctx)



del DSL_MLParser