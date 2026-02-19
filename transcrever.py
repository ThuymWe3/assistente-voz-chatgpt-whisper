from openai import OpenAI # importa a biblioteca principal da openai me permitindo usar "prompt de comando para interagir com ChatGPT"
from config import OPENAI_API_KEY # importa o arquivo conf.py e identifica minha chave " seve como um filtro tambem "

# Cria cliente da Openai " servindo como passaporte de uso evitando o uso da chave secreta a todo momento "
client = OpenAI(api_key=OPENAI_API_KEY)


def transcrever_audio(caminho_audio): # função de transcrição 

    print("Transcrevendo áudio...")

    # Abre o arquivo de áudio
    with open(caminho_audio, "rb") as audio:

        # Envia para o Whisper (Speech-to-Text) e identifica o modelo do chatGpt
        resposta = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio
        )

    texto = resposta.text  # variavel texto armazena resposta  com "texto"

    print("Você disse:", texto) # insforma a mensagem escrita  ao cliente

    return texto # retorno padrao 
