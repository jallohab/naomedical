import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from gtts import gTTS
import threading
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        # Use Google Web Speech API for conversion
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        result_label.config(text=f"Transcription: {text}", fg="#228B22")  # Green text
        
        # Translate the text
        translated = translator.translate(text, dest='es')  # Change 'es' to the desired language code
        translated_text = translated.text
        print(f"Translated: {translated_text}")
        translation_label.config(text=f"Translation: {translated_text}", fg="#228B22")  # Green text
        
        # Convert translated text to speech
        tts = gTTS(translated_text, lang='es')  # Change 'es' to the desired language code
        tts.save("translated_audio.mp3")
        play_audio("translated_audio.mp3")
        
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Google Speech API; {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        start_button.config(text="Start Listening", state=tk.NORMAL)

def play_audio(file_path):
    os.system(f"mpg321 {file_path}")

def start_recognition_thread():
    start_button.config(text="Listening...", state=tk.DISABLED)
    threading.Thread(target=recognize_speech).start()

# Create the main application window
app = tk.Tk()
app.title("Speech-to-Text Transcription and Translation")
app.geometry("600x400")
app.configure(bg="#FFC0CB")  # Pinkish background

# Add a label to display the transcription result
result_label = tk.Label(app, text="Transcription will appear here", wraplength=550, bg="#FFC0CB", font=("Helvetica", 16))
result_label.pack(pady=20)

# Add a label to display the translation result
translation_label = tk.Label(app, text="Translation will appear here", wraplength=550, bg="#FFC0CB", font=("Helvetica", 16))
translation_label.pack(pady=20)

# Add a button to start the speech recognition process
start_button = tk.Button(app, text="Start Listening", command=start_recognition_thread, bg="#0000FF", fg="white", activebackground="#0000FF", activeforeground="white", font=("Helvetica", 16))  # Blue button with white text
start_button.pack(pady=20)

# Add two break lines
tk.Label(app, text="", bg="#FFC0CB").pack()
tk.Label(app, text="", bg="#FFC0CB").pack()

# Add centered bold text
tk.Label(app, text="Below are the code", font=("Helvetica", 16, "bold"), bg="#FFC0CB").pack()

# Add a text widget to display the code
code_text = tk.Text(app, wrap=tk.WORD, bg="#FFC0CB", font=("Helvetica", 12))
code_text.pack(pady=20)
code_text.insert(tk.END, """import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
from googletrans import Translator
from gtts import gTTS
import threading
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        # Use Google Web Speech API for conversion
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        result_label.config(text=f"Transcription: {text}", fg="#228B22")  # Green text
        
        # Translate the text
        translated = translator.translate(text, dest='es')  # Change 'es' to the desired language code
        translated_text = translated.text
        print(f"Translated: {translated_text}")
        translation_label.config(text=f"Translation: {translated_text}", fg="#228B22")  # Green text
        
        # Convert translated text to speech
        tts = gTTS(translated_text, lang='es')  # Change 'es' to the desired language code
        tts.save("translated_audio.mp3")
        play_audio("translated_audio.mp3")
        
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results from Google Speech API; {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        start_button.config(text="Start Listening", state=tk.NORMAL)

def play_audio(file_path):
    os.system(f"mpg321 {file_path}")

def start_recognition_thread():
    start_button.config(text="Listening...", state=tk.DISABLED)
    threading.Thread(target=recognize_speech).start()

# Create the main application window
app = tk.Tk()
app.title("Speech-to-Text Transcription and Translation")
app.geometry("600x400")
app.configure(bg="#FFC0CB")  # Pinkish background

# Add a label to display the transcription result
result_label = tk.Label(app, text="Transcription will appear here", wraplength=550, bg="#FFC0CB", font=("Helvetica", 16))
result_label.pack(pady=20)

# Add a label to display the translation result
translation_label = tk.Label(app, text="Translation will appear here", wraplength=550, bg="#FFC0CB", font=("Helvetica", 16))
translation_label.pack(pady=20)

# Add a button to start the speech recognition process
start_button = tk.Button(app, text="Start Listening", command=start_recognition_thread, bg="#0000FF", fg="white", activebackground="#0000FF", activeforeground="white", font=("Helvetica", 16))  # Blue button with white text
start_button.pack(pady=20)

# Add two break lines
tk.Label(app, text="", bg="#FFC0CB").pack()
tk.Label(app, text="", bg="#FFC0CB").pack()

# Add centered bold text
tk.Label(app, text="Below are the code", font=("Helvetica", 16, "bold"), bg="#FFC0CB").pack()

# Add a text widget to display the code
code_text = tk.Text(app, wrap=tk.WORD, bg="#FFC0CB", font=("Helvetica", 12))
code_text.pack(pady=20)
code_text.insert(tk.END, "The code will be displayed here")

# Run the app
app.mainloop()
""")

# Run the app
app.mainloop()
