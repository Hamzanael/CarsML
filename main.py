import random
from typing import List

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI(
    title='PROJECT',
    description='DESCRIPTION',
)

options_title = [
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

for title in options_title:
    print(f'''
        <div style = "float: left">
            <input class="form-check-input" style="margin-left:1rem" type="checkbox" value="{title}">
            <label class="form-label">{title}</label>   
        </div>
    ''')
    # print(f'<input class="form-check-input" style="margin-left:1rem" type="checkbox" value="{title}">')
    # print(f'<label class="form-label">{title}</label>')


def init(app: FastAPI):
    with open('index.html', mode='r', encoding='utf-8') as index_file:
        app.state.index = index_file.read()


init(app)


@app.post('/search', response_model=int)
async def search(car_name: str = Form(...),
                 car_kilometers: int = Form(...),
                 car_color: str = Form(...),
                 car_year: int = Form(...),
                 car_trans: str = Form(...),
                 options: List = Form(...)):
    options = [1 if option in options else 0 for option in options_title]
    print(car_name, car_kilometers, car_color, car_year, car_trans)
    print(options)
    return random.randint(1, 1000)


@app.get('/', response_class=HTMLResponse)
async def index():
    with open('index.html', mode='r', encoding='utf-8') as index_file:
        return index_file.read()
