from paddleocr import PaddleOCR

# import OCR class
from src.services.OCR.OCR import OCR

# PADDLEOCR class extends the OCR class
class PADDLEOCR(OCR):
    def __init__(self, lang="fr"):
        # Download the pretrained model
        self.model = PaddleOCR(use_angle_cls=True, lang=lang)

    # predict method
    # param: image
    # return: string
    def predict(self, image):
        # Get the prediction from the model
        result = self.model.ocr(image, cls=True)
        # get an array of all the predictions words (only the tuples (word, probability)))
        words = []
        for res in result:
            for line in res:
                word = line[1][0]
                probability = round(line[1][1] * 100, 2)
                print(f'PREDICTION : {word} =============> {probability} %')
                words.append((word))

        # join all the words into a string
        prediction = " ".join(words)
        return prediction