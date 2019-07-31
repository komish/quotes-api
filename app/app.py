import os
import sys

import models as mod

from datetime import datetime  
from fastapi import FastAPI, Header
from sqlalchemy import (
    create_engine, asc, update
)
from datetime import datetime
from random import randint
from pydantic import BaseModel
from starlette.responses import JSONResponse

# set application metadata until a better 
# location for it presents itself.
app_name = "Quotes API"
app_version = "v0.1"

# initialize the application.
app = FastAPI()

# connection information to the backend.
DB_HOST = os.environ.get('DB_HOST')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')

# set an admin token to enable the POST api
# to /quotes in order to add entries.
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN')

# currently we assume mysqlclient (MySQLdb) driver which is 
# the default for sqlalchemy when using the mysql dialect.
# TODO: make this configurable
conn_string = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(conn_string)

table_creation, err = mod.create_tables(engine, mod.metadata)
if not table_creation:
    print(f"Ran into an error creating tables: {err}")
    sys.exit(4)

# We need to grab the Table object
# to interact with it.
quotes = mod.quotes

# We need to define a BaseModel for Pydantic, which
# will be used by the POST API call to define the
# object we accept via the data.
class Quote(BaseModel):
    msg: str
    src: str
    src_mat: str = None
    contrib: str = None
    contrib_link: str = None

@app.get("/")
async def root():
    return {
        "msg": "Thanks for using the Quotes API. Contribute via the repository.",
        "repository": "https://github.com/komish/quotes-api
            }

@app.get("/version")
async def get_version():
    return {"api_name": app_name,
            "api_version": app_version}

@app.get("/quote")
async def get_quote():
    with engine.connect() as conn:
        q = quotes.select().order_by(
            asc(quotes.c.uses)).limit(10)
        p = conn.execute(q)
        r = p.fetchall()
        ind = randint(0, len(r)-1)
        sel = r[ind]
        incr = sel['uses'] + 1
        u = update(quotes).where(quotes.c.id == sel['id']).values(uses = incr)
        upd = conn.execute(u)
    
    return sel

@app.post("/quote", status_code=201)
async def create_quote(quote: Quote, admin_token: str = Header(None)):
    if not ADMIN_TOKEN:
        return JSONResponse(status_code=405,
                content={"msg": "Quote creation is disabled."})
    if admin_token != ADMIN_TOKEN :
        return JSONResponse(status_code=401, 
                content={"msg": 
                "Unauthorized for this endpoint."})
    
    new = quotes.insert().values(
        created_at = datetime.now(),
        msg = quote.msg,
        source = quote.src,
        source_material = quote.src_mat,
        contributor = quote.contrib,
        contribution_method = quote.contrib_link,
        uses = 0
    )

    data = new.compile().params
    with engine.connect() as conn:
        r = conn.execute(new)

    return {'msg': 'success', 
            'inserted_id': r.inserted_primary_key[0], 
            'data': data}

@app.get("/alive", status_code=200)
async def liveness():
    # TODO Implement logic here
    return {"msg": "ok"}

@app.get("/ready", status_code=200)
async def ready():
    # TODO Implement logic here
    return {"msg": "ready"}
