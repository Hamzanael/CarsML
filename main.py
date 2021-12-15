import random
from typing import List

import joblib
import numpy
import uvicorn
from fastapi import FastAPI, Form
from starlette.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles

from normalizers import *

FAVICON_PATH = 'static/favicon/favicon.png'

app = FastAPI(
    title='CarsML',
    description='Car price prediction API.',
)


def get_car_name(car_make: str, car_model: str) -> str:
    return car_make.strip().lower() + ' ' + car_model.strip().lower()


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)


@app.get('/models', response_class=JSONResponse)
async def models():
    return models_json


@app.post('/search', response_model=int)
async def search(car_make: str = Form(...),
                 car_model: str = Form(...),
                 car_kilometers: int = Form(..., ge=0),
                 car_color: str = Form(...),
                 car_year: int = Form(..., ge=1950, lt=2022),
                 car_trans: str = Form(...),
                 options: List[str] = Form(None)):
    if options is None:
        options = []
    car_name = get_car_name(car_make, car_model)
    car_name = normalize_car_name(car_name)
    car_color = normalize_car_color(car_color)
    car_trans = normalize_car_transmission(car_trans)
    options = normalize_options(options)

    # print(car_name, car_kilometers, car_color, car_year, car_trans)
    # print(options)

    arr = car_name + car_color + car_trans + [car_kilometers] + [car_year] + options
    arr = numpy.array(arr).reshape((-1, len(arr)))
    # print(arr)

    return model.predict(arr)


app.mount("/", StaticFiles(directory="static", html=True), name="static")


def get_models():
    all_cars: list[str] = normalize_car_name.rows
    make_to_models = {}
    for car in all_cars:
        first_space = car.index(' ')
        car_make, car_model = car[:first_space], car[first_space + 1:]
        car_make = car_make.title()
        car_model = car_model.title()
        make_to_models.setdefault(car_make, []).append(car_model)

    return JSONResponse(make_to_models)


models_json = get_models()
model = joblib.load('res/random_forest.joblib')

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
