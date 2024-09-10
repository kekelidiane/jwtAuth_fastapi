from fastapi import FastAPI

from database import init_db, close_db


app = FastAPI(
    title="Json Web Token Authentication",
    summary="-----"
)

@app.lifespan("startup")        #appel de l'initialisation de la base de données
async def startup(): 
    await init_db(app)

@app.lifespan("shutdown")       #appel de la fermerture de la connexion
async def shutdown():
    await close_db(app)