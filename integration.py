
api_key = "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"


from time import sleep
import openai

openai.api_key = api_key

def conversar(texto):
    if("bahia" in texto):
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Supunha que você é um banco de dados geográfico da bahia. Voce fornecerá informações apenas do estados da bahia. Se pergutarem algo além de coisas relacionados à bahia, Não responda. Suas respostas devem ser Simplificadas ao máximo possível. Seja direto semelhante à um banco de dados, apenas forneça o dados puro. Responda as perguntas com apenas uma palavra APENAS UMA. Responda apenas perguntas relacionados à BAHIA. Se te perguntarem quantidade forneça apenas o número."},
                {"role": "user", "content": texto},
            ],
            temperature=0.7,
        )
    else:
        sleep(7)
        return "Error: Timeout"

    return resposta['choices'][0]['message']['content']


