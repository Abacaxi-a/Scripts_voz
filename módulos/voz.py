from playsound import playsound
import gtts
import pandas as pd
import speech_recognition  as sr
import os

def perg(self):
    rec = sr.Recognizer()
    #print(sr.Microphone().list_microphone_names())
    with sr.Microphone(1) as mic:
        rec.adjust_for_ambient_noise(mic)
        if os.path.exists('frase_pergunta.mp3'):
            playsound(self.config['voz_pergunta'])
            audio = rec.listen(mic)
            self.texto = rec.recognize_google(audio,language='pt-BR') 
            print(self.texto)
        else:
            frase = gtts.gTTS('Qual seria o pedido',lang='pt-br')
            frase.save('frase_pergunta.mp3')    
        return self.texto

def resposta(self):
    return playsound(self.config['voz_encontrado'])

def resposta_errada(self):
    return playsound(self.config['voz_erro'])
