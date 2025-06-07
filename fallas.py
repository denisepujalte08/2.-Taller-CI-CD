# Romper Flake8
def foo():
    print("sin indentación")  # <-- mal indentado


# Romper SonarCloud
def bug_division():
    return 1 / 0


def suma(a, b):
    return a + b


def suma2(a, b):
    return a + b


def no_usada():
    return "esto nunca se usa"


def test_algo():
    pass


def hola():
    x = 42
    return "chau"
