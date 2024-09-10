import asyncio
from gino import Gino

from main import app

db = Gino()

DATABASE_URL = "postgresql://diane:dianePg19@localhost/authDB"

async def init_db(app):                # Connexion à la base de données
    await db.set_bind(DATABASE_URL)
    app.state.db = db

    await db.gino.create_all()      #creation des tables


async def close_db(app):               #fermer la connexion
    await db.pop_bind().close()


# asyncio.get_event_loop().run_until_complete(startup()) #risque de conflits avec fastapi
