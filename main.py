import random
from typing import List

import uvicorn
from fastapi import FastAPI, Form
from starlette.staticfiles import StaticFiles

from normalizers import *

app = FastAPI(
    title='CarsML',
    description='Car price prediction API.',
)


def get_car_name(car_make: str, car_model: str) -> str:
    return car_make.strip().lower() + ' ' + car_model.strip().lower()


@app.post('/search', response_model=int)
async def search(car_make: str = Form(...),
                 car_model: str = Form(...),
                 car_kilometers: int = Form(..., ge=0),
                 car_color: str = Form(...),
                 car_year: int = Form(..., ge=1950, lt=2022),
                 car_trans: str = Form(...),
                 options: List[str] = Form([])):
    car_name = get_car_name(car_make, car_model)
    car_name = normalize_car_name(car_name)
    car_color = normalize_car_color(car_color)
    car_trans = normalize_car_trans(car_trans)
    options = normalize_options(options)

    print(car_name, car_kilometers, car_color, car_year, car_trans)
    print(options)

    return random.randint(1, 1000)


app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == '__main__':
    uvicorn.run(app, port=5000)
