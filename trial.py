from bark import SAMPLE_RATE, generate_audio, preload_models
# import Audio to listen to generate audio array in notebook.
from IPython.display import Audio

# Text which needs to be converted into Speech
text_prompt1 = """
A Learjet 45 aircraft with eight people on board
veered off on thursday"""
# generate audio numpy array for given text
speech_array1 = generate_audio(text_prompt1,
                history_prompt="en_speaker_6")
# play text in notebook
Audio(speech_array1, rate=SAMPLE_RATE)
import scipy
scipy.io.wavfile.write("bark_out1.wav", rate=SAMPLE_RATE,data=speech_array1)

text_prompt2 = """
woman: Hi Shakira ,how are you?
"""
speech_array2 = generate_audio(text_prompt2)
# play text in notebook
Audio(speech_array2, rate=SAMPLE_RATE)
