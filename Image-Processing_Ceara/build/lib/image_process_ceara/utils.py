"""
    Autor: Iago Magalhães
    Descrição:
        - Função para plot de imagem
        - Função para plot de gráficos
"""

import matplotlib.pyplot as plt

def amostra_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()

def amostra_hist(image, title='Hist', cmap_type='gray'):
    plt.hist(image.ravel(), bins=256)
    plt.title(title)
    plt.axis('off')
    plt.show()