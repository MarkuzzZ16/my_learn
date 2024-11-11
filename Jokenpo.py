import random

x = 0
print('\033[36m-=-=-=JOKENPO=-=-=-\033[m')
print('\033[37m1 - PEDRA\033[m \n\033[34m2 - PAPEL \033[m\n\033[33m3 - TESOURA\033[m')
t = 1
while t == 1:
    x = int(input('Escolha o número correspondente: '))
    if x != 1 and x != 2 and x != 3:
        x = int(input('\033[31mCaractere inválido!\033[m escolha o número correspondente: '))
    pc = random.randint(1,3)

    if x == 1:
        if pc == 1:
            print('\033[33mEmpate\033[m')
        elif pc == 2:
            print('\033[31mVocê perdeu\033[m')
        elif pc == 3:
            print('\033[32mVocê venceu!\033[m')
    if x == 2:
        if pc == 1:
            print('\033[32mVocê Venceu!\033[m')
        elif pc == 2:
            print('\033[33mEmpate\033[m')
        elif pc == 3:
            print('\033[31mVocê perdeu.\033[m')
    if x == 3:
        if pc == 1:
            print('\033[31mVocê perdeu.\033[m')
        elif pc == 2:
            print('\033[32mVocê venceu!\033[m')
        elif pc == 3:
            print('\033[33mEmpate\033[m')

    t = int(input('Jogar novamente? \n \033[32m[1] SIM\033[m  \033[31m[2] NÃO\033[m -> '))
    if t != 1 and t != 2:
        t = int(input('\033[31mCaractere inválido!\033[m escolha o número correspondente: '))
    if t == 2:
        break