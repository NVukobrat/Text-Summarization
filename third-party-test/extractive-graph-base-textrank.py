from gensim.summarization.summarizer import summarize

from exnihilo import data

text = data.read_from_file("../input.txt")

print(summarize(text=text, ratio=0.15, word_count=None, split=False))
