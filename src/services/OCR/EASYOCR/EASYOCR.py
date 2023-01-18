import cv2
import easyocr


# import OCR class
from src.services.OCR.OCR import OCR

class EASYOCR(OCR):
    def __init__(self):
        # Download the pretrained model
        self.model = easyocr.Reader(
            ['fr', 'en', 'it'], model_storage_directory='easyocr_models', verbose=False)

    # load image method
    # param: path
    # return: image
    def load_image(self, path):
        # Load the image
        image = cv2.imread(path)
        # Return the image
        return image

    # predict method
    # param: image
    # return: string
    def predict(self, image):
        return " ".join(self.model.readtext(image, detail=0))