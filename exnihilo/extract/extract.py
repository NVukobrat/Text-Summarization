import operator
import re

from nltk.tokenize import sent_tokenize, word_tokenize

from exnihilo import data
from exnihilo import preprocess
from exnihilo import score
from exnihilo import stop_words

text = data.read_from_file("../../input.txt")

tokenized_sentence = sent_tokenize(text)
text = preprocess.remove_special_characters(str(text))
text = re.sub(r'\d+', '', text)

tokenized_words_with_stopwords = word_tokenize(text)
tokenized_words = [word for word in tokenized_words_with_stopwords if word not in stop_words]
tokenized_words = [word for word in tokenized_words if len(word) > 1]
tokenized_words = [word.lower() for word in tokenized_words]

tokenized_words = preprocess.lemmatize_words(tokenized_words)

input_user = int(input('Percentage of information to retain(in percent):'))
no_of_sentences = int((input_user * len(tokenized_sentence)) / 100)
print(no_of_sentences)
c = 1
sentence_with_importance = {}
for sent in tokenized_sentence:
    sentenceimp = score.sentence_importance(sent, tokenized_sentence)
    sentence_with_importance[c] = sentenceimp
    c = c + 1
sentence_with_importance = sorted(sentence_with_importance.items(), key=operator.itemgetter(1), reverse=True)
cnt = 0
summary = []
sentence_no = []
for word_prob in sentence_with_importance:
    if cnt < no_of_sentences:
        sentence_no.append(word_prob[0])
        cnt = cnt + 1
    else:
        break
sentence_no.sort()
cnt = 1
for sentence in tokenized_sentence:
    if cnt in sentence_no:
        summary.append(sentence)
    cnt = cnt + 1
summary = " ".join(summary)
print("\n")
print("Summary:")
print(summary)
outF = open('summary.txt', "w")
outF.write(summary)
