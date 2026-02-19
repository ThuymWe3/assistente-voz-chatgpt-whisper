# Importa funções para gravar e trancrever audio 
from gravador import gravar_audio
from transcrever import transcrever_audio


print("Assistente inclusivo iniciado...") # mostra mensagem 

# Grava áudio
caminho = gravar_audio()

# Transcreve
texto = transcrever_audio(caminho)

print("Você disse:", texto)  # mostra mensagem 
