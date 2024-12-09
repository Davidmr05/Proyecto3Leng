# Generated from DSL_ML.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DSL_MLParser import DSL_MLParser
else:
    from DSL_MLParser import DSL_MLParser

# This class defines a complete listener for a parse tree produced by DSL_MLParser.
class DSL_MLListener(ParseTreeListener):

    # Enter a parse tree produced by DSL_MLParser#program.
    def enterProgram(self, ctx:DSL_MLParser.ProgramContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#program.
    def exitProgram(self, ctx:DSL_MLParser.ProgramContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#statement.
    def enterStatement(self, ctx:DSL_MLParser.StatementContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#statement.
    def exitStatement(self, ctx:DSL_MLParser.StatementContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:DSL_MLParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:DSL_MLParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#assignment.
    def enterAssignment(self, ctx:DSL_MLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#assignment.
    def exitAssignment(self, ctx:DSL_MLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#expression.
    def enterExpression(self, ctx:DSL_MLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#expression.
    def exitExpression(self, ctx:DSL_MLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#functionCall.
    def enterFunctionCall(self, ctx:DSL_MLParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#functionCall.
    def exitFunctionCall(self, ctx:DSL_MLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#conditional.
    def enterConditional(self, ctx:DSL_MLParser.ConditionalContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#conditional.
    def exitConditional(self, ctx:DSL_MLParser.ConditionalContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#loop.
    def enterLoop(self, ctx:DSL_MLParser.LoopContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#loop.
    def exitLoop(self, ctx:DSL_MLParser.LoopContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#condition.
    def enterCondition(self, ctx:DSL_MLParser.ConditionContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#condition.
    def exitCondition(self, ctx:DSL_MLParser.ConditionContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:DSL_MLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:DSL_MLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#block.
    def enterBlock(self, ctx:DSL_MLParser.BlockContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#block.
    def exitBlock(self, ctx:DSL_MLParser.BlockContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#range.
    def enterRange(self, ctx:DSL_MLParser.RangeContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#range.
    def exitRange(self, ctx:DSL_MLParser.RangeContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#matrixOperation.
    def enterMatrixOperation(self, ctx:DSL_MLParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#matrixOperation.
    def exitMatrixOperation(self, ctx:DSL_MLParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#matrixRow.
    def enterMatrixRow(self, ctx:DSL_MLParser.MatrixRowContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#matrixRow.
    def exitMatrixRow(self, ctx:DSL_MLParser.MatrixRowContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#graphOperation.
    def enterGraphOperation(self, ctx:DSL_MLParser.GraphOperationContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#graphOperation.
    def exitGraphOperation(self, ctx:DSL_MLParser.GraphOperationContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#fileOperation.
    def enterFileOperation(self, ctx:DSL_MLParser.FileOperationContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#fileOperation.
    def exitFileOperation(self, ctx:DSL_MLParser.FileOperationContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#mlOperation.
    def enterMlOperation(self, ctx:DSL_MLParser.MlOperationContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#mlOperation.
    def exitMlOperation(self, ctx:DSL_MLParser.MlOperationContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#printStatement.
    def enterPrintStatement(self, ctx:DSL_MLParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#printStatement.
    def exitPrintStatement(self, ctx:DSL_MLParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by DSL_MLParser#argumentList.
    def enterArgumentList(self, ctx:DSL_MLParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by DSL_MLParser#argumentList.
    def exitArgumentList(self, ctx:DSL_MLParser.ArgumentListContext):
        pass



del DSL_MLParser