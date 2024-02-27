import calculadora

def main():
    a = 2
    b = 3
    soma = calculadora.soma(a, b)
    print (f'{a} + {b} = {soma}')
    subtracao = calculadora.subtrair(a, b)
    print (f'{a} - {b} = {subtracao}')
    produto = calculadora.multiplicar(a, b)
    print(f'{a} * {b} = {produto}')

main()