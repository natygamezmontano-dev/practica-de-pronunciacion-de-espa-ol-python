import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr

import random

from googletrans import Translator
duration = 5  # segundos de grabación
count=0
sample_rate = 44100
idioma=input("Hola hoy vamos a mejorar tu nivel de pronunciación en español😮, para eso puedes decir las palabras que te mostraremos y hablaras cuando se te indique 😋🤩🤔😝 escoje un nivel: facil, medio, dificil ")
for _ in range(5):  # repetir el proceso 5 veces
    
    facil=["hola","como estas","perro"] # idiomas fáciles de aprender
    medio=["banano", "escuela", "amigo", "ventana", "amarillo"] # idiomas medios de aprender
    dificil= ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"] # idiomas difíciles de aprender
    def palabra():
        if idioma=="facil":
            print(random.choice(facil))
        elif idioma=="medio":
            print(random.choice(medio))
        elif idioma=="dificil":
            print(random.choice(dificil))
    print(palabra())
    print("Habla ahora🥺...")
    recording = sd.rec(
    int(duration * sample_rate), # el número de muestras a grabar
    samplerate=sample_rate,      # tasa de muestreo
    channels=1,                  # 1 significa grabación mono
    dtype="int16")               # tipo de datos para las muestras grabadas
    sd.wait()  # esperando a que termine la grabación

    wav.write("output.wav", sample_rate, recording)
    print("Grabación completa, ahora reconociendo...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language=idioma)
            while True:
                
                if text in facil:
                    print("¡Bien hecho! Has pronunciado correctamente.")
                    count+=1
                    break
                if text in medio:
                    print("¡Bien hecho! Has pronunciado correctamente.")
                    count+=1
                    break
                if text in dificil:
                    print("¡Bien hecho! Has pronunciado correctamente.")
                    count+=1
                    break
                else:
                    print("mmm quieres volver a intentarlo?!!!.")
                    break
    
        except sr.UnknownValueError:             # - si Google no pudo entender el habla debido a ruido o silencio
            print("No se pudo reconocer el habla.")
        except sr.RequestError as e:             # - si no hay conexión a Internet o la API no está disponible
            print(f"Error del servicio: {e}")
print("Tu puntuación es:",count)
            ##translator = Translator()
       ## translated = translator.translate(text, dest=idioma)  # el 'en' aquí es un código para Inglés
        ##print("🌍 Traducción al español:", translated.text)




























