# from src.services.OCR.KERAS.KERAS import KERAS
from src.services.OCR.EASYOCR.EASYOCR import EASYOCR
from src.services.OCR.PADDLEOCR.PADDLEOCR import PADDLEOCR
from src.services.NLP.GENSIM.GENSIM import GENSIM
from src.services.NLP.TFIDF.TFIDF import TFIDF

def getOCR(name):
    # if name == "KERAS":
    #     return KERAS()
    if name == "EASYOCR":
        return EASYOCR()
    elif name == "PADDLEOCR":
        return PADDLEOCR()

def getNLP(name):
    if name == "GENSIM":
        return GENSIM(data_path="./ressources/data_clean.csv", model_path="./src/services/models/gensim.model")
    if name == "TFIDF":
        return TFIDF(data_path="./ressources/data_clean.csv")


def resolveImage(image):
    OCR = getOCR("PADDLEOCR")
    OCR_prediction = OCR.predict(image)
    
    NLP = getNLP("TFIDF")
    prediction = NLP.predict(OCR_prediction)

    print(prediction)
    res = []
    for pred in prediction:
        id = pred[0].split(",")[0]
        probability = pred[1]

        print(f'PREDICTION : {id} =============> {probability} %')

        res.append({
            "id": id,
            "probability": probability
        })

    return res
