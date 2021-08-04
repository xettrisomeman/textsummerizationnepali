import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re


def get_summarized_text(text):

    sentences = re.split('।', text)

    tfidf = TfidfVectorizer()

    words_tfidf = tfidf.fit_transform(sentences)

    num_sentences = 5

    sentence_sum = words_tfidf.sum(axis=1)

    important_sentences = np.argsort(sentence_sum, axis=0)[::-1]

    return get_text(num_sentences, sentences, important_sentences)




def get_text(num_sentences, sentences, important_sentences):
    full_sentence = ' '
    for i in range(0, len(sentences)):
        if i in important_sentences[:num_sentences]:
            full_sentence += sentence[i] + '।'
    return full_sentence

