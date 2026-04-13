import os
import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def process_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = word_tokenize(text)
    pos_tags = nltk.pos_tag(words)
    pos_dict = [{"word": word, "pos": pos} for word, pos in pos_tags]
    return pos_dict
