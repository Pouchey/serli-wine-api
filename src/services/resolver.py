# from src.services.OCR.KERAS.KERAS import KERAS
from src.services.OCR.EASYOCR.EASYOCR import EASYOCR
# from src.services.NLP.GENSIM.GENSIM import GENSIM
from src.services.NLP.TFIDF.TFIDF import TFIDF
# import cv2


def resolveImage(image):
    # ocr = KERAS()
    ocr = EASYOCR()
    OCR_prediction = ocr.predict(image)

    # nlp = GENSIM(data_path="./ressources/external_data.csv", model_path="./src/services/models/gensim.model")
    nlp = TFIDF(data_path="./ressources/data_clean.csv")
    prediction = nlp.predict(OCR_prediction)

    print(prediction)
    res = []
    for pred in prediction:
        id = pred[0].split(",")[0]
        percentage = pred[1]
        res.append(id)

    return res
