import os  # Importa o pacote os
import platform  # Importa o pacote platform

nome = platform.system()  # Pega o nome da plataforma que estamos usando, windows nesse caso.
print(nome)

meio_ambiente = os.environ['HOMEDRIVE']  # Mostra as especificações do ambiente do OS. Pode usar as keys para pegar informações, pois é um dicionario. Caso não seja o caso, usar somente os.environ
print(meio_ambiente)

ip_processo = os.getpid()  # Pega o id do processo atual
print(ip_processo)

caminho_atual = os.getcwd()  # Retorna o caminho do arquivo
print(caminho_atual)

print(__file__)  # Retorna o arquivo completo do arquivo, com o arquivo 'Aula.py' incluso