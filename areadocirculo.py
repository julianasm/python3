#versão01

pi = 3.14159
raio = 10
area_do_circulo = pi * (raio**2)
print("Area do circulo é igual a :", area_do_circulo)

#versao 02
from math import pi
raio = 15.3
print('area do circulo é igual a: ', pi * raio ** 2)
print(dir())

#versao 03

from math import pi
raio = input('Informe o raio: ')

print('area do circulo é igaul a: ', pi * float(raio) ** 2)
#é necessario converter para float ou int porque raio inicialmente é uma string

print('nome do modulo', __name__) #principal
print('nome do pacote',__package__)

import main.py

#versão 04

from math import pi

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    print('area do circulo é igaul a: ', pi * float(raio)**2)
#é necessario converter para float ou int porque raio inicialmente é uma string

#versão 05

from math import pi

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    print('area do circulo é igaul a: ', pi * float(raio)**2)
#é necessario converter para float ou int porque raio inicialmente é uma string

import __main__

#criando uma função sem retorno

from math import pi


def circulo(raio):  #definição da função
    print('area do circulo é igual a: ', pi * float(raio)**2)


#vai receber como parametro o raio do circulo
#entre parenteses são colocados os parametros da função

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)

from __main__ import (circulo)
print(circulo(2))
#é possivel importar a função e utiliza-la

#criando uma função com retorno

from math import pi


def circulo(raio):  #definição da função
    return (pi * float(raio)**2)


#vai receber como parametro o raio do circulo
#entre parenteses são colocados os parametros da função

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_do_circulo = circulo(raio)
    print('area do circulo é igual a:', area_do_circulo)

#é possivel importar a função e utiliza-la
