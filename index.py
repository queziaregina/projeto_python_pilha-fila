from collections import deque

fila = deque()

def menu_principal():
        while True:
            print("""
            MENU PRINCIPAL
            1 – Operações
            2 – Expressões
            0 – Finalizar Programa
            """)

            opcao_menu_principal = int(input("Escolha uma das opções acima: "))

            if opcao_menu_principal == 1:
                menu_operacoes()
            elif opcao_menu_principal == 2:
                validar_expressao()
            elif opcao_menu_principal == 0:
                print("Programa Finalizado.")
                break

def menu_operacoes():
        print("""
        OPERAÇÕES
        1 – Adicionar Operação na Fila
        2 - Executar Próxima Operação da Fila 
        3 – Executar Todas as Operações da Fila 
        0 – Voltar para o Menu Principal
        """)

        opcao_menu_operacoes = int(input("Escolha uma das opções acima: "))

        if opcao_menu_operacoes == 1:
            adicionar_operacao()
        if opcao_menu_operacoes == 2:
            proxima_fila()
        if opcao_menu_operacoes == 3:
            todas_as_operacoes()
        if opcao_menu_operacoes == 0:
            menu_principal()

        return opcao_menu_operacoes
              
def adicionar_operacao():
    print("""
    1 – Adição (+)
    2 – Subtração (–)
    3 – Multiplicação (*)
    4 – Divisão (/)
    """)

    operacao_escolhida = int(input("Escolha uma das operações: "))

    valores = input("Digite os valores para serem adicionados na Fila: ").split()
    fila.append((operacao_escolhida, valores))
    print("Operação adicionada na Fila com sucesso!")

def proxima_fila():
    if len(fila) == 0:
        print("Fila vazia!")
    else:
        operacao_escolhida, valores = fila.popleft()

        resultado = calcular(operacao_escolhida, valores)
        print(f"Operação: {operacao_escolhida} Valores: {valores} Resultado: {resultado}")

def todas_as_operacoes():
    if len(fila) == 0:
        print("Fila de operações vazia!")
    else:
        while len(fila) > 0:
            operacoes, valores = fila.popleft()
            resultado = calcular(operacoes, valores)
            print(f"Operação: {operacoes} Valores: {valores} Resultado: {resultado}")

def calcular(operacao_escolhida, valores):
    valores = [int(v) for v in valores]

    if operacao_escolhida == 1:
        return sum(valores)
    
    elif operacao_escolhida == 2:
        return valores[0] - sum(valores[1:])
    
    elif operacao_escolhida == 3:
        resultado = 1
        for v in valores:
            resultado *= v
        return resultado
    
    elif operacao_escolhida == 4:
        resultado = valores[0]
        for v in valores[1:]:
            resultado /= v
        return resultado
    
def validar_expressao():
    pilha = []

    expressao_informada = input("Escreva uma expressão matemática: ")

    for valor in expressao_informada:
        if valor in '({[':
                pilha.append(valor)
                
menu_principal()