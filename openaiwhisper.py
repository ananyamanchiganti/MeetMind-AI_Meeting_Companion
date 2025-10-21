import whisper
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
model = whisper.load_model("base")
file = "1minspeech.mp3"
result = model.transcribe(file)
sentences = sent_tokenize(result["text"])
print(result["text"])
print("LIST OF SENTENCES")
print(sentences)
chunks = []