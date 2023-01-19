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
        print("=====================================================================")
        print("PADDLEOCR prediction: ", result)
        # get an array of all the predictions words (only the tuples (word, probability)))

        words = []
        for res in result:
            for line in res:
                word = line[1][0]
                probability = round(line[1][1] * 100, 2)
                print(f'PREDICTION : {word} =============> {probability} %')
                words.append((word))

        # get an array of all the predictions words (only the words)
        print("=====================================================================")
        print("PADDLEOCR words: ", words)

        # join all the words into a string
        prediction = " ".join(words)

        return prediction

        # predictions
        # #predictions = [prediction[1][0] for prediction in result]
        # predictions = []
        # print("=====================================================================")
        # print("PADDLEOCR prediction: ", predictions)
        # # join all the words into a string
        # prediction = " ".join(predictions)
        # return prediction
