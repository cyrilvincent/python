from fastapi import FastAPI
import uvicorn
import media
import services
import adapters
import dtos

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/detail/{id}")
def detail(id: int) -> dtos.MediaDetailDTO:
    service = services.CartService()
    m = service.detail(id)
    return adapters.MediaAdapter.to_detail_dto(m)

@app.get("/search/{q}")
def search(q: str) -> list[dtos.MediaDetailDTO]:
    service = services.CartService()
    medias = service.search(q)
    return [adapters.MediaAdapter.to_media_dto(m) for m in medias]





uvicorn.run(app, host="0.0.0.0")

# TP
# Effectuer 3 approches différentes
# 1/ detail qui retourne un dict
# 2/ Vos entities doivent hériter de pydantic
# 3/ Créer un DetailDTO id, title, price, publisher_name, [first_name, last_name]
     # Créer la class MediaAdapter avec la méthode to_dto(entity) -> dto
     # L'appeler depuis FastAPI



