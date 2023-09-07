"""
    Autor: Iago Magalhães
    Descrição:
        - Função para conversão para tons de cinza
        - Função para conversão para HSV
"""

from skimage import color

def acizentado(image):
    result = color.rgb2gray(image)
    return result

def cor_coisada(image):
    result = color.rgb2hsv(image)
    return result