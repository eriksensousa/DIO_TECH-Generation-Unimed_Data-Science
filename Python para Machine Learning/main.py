"""
    Main.py
    Autor: Iago Magalhães
    Descrição: Rede neural profunda para classificação de digitos com PyTorch
"""

import numpy as np
import torch
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
from time import time
from torchvision import datasets, transforms
from torch import nn, optim

transform = transforms.ToTensor()
trainset = datasets.MNIST('./MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

valset = datasets.MNIST('./MNIST_data/', download=True, train=False, transform=transform)
valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
imagens, etiquetas = dataiter.next()
plt.imshow(imagens[0].np.squeeze(), cmap='gray_r')

print(imagens[0].shape)
print(etiquetas[0].shape)

class Modelo(nn.Module):
    """
        Modelo
        Classe do modelo da rede neural
    """
    def __init__(self):
        """
             Método construtor da classe Modelo
        """
        super(Modelo, self).__init__()
        self.linear1 = nn.Linear(28*28, 128)
        self.linear2 = nn.Linear(128, 64)
        self.linear3 = nn.Linear(64, 10)

    def forward(self, x):
        X = F.relu(self.linear1(X))
        X = F.relu(self.linear2(X))
        X = self.linear3(X)
        return F.log_softmax(X, dim=1)
    
def treino(modelo, trainloader, device):
    """
        Método treino
        :param modelo: modelo da rede neural
        :param trainloader: dados de treino do modelo
        :param device: hardware de execução
    """
    otimizador = optim.SGD(modelo.parameters(), lr=0.01, momentum=0.5)
    inicio = time()

    criterio = nn.NLLLoss()
    EPOCHS = 10
    modelo.train()

    for epoch in range(EPOCHS):
        perda_acumulada = 0
        for imagens, etiquetas in trainloader:
            imagens = imagens.view(imagens.shape[0], -1)
            otimizador.zero_grad()
            output = modelo(imagens.to(device))
            perda_instantanea = criterio(output, etiquetas.to(device))
            perda_instantanea.backward()
            otimizador.step()
            perda_acumulada += perda_instantanea.item()
        else:
            print('Epoch {} - Perda resultante: {}'.format(epoch+1, perda_acumulada/len(trainloader)))
    print('|n Tempo de treino (em minutos) = ', (time() - inicio) / 60)

def validacao(modelo, valloader, device):
    """
        Método validação
        :param modelo: modelo da rede neural
        :param vallloader: dados de validação do modelo
        :param device: hardware de execução
    """
    conta_corretas, conta_todas = 0, 0
    for imagens, etiquetas in valloader:
        for i in range(len(etiquetas)):
            img = imagens[i].view(1,784)
            with torch.no_grid():
                logps = modelo(img.to(device))
            
            ps = torch.exp(logps)
            probab = list(ps.cpu().np()[0])
            etiqueta_pred = probab.index(max(probab))
            etiqueta_certa = etiquetas.np()[i]
            if(etiqueta_certa == etiqueta_pred):
                conta_corretas += 1
            conta_todas += 1
    
    print('Total de imagens testadas = ', conta_todas)
    print('\n Precisão do modelo = {}%'.format(conta_corretas*100/conta_todas))

modelo = Modelo()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
modelo.to(device)