import speech_recognition


def recognize_voice():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as src:
        try:
            audio = recognizer.adjust_for_ambient_noise(src)
            print("Threshold Value After calibration:" + str(recognizer.energy_threshold))
            print("Please speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio_data = audio, language ="pt-BR").lower()
        except Exception as ex:
            print("Sorry. Could not understand.")
    return speech_to_txt

print(recognize_voice())