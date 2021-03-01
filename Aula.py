import os  # Importa o pacote os
import platform  # Importa o pacote platform
import shutil

nome = platform.system()  # Pega o nome da plataforma que estamos usando, windows nesse caso.
print(nome)

print('-'*45)

meio_ambiente = os.environ['HOMEDRIVE']  # Mostra as especificações do ambiente do OS. Pode usar as keys para pegar informações, pois é um dicionario. Caso não seja o caso, usar somente os.environ
print(meio_ambiente)

print('-'*45)

ip_processo = os.getpid()  # Pega o id do processo atual
print(ip_processo)

print('-'*45)
 
print('Caminho do arquivo:', os.getcwd())  # Retorna o caminho do arquivo
print('Caminho completo do arquivo:', __file__)  # Retorna o caminho completo do arquivo, com o arquivo 'Aula.py' incluso
print('Nome do arquivo atual:', os.path.basename(__file__))  # Retorna somente o arquivo 'Aula.py'
print('Pasta do arquivo atual:', os.path.dirname(__file__))  # Retorna o diretorio do arquivo, como na getcwd
print('Caminho absoluto do arquivo:', os.path.abspath(__file__))  # Retorna o diretorio absoluto do arquivo

print('-'*45)

print('Lista de arquivos no diretorio atual:', os.listdir())  # Lista o diretorio atual. O que tem nesse diretorio
print('lISTA DE ARQUIVOS NO DIRETORIO C:', os.listdir('C://'))  # Lista o diretorio C://

# os.mkdir('Teste//Segundo_teste')  # Cria uma pasta no diretorio atual, caso queira criar em outro diretorio, especifica-se o mesmo. Além de que não é possivel criar uma pasta de mesmo nome, mesmo em outro diretorio
# os.mkdir('C://teste') exemplo de criação no disco C
# Não é uma função recursiva, tem que criar cada diretorio manualmente

# os.rename('Teste//arquivo45.txt', 'Teste//arquivo455.txt')  # Renomeio o arquivo selecionado para aquivo45
# os.rename('Teste//Segundo_teste', 'Teste//Teste_2')  # Também pode ser utilizado para renomear diretorios

print('-'*45)

shutil.copy2('Teste//arquivo455.txt', 'Teste//Teste_2//arquivo_teste.txt')  # Copia o arquivo para outro diretorio, podendo mudar o nome do mesmo.
# O primeiro parametro é a origem e o segundo o destino do arquivo