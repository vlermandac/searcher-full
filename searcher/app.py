from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from main import Main

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
)


@app.post("/submit")
async def submit(user_query: Annotated[str, Form()]):
    main = Main()
    rag, ids = main.run("--RAG", query=user_query)
    items = {"rag": rag,
             "ids": ids}
    return items
