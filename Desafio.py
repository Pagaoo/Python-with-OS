# Criar 10 pastas com 10 arquivos dentro de cada uma
import os

diretorio = 'desafio_1'

if not os.path.exists(diretorio):
    os.mkdir(diretorio)

for i in range(1,11):
    if not os.path.exists(diretorio+'//pasta_'+str(i)):
        os.mkdir(diretorio+'//pasta_'+str(i))
    
    for j in range(1,11):
        open(diretorio+'//pasta_'+str(i)+'//arquivo_'+str(j)+'.txt', 'w+')