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
        value = self.visit(ctx.expression())
        print(value)

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
        elif ctx.getChildCount() == 3:  # Expresión binaria (e.g., a + b)
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
            else:
                raise Exception(f"Operador desconocido: {operator}")
        else:
            return self.visitChildren(ctx)
