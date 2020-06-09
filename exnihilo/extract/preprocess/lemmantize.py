from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


def lemmatize_words(words):
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))

    return lemmatized_words


def get_lemmatizer():
    return lemmatizer if lemmatizer is not None else WordNetLemmatizer()
