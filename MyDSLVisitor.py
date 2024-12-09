from DSL_MLVisitor import DSL_MLVisitor

class MyDSLVisitor(DSL_MLVisitor):
    def __init__(self):
        self.variables = {}  # Diccionario para almacenar las variables

    # Manejo del programa principal
    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

    # Declaración de variables
    def visitVariableDeclaration(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        print(f"Variable '{var_name}' inicializada con valor: {value}")
        return value

    # Impresión
    def visitPrintStatement(self, ctx):
        value = [self.visit(arg) for arg in ctx.argumentList().expression()]
        print(" ".join(map(str, value)))

    # Manejo de expresiones
    def visitExpression(self, ctx):
        if ctx.NUMBER():  # Si es un número
            return float(ctx.NUMBER().getText())
        elif ctx.ID():  # Si es una variable
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Error: La variable '{var_name}' no está declarada.")
        elif ctx.getChildCount() == 3:  # Expresión binaria (e.g., a + b, x^y)
            left = self.visit(ctx.getChild(0))
            operator = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))

            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                return left / right
            elif operator == '%':
                return left % right
            elif operator == '^':  # Potencias
                return left ** right
            else:
                raise Exception(f"Operador desconocido: {operator}")
        else:
            return self.visitChildren(ctx)

    # Manejo de funciones (e.g., sin, cos, sqrt, plot)
    def visitFunctionCall(self, ctx):
        func_name = ctx.getChild(0).getText()
        args = []

        # Verifica si hay una lista de argumentos
        if ctx.argumentList():
            args = [self.visit(arg) for arg in ctx.argumentList().expression()]

        if func_name == 'sin':
            import math
            if len(args) < 1:
                raise Exception("La función 'sin' requiere un argumento.")
            return math.sin(args[0])
        elif func_name == 'cos':
            import math
            if len(args) < 1:
                raise Exception("La función 'cos' requiere un argumento.")
            return math.cos(args[0])
        elif func_name == 'sqrt':
            import math
            if len(args) < 1:
                raise Exception("La función 'sqrt' requiere un argumento.")
            return math.sqrt(args[0])
        elif func_name == 'plot':
            import matplotlib.pyplot as plt
            if len(args) < 2:
                raise Exception("La función 'plot' requiere dos listas como argumentos.")
            plt.plot(args[0], args[1])
            plt.show()
            return None
        else:
            raise Exception(f"Función no soportada: {func_name}")

    # Manejo de operaciones con matrices
    def visitMatrixOperation(self, ctx):
        import numpy as np

        if ctx.getChild(2).getText() == 'transpose':  # Transposición
            matrix = self.variables[ctx.ID(1).getText()]
            self.variables[ctx.ID(0).getText()] = np.transpose(matrix)
        elif ctx.getChild(2).getText() == 'inverse':  # Inversa
            matrix = self.variables[ctx.ID(1).getText()]
            self.variables[ctx.ID(0).getText()] = np.linalg.inv(matrix)
        elif ctx.getChild(2).getText() in ('+', '-', '*'):  # Operaciones
            left = self.variables[ctx.ID(0).getText()]
            right = self.variables[ctx.ID(2).getText()]
            operation = ctx.getChild(1).getText()

            if operation == '+':
                self.variables[ctx.ID(0).getText()] = np.add(left, right)
            elif operation == '-':
                self.variables[ctx.ID(0).getText()] = np.subtract(left, right)
            elif operation == '*':
                self.variables[ctx.ID(0).getText()] = np.matmul(left, right)
        else:
            raise Exception("Operación con matrices no soportada.")
