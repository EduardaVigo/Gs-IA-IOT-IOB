from gtts import gTTS
import speech_recognition as sr
import pygame

pygame.init()
pygame.mixer.init()
microfone = sr.Microphone()
reconhecedor = sr.Recognizer()


def cadastrar_alimentos():
    while True:
        audio = gTTS("Qual o nome do alimento que você gostaria de cadastrar? Ou diga 'Não quero cadastrar' para sair.",
                     lang='pt-br')
        audio.save('Audios/nome_alimento.mp3')
        pygame.mixer.music.load('Audios/nome_alimento.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        print("Qual o nome do alimento que você gostaria de cadastrar? Ou diga 'Não quero cadastrar' para sair.")

        with microfone as source:
            audio = reconhecedor.listen(source)
        texto = reconhecedor.recognize_google(audio, language='pt-br')

        if "não quero cadastrar" in texto.lower():
            audio = gTTS("Tudo bem! Nos vemos numa próxima.", lang='pt-br')
            audio.save('Audios/finalizacao.mp3')
            pygame.mixer.music.load('Audios/finalizacao.mp3')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pass
            print("Tudo bem! Nos vemos numa próxima.")
            break

        nome_alimento = texto

        audio = gTTS(f"Alimento cadastrado: {nome_alimento}.", lang='pt-br')
        audio.save('Audios/nome_cadastrado.mp3')
        pygame.mixer.music.load('Audios/nome_cadastrado.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        print(f"Alimento cadastrado: {nome_alimento}.")

        cadastrar_quantidade(nome_alimento)

def cadastrar_quantidade(nome_alimento):
    audio = gTTS(f"Qual a quantidade de {nome_alimento} você gostaria de cadastrar?", lang='pt-br')
    audio.save('Audios/qtd_alimento.mp3')
    pygame.mixer.music.load('Audios/qtd_alimento.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    print(f"Qual a quantidade de {nome_alimento} você gostaria de cadastrar?")

    with microfone as source:
        audio = reconhecedor.listen(source)

    try:
        qtd_alimento = reconhecedor.recognize_google(audio, language='pt-br')
        audio = gTTS(f"Foram cadastrados: {qtd_alimento}.", lang='pt-br')
        audio.save('Audios/qtd_cadastrada.mp3')
        pygame.mixer.music.load('Audios/qtd_cadastrada.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        print(f"Quantidade cadastrada: {qtd_alimento}(s).")
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a quantidade. Tente novamente.")


cadastrar_alimentos()
