import os # permite que minhas variaveis interaja com o sistema operacinal do meu pc 
from dotenv import load_dotenv

# Carrega o arquivo .env
load_dotenv()

# Pega a chave da OpenAI do .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # aqui tem um exemplo de interação biblioteca (os)."acessa"(get)aqrquivo(.env)chave openai
