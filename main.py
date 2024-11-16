''' Feito por:
Aloísio Marques Lingo Filho
e
Guilherme de Souza Dionisio Rosseti
'''

from sympy import var
from sympy import sympify
from sympy.utilities.lambdify import lambdify


def bisection(f, a, b, E):
    '''Aproximação da solução de f(x) = 0 no intervalo[a, b] pelo método de bissecção.

    Parâmetros
    ----------
    f: função f(x)
        A função no qual queremos encontrar a aproximação de f(x) = 0.
    a, b: números reais
        O intervalo de busca para a solução.
        A função retorna None caso f(a)*f(b) >= 0 por não respeitar o Teorema do Ponto Intermediário
    E: Decimal
        Tolerância de erro esperada.

    Retorna
    -------
    x_N: número real
        O intermédio do enésimo intervalo computado pelo método de bissecção.

    Exemplos
    --------
    >> > f = lambda x: x**2 - x - 1
    >> > bisection(f, 1, 2, 25)
    1.618033990263939
    >> > f = lambda x: (2*x - 1)*(x - 3)
    >> > bisection(f, 0, 1, 10)
    0.5
    '''
    if f(a)*f(b) >= 0:
        print("Bissecção falhou.")
        return None
    a_n = a
    b_n = b
    e_n = abs(f(a+b/2))
    n = 1
    while (e_n > e):
        print(f"a = {a_n}; b = {b_n}; x{n} = {(a_n + b_n) / 2}")
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)

        e_n = abs(f_m_n)
        print(f"Erro atual: {e_n}")

        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            break
        else:
            print("Bissecção falhou.")
            return None

        n += 1
        print("-"*50)
    print(f"Nº de iterações: {n}\n")
    print(f"Raiz de f(x) é {(a_n + b_n) / 2}")
    return (a_n + b_n)/2


def newton(f, Df, x0, E):
    '''Aproximação da solução de f(x) = 0 pelo método de Newton.

    Parâmetros
    ----------
    f : função f(x)
        A função no qual queremos encontrar a aproximação de f(x) = 0.
    Df : function f'(x)
        Derivada de f(x).
    x0 : número real
        Chute inicial para a solução f(x) = 0.
    E : número real
        Tolerância usada como critério de parada |f(xn)| < E.

    Retorna
    -------
    xn : número real
        Raiz aproximada de f(x)

    Examplos
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8)
    1.618033988749989
    '''
    xn = x0
    e_n = abs(f(x0))
    n = 1
    while (e_n > E):
        print(f"x{n-1} = {xn};")
        fxn = f(xn)
        e_n = abs(fxn)
        print(f"Erro atual: {e_n}\n")
        print("-"*50)
        if e_n <= E:
            print(f'Nº de iterações {n}\n')
            print(f'Raiz de f(x) é {xn}\n')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Derivada resulta em zero. Solução não encontrada.')
            return None
        xn = xn - fxn/Dfxn
        n += 1
    print(f"x{n-1} = {xn};")
    print(f"Erro atual: {e_n}\n")
    print(f'Nº de iterações {n}\n')
    print(f'Raiz de f(x) é {xn}\n')
    return None


x = var('x')  # Definindo qual a variável da função


while (True):
    print("-"*50)
    print("ENCONTRAR ZERO EM FUNÇÃO")
    print("-"*50)
    user_input = input("Digite a função f(x): ")
    expr = sympify(user_input)
    f = lambdify(x, expr)

    print("-"*50)
    print("TOLERÂNCIA")
    print("-"*50)

    e = float(input("Digite a tolerância: "))

    print("-"*50)
    print("BISSECÇÃO")
    print("-"*50)
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    print("\n")
    bisection(f, a, b, e)

    print("-"*50)
    print("NEWTON")
    print("-"*50)

    dF_expr = expr.diff(x)
    dF = lambdify(x, dF_expr)

    x0 = float(input("Digite o chute inicial: "))
    newton(f, dF, x0, e)

    break
