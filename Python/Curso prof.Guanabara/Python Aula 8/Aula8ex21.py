import pygame
import os
import sys

# Pega o caminho absoluto da pasta onde este script está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Muda o "foco" do Python para essa pasta
os.chdir(diretorio_atual)

pygame.mixer.init()

# Agora o Python vai achar o arquivo, pois ele "entrou" na pasta certa
arquivo_audio = "DownUnder.mp3" # Verifique se o nome está idêntico (maiúsculas/minúsculas)

if os.path.exists(arquivo_audio):
    print(f"Sucesso! Tocando: {arquivo_audio}")
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
else:
    print(f"Erro: O arquivo '{arquivo_audio}' não foi encontrado em: {diretorio_atual}")
    print("Arquivos que eu vejo nesta pasta:", os.listdir())