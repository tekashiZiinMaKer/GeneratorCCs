#! /bin/bash 

#Generator CCs _
# Version: 1.0
# Description: Generator CC's, A Simple Script That Lets You Generate CC's! 
# Author: tekashiZiinMaKer
# Github: https://github.com/tekashiZiinMaKer
# E-mail: tekashimaker504@gmail.com
# Crédits: tekashiZiinMaKer
# Date: 22-02-2022
# Language: Python
# Portable: file 
# Sif you copy, consider giving credit! We keep our code  open source to help others

import sys
import os
import time
import socket
import random


#bibliotecas
import random
from datetime import date
#variaveis
con = bin = 0
data = date.today().year

#layout
os.system("clear")
print('olá vou checar se tem alguma atualização se tiver vou atualizar, peço que aguarde') 
time.sleep(0.5)
os.system("pkg install figlet")
os.system("clear")
os.system("figlet Generator CCs")
print
print('-' *43)
print(' [1] - VISA')         
print(' [2] - MASTER')
print(' [3] - BIN')
print(' by tekashiZiinMaker ')
print('-' *43)
#Estruturas
while True:
    op = int(input(' select an option: '))
    cvv = random.randrange(1,999)
    mes = random.randint(1,12)
    ano = data + random.randint(1,7)
    cc = random.randrange(1,9999999999)
    if op == 1:
        bin = 406655
        con += 1
        print('-' * 43)
        print('')
        print(' CC VISA GENERATED #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op == 2: 
        bin = 545805
        con += 1
        print('-' * 43)
        print('')
        print(' CC MASTER GENERATED #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op == 3:
        bin = int(input(' Add a bin 06 digits:'))
        con += 1
        print('-' * 43)
        print('')
        print(' BIN GENERATED #{}'.format(con))
        print('')
        print(' Cartão: {}{}'.format(bin, cc))
        print(' Cvv: {}'.format(cvv))
        print(' Validade: mês {} de {}'.format(mes, ano))
        print('-' *43)
    elif op < 1:
        print('')
        print('Generator closed successfully!')
        print('')
        break
    else:
        print('-' * 43)
        print('Erro! type again!')
        print('-' *43)
    print('Best Generator CCs here !')
    print('')
