#imports open ai whisper (open source code)
import whisper
#imports natural language toolkit tokenizer
from nltk.tokenize import sent_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
model = whisper.load_model("base")
#transcribing file
file = "1minspeech.mp3"
result = model.transcribe(file)
#result["text"] gives transcript as a string with proper punctuation
#tokenizes transcript into sentences
sentences = sent_tokenize(result["text"])
#creates transcript
transcript = result["text"]
print(transcript)
#code to sort transcript into list of 1800 char chunks for distilbert
chunks = []
max_chars = 1800
chunk = ""
current = 0
for sentence in sentences:
    if current + len(sentence) > max_chars:
        chunks.append(chunk.strip())
        chunk = ""
        current = 0
        while len(sentence) > max_chars:
            chunks.append(sentence[:max_chars])
            sentence = sentence[max_chars:]
    chunk += " " + sentence
    current += len(sentence)
if chunk.strip():
    chunks.append(chunk.strip())
print(chunks)