import math
import re

from exnihilo.extract.preprocess import preprocess
from exnihilo.extract.preprocess.preprocess import stop_words, lemmatizer


def sentence_importance(sentence, sentences):
    sentence_score = 0
    sentence = preprocess.remove_special_characters(str(sentence))
    sentence = re.sub(r'\d+', '', sentence)
    pos_tagged_sentence = preprocess.pos_tagging(sentence)
    for word in pos_tagged_sentence:
        if word.lower() not in stop_words and word not in stop_words and len(word) > 1:
            word = word.lower()
            word = lemmatizer.lemmatize(word)
            sentence_score = sentence_score + word_tfidf(word, sentences, sentence)

    return sentence_score


def freq(words):
    words = [word.lower() for word in words]
    dict_freq = {}
    words_unique = []
    for word in words:
        if word not in words_unique:
            words_unique.append(word)
    for word in words_unique:
        dict_freq[word] = words.count(word)

    return dict_freq


def word_tfidf(word, sentences, sentence):
    tf = tf_score(word, sentence)
    idf = idf_score(len(sentences), word, sentences)
    tf_idf = tf_idf_score(tf, idf)

    return tf_idf


def tf_idf_score(tf, idf):
    return tf * idf


def tf_score(word, sentence):
    """
    Formula:
    Number of times term w appears in a document) / (Total number of terms in the document).
    """
    word_frequency_in_sentence = 0
    len_sentence = len(sentence)
    for word_in_sentence in sentence.split():
        if word == word_in_sentence:
            word_frequency_in_sentence = word_frequency_in_sentence + 1
    tf = word_frequency_in_sentence / len_sentence

    return tf


def idf_score(no_of_sentences, word, sentences):
    """
    Formula:
    log_e(Total number of documents / Number of documents with term w in it)
    """
    no_of_sentence_containing_word = 0
    for sentence in sentences:
        sentence = preprocess.remove_special_characters(str(sentence))
        sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.split()
        sentence = [word for word in sentence if word.lower() not in stop_words and len(word) > 1]
        sentence = [word.lower() for word in sentence]
        sentence = [lemmatizer.lemmatize(word) for word in sentence]
        if word in sentence:
            no_of_sentence_containing_word = no_of_sentence_containing_word + 1
    idf = math.log10(no_of_sentences / no_of_sentence_containing_word)

    return idf
