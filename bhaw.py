from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)

from scipy.io.wavfile import write as write_wav
import os

# Specify absolute path for the audio file
file_path = r"C:\Users\anand\OneDrive\Documents\bark-audio\recording\audio.wav"


# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Save the audio file
try:
    write_wav(file_path, SAMPLE_RATE, audio_array)
    print(f"Audio file saved successfully at {file_path}")
except FileNotFoundError:
    print("Error: Could not save audio file. Please check the file path and permissions.")