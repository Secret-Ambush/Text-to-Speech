from bark import SAMPLE_RATE, generate_audio, preload_models
import scipy
import pyaudio

# Text which needs to be converted into Speech
text_prompt1 = """ A Learjet 45 aircraft with eight people on board veered off on thursday"""

# generate audio numpy array for given text
speech_array1 = generate_audio(text_prompt1, history_prompt="en_speaker_6")

# play text in notebook
P = pyaudio.PyAudio()

stream = P.open(format=pyaudio.paInt16, channels=1, output=True)
stream.write(speech_array1.tobytes())

stream.close() # this blocks until sound finishes playing

P.terminate()

# to save as wav file
scipy.io.wavfile.write("bark_out1.wav", rate=SAMPLE_RATE,data=speech_array1) 

# text_prompt2 = """ woman: Hi Shakira ,how are you? """
# speech_array2 = generate_audio(text_prompt2)
