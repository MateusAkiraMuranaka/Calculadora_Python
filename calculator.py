import logging

def somar(a, b):
    resultado = a + b
    logging.debug(f'Soma: {a} + {b} = {resultado}')
    return resultado

def subtrair(a, b):
    resultado = a - b
    logging.debug(f'Subtração: {a} - {b} = {resultado}')
    return resultado

def multiplicar(a, b):
    resultado = a * b
    logging.debug(f'Multiplicação: {a} * {b} = {resultado}')
    return resultado

def dividir(a, b):
    try:
        resultado = a / b
        logging.debug(f'Divisão: {a} / {b} = {resultado}')
        return resultado
    except ZeroDivisionError as e:
        logging.error('Erro de divisão por zero')
        return None
