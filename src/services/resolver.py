from src.services.OCR.KERAS.KERAS import KERAS
from src.services.NLP.GENSIM.GENSIM import GENSIM
# import cv2

def resolveImage(image):
    keras = KERAS()
    OCR_prediction = keras.predict(image)
    
    gensim = GENSIM(data_path="./ressources/external_data.csv", model_path="./src/services/models/gensim.model")

    prediction = gensim.predict(OCR_prediction)

    print(prediction)
    res = []
    for pred in prediction:
        id = pred[0].split(",")[0]
        res.append(id)

    return res

