# Romper Flake8
def foo():
print("sin indentación")  # <-- mal indentado

# Romper SonarCloud
def bar():
    if True:
        return "Esto es un error de SonarCloud"  # <-- mal uso de la condición
    else:
        return "Esto no debería ejecutarse"
