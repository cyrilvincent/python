from fastapi import FastAPI
from factory import Db
import services
from adapters import Adapter
import dtos

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/cart")
def cart():
    pass

@app.get("/media/{id}")
def media(id:int):
    session = Db.context().get_session()
    service = services.ManageCartService(session)
    media = service.get_detail(id)
    dto = Adapter.from_media_to_media_detail_dto(media)
    return dto

@app.post("/media")
def add_media(media:dtos.MediaDTO):
    # todo
    pass


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000)

