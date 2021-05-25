from enum import Enum
from fastapi import FastAPI
from fastapi import WebSocket
import asyncio as aio

app = FastAPI()

class dataSource(str, Enum):
    linkcsv = "linkcsv"
    csv = "csv"
    other = "other"

@app.post("/train_model")
async def train_model(cvs):
    #
    #
    #
    return {"message": "Hello World"}

@app.get('/new_results/{uid}/{source}')
async def new_results(uid: str,source: dataSource,path: str):
    #so link could be like http://127.0.0.1:8000/new_results/csv?path="path/to/csvfile"
    if source == dataSource.csv:
        #open uploaded csv, get xG values
        pass
    elif source == dataSource.linkcsv:
        #download csv first then do the operations
        pass
    else:
        #other
        pass
    return {'results_xG': 'data you want, could be updated html file or json'}