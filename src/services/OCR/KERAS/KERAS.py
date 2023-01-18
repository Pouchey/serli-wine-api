import keras_ocr

#import OCR class
from src.services.OCR.OCR import OCR


# KERAS class extends the OCR class
class KERAS(OCR):
    def __init__(self):
        # Download the pretrained model
        self.model = keras_ocr.pipeline.Pipeline()

    # load image method
    # param: path
    # return: image
    def load_image(self, path):
        # Load the image
        image = keras_ocr.tools.read(path)
        # Return the image
        return image

    # predict method
    # param: image
    # return: string
    def predict(self, image):
        # Get the prediction from the model
        prediction_groups = self.model.recognize([image])
        # get an array of all the predictions words
        predictions = [prediction for group in prediction_groups for prediction in group]
        # get the text from the predictions
        prediction = [prediction[0] for prediction in predictions]
        # join all the words into a string
        prediction = " ".join(prediction)
        return prediction




