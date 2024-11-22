from classes import *
import os

def menu():
    while True:
        print('\n --  LOJA DE DOCES  -- \n')
        print('1 - DOCES E PREÇOS')
        print('2 - DESCRIÇÃO DOCES\n')
        try:
            escolha = int(input('---> '))
            os.system('pause')
            os.system('cls')
        except ValueError as e:
            print(f'Valor inválido, o erro foi: {e}')
            os.system('cls')

        match escolha:
            case 1:
                mostrar_precos()
                os.system('pause')
                os.system('cls')
            case 2:
                mostrar_descricao()
                os.system('pause')
            case _:
                print("Opção inválida.")
                os.system('pause')
                os.system('cls')


menu()
os.system("pause")