"""
ENTRADA:
A entrada consiste de diversos casos de teste.
Cada caso de teste consiste uma string informando qual a situação de levantamento de pernas do papagaio.

SAÍDA:
Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará.
Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.

Ex:
esquerda  -> ingles
direita   -> frances
nenhuma   -> portugues
ambas     -> caiu
"""

while True: 
    try: 
        #TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
        #e imprima a saída de acordo com a situação das pernas do papagaio
        res = input()
        if('esquerda' == res):
            print('ingles')
        elif('direita' == res):
            print('frances')
        elif('nenhuma' == res):
            print('portugues')
        else:
            print('caiu')
    except EOFError: 
        break