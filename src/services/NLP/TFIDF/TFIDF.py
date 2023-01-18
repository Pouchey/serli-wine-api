from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# import NLP class
from src.services.NLP.NLP import NLP


class TFIDF(NLP):
    def __init__(self, model_path=None, data_path="../../data/data.csv"):
        # call the super class constructor
        super().__init__(model_path, data_path)
        self.values = []
        self.vectorizer = TfidfVectorizer(strip_accents='ascii')

        if data_path is not None:
            self.loadValues()
            self.vectorizer.fit(self.values)

    def predict(self, text):
        cosine = cosine_similarity(self.vectorizer.transform(
            [text]), self.vectorizer.transform(self.values)).flatten()

        result = []

        for index in cosine.argsort()[-4:][::-1]:
            self.debug(round(cosine[index] * 100, 2), "% ===>", self.data[index])
            result.append([self.data[index], round(cosine[index] * 100, 2)])

        return result

    def loadValues(self):
        self.debug("[INFO] loading values")

        for data in self.data:
            line = data.split(',')
            self.values.append(' '.join(line[1:]))
