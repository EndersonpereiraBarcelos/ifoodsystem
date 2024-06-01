from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
      <head>
        <title>Ifood Clone</title>
      </head>
      <body>
        <h1> A Melhor lanchonete da sua região</h1>
        <ul> a</ul>
      </body>
    </html>"""


@app.get('/a', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""