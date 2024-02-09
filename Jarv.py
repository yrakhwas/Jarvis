import speech_recognition as sr
import pyautogui as pg

def listen_command_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(source=mic, duration=0.5)
        print("Скажіть щось...")
        audio = recognizer.listen(source=mic, timeout=5, phrase_time_limit=5)

    try:
        query = recognizer.recognize_google(audio, language='uk-UA').lower()
        print("Ви сказали:", query)
        return query
    except sr.UnknownValueError:
        print("Голос не розпізнано.")
        return None
    except sr.RequestError as e:
        print(f"Помилка сервісу розпізнавання: {e}")
        return None

def main():
    while True:
        print("Я вас слухаю")
        voice_command = listen_command_voice()

        if voice_command:
            print("Виконую команду:", voice_command)
            # Тут ви можете додати свої власні команди та логіку обробки

        else:
            print("Очікую команду")

if __name__ == "__main__":
    main()
