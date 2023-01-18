import numpy as np
import cv2
from src.services.resolver import resolveImage

async def resolve(image):
  # Images is byte array
  # Convert to numpy array
  nparr = np.frombuffer(image, np.uint8)
  # Convert to image
  image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

  res = resolveImage(image)

  # get ids array
  ids = [r["id"] for r in res]
  # get probabilities array
  probabilities = [r["probability"] for r in res]

  print("ids: ", ids)
  print("probabilities: ", probabilities)

  return {
    "imageIds": ids,
    # "probabilities": probabilities
  }
