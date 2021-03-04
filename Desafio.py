# Criar 10 pastas com 10 arquivos dentro de cada uma
import os

diretorio = 'desafio_1'  # Diretorio setado como uma variável para uso posterior

if not os.path.exists(diretorio):  # Checa se não existe esse diretório, se não existe, cria ele
    os.mkdir(diretorio)

for i in range(1,11):
    if not os.path.exists(diretorio+'//pasta_'+str(i)):  # Checa se existem essas pastas no diretório setado anteriormente, caso não, cria essas pastas
        os.mkdir(diretorio+'//pasta_'+str(i))  # Cria-se aqui uma pasta no diretorio desafio_1. Pasta essa acompanhada pelo index de i -> 1 - 10
    
    for j in range(1,11):
        open(diretorio+'//pasta_'+str(i)+'//arquivo_'+str(j)+'.txt', 'w+')  # Cria-se os arquivos .txt dentro dessas pastas