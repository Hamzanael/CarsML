from typing import List

import pandas as pb
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# __all__ = [name for name, attr in globals().items() if name.startswith('normalize_') and isinstance(attr, Callable)]
__all__ = [
    'normalize_car_name',
    'normalize_car_color',
    'normalize_car_transmission',
    'normalize_options',
]

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

OPTIONS_TITLES = [title.lower().strip() for title in OPTIONS_TITLES]

CAR_TRANSMISSIONS = [
    'automatic',
    'manual',
]

CAR_COLORS = [
    'black',
    'blue',
    'gold',
    'grey',
    'red',
    'silver',
    'white',
]

xs = {
    'x0': 'name',
    'x1': 'kilometers',
    'x2': 'color',
    'x3': 'year',
    'x4': 'transmission',
    'x5 - x17': 'options',
}

xss = {
    'car_name': 'x0',
    'car_color': 'x2',
    'car_transmission': 'x4'
}


def load_rows():
    dataset = pb.read_csv('res/FinalData.csv')
    x = dataset.iloc[:, :-1].values
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 2, 4])], remainder='passthrough',
                           verbose_feature_names_out=False)

    ct.fit_transform(x)
    rows: list[str] = ct.get_feature_names_out()
    row_types = {}
    for row_name in rows:
        if '_' in row_name:
            first_underscore = row_name.index('_')
            row_type, row = row_name[: first_underscore], row_name[first_underscore + 1:]
            row_types.setdefault(row_type, []).append(row)
        else:
            row_types[row_name] = []

    return row_types


row_types = load_rows()


class FieldNormalizer:
    def __init__(self, field_name: str, required=True):
        self.name = field_name
        self.rows = [row.lower() for row in row_types[xss[field_name]]]
        self.required = required

    def normalize(self, value: str):
        value = value.lower()
        norm = [value == row_name for row_name in self.rows]
        if self.required and not any(norm):
            raise ValueError()
        return norm

    def __call__(self, value: str):
        return self.normalize(value)


normalize_car_name = FieldNormalizer('car_name')
normalize_car_transmission = FieldNormalizer('car_transmission')
normalize_car_color = FieldNormalizer('car_color')


def normalize(field, accepted) -> List[bool]:
    # raises ValueError if the color doesn't exist
    field_index = accepted.index(field)
    norm = [False] * len(accepted)
    norm[field_index] = True
    return norm


def normalize_options(options: List[str]) -> List[bool]:
    options = [option.lower() for option in options]
    return [option in options for option in OPTIONS_TITLES]
