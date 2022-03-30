import speech_recognition as sr
while True:
    try:
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
        word = r.recognize_google(audio, language="ru_RU")
        print(word)
    except sr.UnknownValueError:
        print("Не молчите !")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
