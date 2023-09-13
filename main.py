from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

dummy_data = [
    {
        "boundingBox": {
            "boundingBoxes": [
                {
                    "height": 2832,
                    "label": "bird",
                    "left": 681,
                    "top": 599,
                    "width": 1364
                }
            ],
            "inputImageProperties": {
                "height": 3726,
                "width": 2662
            }
        }
    }
]

@app.get("/")
async def home():
    return {
        "Hello world"
    }

@app.get("/empty_array", response_model=List[Dict])
async def get_empty_array():
    return dummy_data

