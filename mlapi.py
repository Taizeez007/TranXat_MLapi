from urllib import request
from pydantic import BaseModel
import pickle
import pandas as pd
import requests
from Model import model
import uvicorn
import api_key_utils
import os
import json
from typing import Optional
from fastapi import FastAPI, Header, HTTPException, status
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from test_transaction import responder 

baseurl="https://www.databaseserver.com/api/datainfo" 
"""url of server where data is to be extracted accessible to
user to manage storage"""


endpoint="user" #endpoint from which data is to extracted


app=FastAPI()

def mainurl(baseurl, endpoint):
    r=requests.get(baseurl + endpoint)
    return r.json()

import base64
#value of data in json is extracted
data= mainurl(baseurl, endpoint)

'''def  img_decode(data):
    file= open('data','rb')
    byte=file.read()
    file.close()
    decode_img=open('data','wb')
    img_dec=decode_img.write(base64.b64decode((byte)))
    img_dec.close()

    return img_dec '''
#save captured pic, encode and save on storage. train model to update


@app.get("/")
async def home(name: str):
    return {"message": f"Hello! {name}"}
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


#image saved to local storage during capture is decoded and jsonify
path="https://www.databaseserver.com/api/datainfo/images" 

def extract_img():
    with open("image_files","rb") as file:
        data_n=file.read()
        en_data=base64.b64encode(data_n)
    return en_data.json()

new_img= extract_img()

#updates image database to train model
@app.post('/update_img')
async def img_update():
    headers={
        "Content-Type": "application/json"
    }
    response= requests.post(f"{baseurl}/image",
    data=json.dumps(new_img), headers=headers)




class paramInput(BaseModel):
    'img':str

from Model import model_pkl

#webhook and api key creation
if responder.response==200:
    with open('Model.py','rb') as trainM:
        model=pickle.load(trainM)

@app.post('/')
async def mainModel(item:paramInput):
    try:
        df=pd.DataFrame([item.dict().values], columns=item.dict().keys())
        pred=model.predict(df)
        while True:
            responses='information verified! continue'
    except Exception as e:
            responses="Error try again or quit"

     
    return {responses}

#check pip freeze >requirements.txt after first line of procfile



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="127.0.0.1", 
        port=8000,
        # ssl_keyfile= Path(__file__).absolute().parents[0] / 'localhost.key',
        # ssl_certfile= Path(__file__).absolute().parents[0] / 'localhost.crt'
    )