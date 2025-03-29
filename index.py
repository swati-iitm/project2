from fastapi import FastAPI, File, Form, UploadFile
from pydantic import BaseModel
from sent_tranf import MatchQuestion
#from openai_embed import get_embeddings
import os
from functions import *
import json

app=FastAPI()

print ("This is Line 1")

class Item(BaseModel):
    print("Inside class item")
    name: str
    roll_no: int
    roe_marks: int


with open("question_mapper.json",'r') as f:
    question_mapper=json.load(f)
    print("Read question mapper")

sent = MatchQuestion()

@app.post("/sent-tranf")
def sent_tranf(question:str = Form(...), file:str = Form(...)):
    print(question)
    match=sent.match_question(question)
    print(match)
    response = globals()[question_mapper[match]](question, file)
    #return match
    return {"answer": response}
