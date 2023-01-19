import io
from fastapi.responses import StreamingResponse
import cv2
import os


def imageToBytes(image):
    _, buffer = cv2.imencode('.jpg', image)
    byte_im = buffer.tobytes()
    io_buffer = io.BytesIO(byte_im)
    return io_buffer


def sendImage(image):
    buffer = imageToBytes(image)
    res = StreamingResponse(buffer, media_type="image/jpeg")
    return res


def getImage(id):
    path = 'ressources/external_data/' + str(id) + '/'

    try:
        files = os.listdir(path)
        path = path + files[0]
        image = cv2.imread(path)
    except:
        image = None

    return image
