import random
from typing import List, Callable

import uvicorn
from fastapi import FastAPI, Form, params
from fastapi.responses import HTMLResponse

OPTIONS_TITLES = [
    'ABS',
    'Xenon Light',
    'Leather Seats',
    'Touch Screen',
    'Navigation System',
    'Led Lights',
    'Sunroof',
    'Heated Seats',
    'Bluetooth',
    'Electric mirrors',
    'Cruise Control',
    'Rear camera',
    'Parking sensors',
]

CAR_TRANSMISSIONS = [
    'automatic',
    'manual',
]

CAR_COLORS = [
    'red',
    'blue',
]

app = FastAPI(
    title='PROJECT',
    description='DESCRIPTION',
)


# class CheckedForm(params.Form):
#     def __init__(self, checker: Callable, *args, **kwargs):
#         self.checker


def init(app: FastAPI):
    with open('index.html', mode='r', encoding='utf-8') as index_file:
        app.state.index = index_file.read()


def normalize_options(options):
    options = [option.lower() for option in options]
    return [1 if option.lower() in options else 0 for option in OPTIONS_TITLES]


@app.get('/', response_class=HTMLResponse)
async def index():
    with open('index.html', mode='r', encoding='utf-8') as index_file:
        return index_file.read()


@app.post('/search', response_model=int)
async def search(car_name: str = Form(...),
                 car_kilometers: int = Form(..., ge=0),
                 car_color: str = Form(...),
                 car_year: int = Form(..., ge=1950, lt=2022),
                 car_trans: str = Form(...),
                 options: List[str] = Form([])):
    print(options)
    options = normalize_options(options)
    # logging.info([car_name, car_kilometers, car_color, car_year, car_trans])
    print(car_name, car_kilometers, car_color, car_year, car_trans)
    # logging.info(options)
    print(options)
    return random.randint(1, 1000)


init(app)
if __name__ == '__main__':
    uvicorn.run(app)
