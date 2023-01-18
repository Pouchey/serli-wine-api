from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from src.wineController import getWine,searchWine
from src.imageController import getImage, sendImage

from src.resolveController import resolve

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:4173",
    "http://localhost:8080",
    "http://serli-wine-app.cleverapps.io",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/resolve")
async def resolver(
  image: UploadFile = File()
  ):
  reqImage = await image.read()
  res = await resolve(reqImage)
  return res

@app.get("/api/wines/{id}")
async def get_wine(id: int):
  wine = getWine(id)
  return wine

@app.get("/api/wines/{id}/image")
async def get_image(id: int):
  image = getImage(id)
  return sendImage(image)

#search with query
@app.get("/api/search")
async def get_wine(q: str):
  wine = searchWine(q)
  return wine


  

# Configuring the server host and port
if __name__ == '__main__':
  uvicorn.run(app, port=8080)