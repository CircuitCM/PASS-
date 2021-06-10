import os
from enum import Enum

from starlette.templating import Jinja2Templates
from fastapi import FastAPI, Request
import ApplyFuncs as af
import pandas as pd
import aiohttp
from fastapi import WebSocket
import asyncio as aio
import csv

app = FastAPI()
templates = Jinja2Templates(directory="html")

class dataSource(str, Enum):
    linkcsv = "linkcsv"
    csv = "csv"
    other = "other"


@app.on_event("startup")
async def startup():
    fp = __file__.replace('\\','/').replace('//','/')
    fp = fp[:fp.rfind('/')]
    os.chdir(fp)
    ddir= fp+'/Model Data/Results'
    if not os.path.exists(ddir):
        os.makedirs(ddir)

@app.get("/")
async def start(q: Request):
    return templates.TemplateResponse("Home.html",{'request':q,'data':'start,test,table\r\nblip,blop,bloop'})


@app.get("/login")
async def login(q: Request):

    return templates.TemplateResponse("Login.html",{'request':q})

@app.post("/train_model")
async def train_model():
    #implement where data comes from
    return {"message": "Hello World"}

@app.get('/new_results')
async def new_results(q: Request):
    #so link could be like http://127.0.0.1:8000/new_results/csv?path="path/to/csvfile"
    #for now I'm just cloning the input
    #af.results_from('https://docs.google.com/spreadsheets/d/1a6nel46Mk-wr8scatqAJJ9fdlUb8r2tZjVmwHd_BOCw/export?format=csv&gid=0')
    async with aiohttp.ClientSession() as session:
        gurl = 'https://docs.google.com/spreadsheets/d/1a6nel46Mk-wr8scatqAJJ9fdlUb8r2tZjVmwHd_BOCw/export?format=csv&gid=0'
        async with session.get(gurl) as resp:
            cs = await resp.read()
    cs = cs.decode('unicode_escape')
    print(cs)

    # if source == dataSource.csv:
    #     #open uploaded csv, get xG values
    #     pass
    # elif source == dataSource.linkcsv:
    #     #download csv first then do the operations
    #     pass
    # else:
    #     #other
    #     pass
    return templates.TemplateResponse("Home.html",{'request':q,'data':cs})