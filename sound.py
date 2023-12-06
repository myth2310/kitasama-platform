# listen_and_transcribe.py
import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Katakan sesuatu:")
        audio_text = recognizer.listen(source)

    try:
        # Atur parameter language ke 'id-ID' untuk bahasa Indonesia
        text = recognizer.recognize_google(audio_text, language='id-ID')
        print("Anda mengatakan:", text)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition tidak bisa memahami audio")
        return "Tidak diketahui"
    except sr.RequestError as e:
        print(f"Tidak bisa mendapatkan hasil dari layanan Google Speech Recognition; {e}")
        return "Error"

if __name__ == "__main__":
    listen_and_transcribe()
