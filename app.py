from flask import Flask, render_template, Response
import speech_recognition as sr


app = Flask(__name__)


import speech_recognition as sr

def generate_audio():
    recognizer = sr.Recognizer()

    # Inisialisasi source di luar loop
    source = sr.Microphone()

    # Inisialisasi list untuk menyimpan hasil transkripsi
    transcriptions = []

    with source as audio_stream:
        print("Mulai mendengarkan...")

        while True:
            try:
                # Streaming audio
                audio_text = recognizer.listen(audio_stream)

                # Atur parameter language ke 'id-ID' untuk bahasa Indonesia
                text = recognizer.recognize_google(audio_text, language='id-ID')

                if text:  # Jika hasil transkripsi tidak kosong
                    transcriptions.append(text)

                # Kirim semua hasil transkripsi melalui generator
                yield f"data: {', '.join(transcriptions)}\n\n"

            except sr.UnknownValueError:
                # Jika tidak dapat memahami audio
                yield f"data: {', '.join(transcriptions)}\n\n"
            except sr.RequestError as e:
                # Jika terjadi kesalahan pada layanan Google Speech Recognition
                yield f"data: Error - {str(e)}\n\n"

    # Panggil source.__exit__() secara manual setelah loop selesai
    source.__exit__(None, None, None)  # agar hasil transkrip sebelumnya tetap ada

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech')
def speech():
    return render_template('speech.html')

@app.route('/stream')
def stream():
    return Response(generate_audio(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
