import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    '''
    transcribir discurso de grabacion de microfono
    parametro recognizer
    parametro microphone
    return None si el discurso no se pudo transcribir, de lo contrario un
    string contendra el texto de la transcripcion
    '''
    print('Porfavor lee la sentencia en inglés')
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    
    try:
        text = recognizer.recognize_google(audio)
    except Exception as e:
        print(e)
        text = None

    return text

if __name__ == '__main__':
    text = input('Please input a English word or sentence: ').strip()

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speech_text = recognize_speech_from_mic(recognizer, microphone)

    while speech_text != None and text.lower() != speech_text.lower():
        print(speech_text)

        speech_text = recognize_speech_from_mic(recognizer, microphone)

    if speech_text:
        print('{} {}'.format(speech_text, '✓'))
    else:
        print('Porfavor prueba el reconocimiento de discurso mas tarde')