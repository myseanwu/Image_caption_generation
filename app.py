"""The basic workflow includes"""

# Import Packages
# Create Our Route (/predict)
# Load our Models and Vectorizer
# Receive Input From Endpoint
# Vectorize the data/name
# Make our predictions
# Send Result as JSON

# FastApi
import uvicorn
from fastapi import FastAPI,Query, Request, Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from enum import Enum

# ML 
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import random
import os
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf

# MongoDB

# client = pymongo.MongoClient("mongodb+srv://Sean:Quanta1106@cluster0-lhcgy.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.test


# Models 

from coco_project import evaluate, predict_url, main_predict, img_name_val




# init app and templates
app = FastAPI()
templates = Jinja2Templates(directory='templates')

# post
class Item(BaseModel):
    name: str


# Routes
@app.get('/')
async def index():
	return {"text":"Hello API Masters, Seann"}

@app.get('/items/')
async def get_items(name:str = Query(None,min_length=2,max_length=7)):
	return {"name":name}


@app.get("/prediction/")
async def read_item(request: Request, prediction_url = None):
    """predict image caption"""
    result = ''

    if prediction_url is None:
        image_url = 'http://t2.gstatic.com/images?q=tbn:ANd9GcTFuo4YroGo0Ijds5JJKsLBVGKjbi338vzHx1qDXn4DyqUewRWYt2cUETAJtMlTjANaRb1o0vSgRzfsL8DJ2eQ'
        image_extension = image_url[-4:]
        image_path = tf.keras.utils.get_file('image1'+image_extension,
                                        origin=image_url)
        # result, attention_plot = evaluate(image_path)
        # result.remove('<end>')

    else:
        image_url = str(prediction_url)

        image_extension = image_url[-4:]
        image_path = tf.keras.utils.get_file('image'+image_extension,
                                        origin=image_url)

    result, attention_plot = evaluate(image_path)
    if '<end>' in result:
        result.remove('<end>')

    # return {'Image:',"Prediction caption": result}
    return templates.TemplateResponse('prediction.html',{
        'request': request,
        'image_url': image_url ,
        # 'image_url_2': url_2 ,
        "prediction_caption": result,
        # "prediction_caption_2": result_2
    })

@app.post("/url/")
async def create_url(url_request: Item):
    """post url"""
    return {'url': Item}



# ML Aspect


# Using Post
@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == '__main__':
	uvicorn.run('app:app',host="127.0.0.1",port=8000, reload=True)




