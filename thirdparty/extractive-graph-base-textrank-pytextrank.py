import pytextrank
import spacy

from exnihilo import data

text = data.read_from_file("../input.txt")

nlp = spacy.load("en_core_web_sm")
tr = pytextrank.TextRank()
tr.load_stopwords(path="stop.json")
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
doc = nlp(text)

print("Summary:")
for sent in doc._.textrank.summary(limit_phrases=15, limit_sentences=3):
    print(sent, end=" ")
