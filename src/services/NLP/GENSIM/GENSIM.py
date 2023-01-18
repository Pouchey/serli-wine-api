# gensim NLP

from gensim.models import Word2Vec
from keras.preprocessing.text import text_to_word_sequence
import pandas as pd
import numpy as np

# import NLP class
from src.services.NLP.NLP import NLP


# GENSIM class extends the NLP class
class GENSIM(NLP):
    def __init__(self, model_path = "../../models/gensim.model", data_path = "../../data/data.csv"):
        # call the super class constructor
        super().__init__(model_path, data_path)
        self.tokenized_data = []

        if data_path is not None:
            self.tokenize_data()

    # load a model method
    # param: path
    # return: model
    def load_model(self, path):
        self.debug("[INFO] loading model from path:", path, "...")
        # load the model
        model = Word2Vec.load(path)
        return model

    # method to predict the text
    # param: string
    # return: string[]
    def predict(self, text):
        self.debug("[INFO] predicting texts:", text, "...")
        try:

            # tokenize the text
            tokenized_text = text_to_word_sequence(text)

            # Find the sentence embedding for the text if the word is in the vocabulary
            text_embedding = np.mean([self.model.wv[word] for word in tokenized_text if word in self.model.wv.index_to_key], axis=0)

            # Find the sentence embedding for each sentence in the corpus
            data_embeddings = np.array([np.mean([self.model.wv[word] for word in sentence], axis=0) for sentence in self.tokenized_data])

            # Find the cosine similarity between the text embedding and each sentence in the corpus
            cosine_similarities = np.array([np.dot(text_embedding, data_embedding) / (np.linalg.norm(text_embedding) * np.linalg.norm(data_embedding)) for data_embedding in data_embeddings])


            # Find the 4 most similar sentences with a percentage similarity
            result = []
            for index in np.argsort(cosine_similarities)[-4:]:
                self.debug(round(cosine_similarities[index] * 100, 2), "% ===>", self.data[index])
                result.append([self.data[index], round(cosine_similarities[index] * 100, 2)])

            return result




        except Exception as e:
            print(e)
            print('No similar sentence found')
            return []


    def tokenize_data(self):
        # tokenize the data
        self.debug("[INFO] tokenizing data...")
        self.tokenized_data = [text_to_word_sequence(sentence) for sentence in self.data]

