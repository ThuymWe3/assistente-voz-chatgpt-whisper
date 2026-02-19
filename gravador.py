
import sounddevice as sd # biblioteca que faz uma interação com pythin e meu pc micro e autofalant
from scipy.io.wavfile import write # biblioteca que tranforma os dados(numeros) em ""som"""formato (wav)  
import os # biblioteca que faz "ponte" entre  Python e a  interação com meu sistema 

# função grava audio 
def gravar_audio():

    fs = 44100    # parametro de qualidade tipo CD 
    duracao = 5   # tempo de duração 

    print("Gravando áudio por 5 segundos...") # Impressão de mensagem 
     
    grava = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()  # linha completa espera o terminal gravar; duração X frequencia = qualidade 

    pasta = "audio"   
    if not os.path.exists(pasta):  #se não houver evita erros se ja existe 
        os.makedirs(pasta) # cria pasta de audio

    caminho = os.path.join(pasta, "gravacao.wav") # cria endereço/nome pasta+arquivo com resultado Garante que o caminho funcione em qualquer sistema operacional Windows,Linux etc..) sem erros de formatação d

    write(caminho, fs, grava) # salva fisicamente o audio 

    print("Áudio salvo em", caminho) # ""converte em texto"""

    return caminho # retorno
