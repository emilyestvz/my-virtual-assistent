from flask import Flask, render_template, request, jsonify
import speech_recognition as sr 
import pyttsx3 
import time

app = Flask(__name__)

def ouvir_comando():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        f'''Olá, diga algo!'''
        audio = recognizer.listen(source)
        
        try:
            comando = recognizer.recognize_google(audio, language='pt-BR')
            return comando
        except sr.UnknownValueError:
            return 'Não entendi o que você disse.'
        except sr.RequestError:
            return 'Ocorreu um erro ao se conectar ao serviço de reconhecimento de voz.'
        
def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comando', methods=['POST'])
def comando():
    comando = ouvir_comando()
    resposta = f'Você disse: {comando}'
    falar(resposta)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
    time.sleep(1)  # Aguarda 1 segundo para garantir que o texto seja lido antes de parar o programa
    falar('Obrigado por utilizar o meu assistente!')