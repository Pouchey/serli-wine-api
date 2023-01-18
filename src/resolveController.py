import numpy as np
import cv2

async def resolve(image):
  # Images is byte array
  # Convert to numpy array
  nparr = np.frombuffer(image, np.uint8)
  # Convert to image
  image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)



  return {
    "imageIds": [1,2,3,4]
  }
