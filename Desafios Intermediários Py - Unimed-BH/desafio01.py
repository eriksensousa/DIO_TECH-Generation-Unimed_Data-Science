"""
ENTRADA:
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

SAÍDA:
Um único inteiro, que representa a posição da letra no alfabeto.

Ex: C -> 3
"""

letra = input() 

# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
alfabeto = [
            '',
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'L', 'K', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y',
            'Z'
          ]

index = alfabeto.index(letra)

print(index)