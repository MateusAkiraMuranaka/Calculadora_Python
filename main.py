import logging
from calculator import somar, subtrair, multiplicar, dividir
from configlog import setup_logging

def main():
    setup_logging()

    logging.info("Calculadora iniciada")

    print("Bem-vindo à Calculadora!")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    if escolha != '1' or escolha != '2' or escolha != '3' or escolha != '4':
        logging.critical(f'Erro crítico: valor inválido de entrada - {escolha}')
        print("Entrada inválida! Certifique-se de digitar números entre 1 e 4.")
        return
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError as e:
        logging.critical(f'Erro crítico: valor inválido de entrada - {e}')
        print("Entrada inválida! Certifique-se de digitar números.")
        return

    if escolha == '1':
        logging.info('Operação escolhida: Soma')
        print(f'Resultado: {somar(num1, num2)}')
    elif escolha == '2':
        logging.info('Operação escolhida: Subtração')
        print(f'Resultado: {subtrair(num1, num2)}')
    elif escolha == '3':
        logging.info('Operação escolhida: Multiplicação')
        print(f'Resultado: {multiplicar(num1, num2)}')
    elif escolha == '4':
        logging.info('Operação escolhida: Divisão')
        resultado = dividir(num1, num2)
        if resultado is not None:
            print(f'Resultado: {resultado}')
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        logging.warning(f'Operação inválida selecionada: {escolha}')
        print("Escolha inválida! Selecione uma operação válida.")

    logging.info("Calculadora finalizada")

if __name__ == "__main__":
    main()
