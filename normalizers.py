import functools
from typing import List, Callable, Any, Annotated

# __all__ = [name for name, attr in globals().items() if name.startswith('normalize_') and isinstance(attr, Callable)]
__all__ = [
    'normalize_car_name',
    'normalize_car_color',
    'normalize_car_trans',
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
    'red',
    'blue',
]


def normalized(endpoint: Annotated[Any, Any]) -> Callable:
    normalizers = {}

    for field in endpoint.__annotations__:
        ...

    @functools.wraps(endpoint)
    def inner(*args, **kwargs):
        ...

    return inner


def normalize(field, accepted) -> List[bool]:
    # raises ValueError if the color doesn't exist
    field_index = CAR_COLORS.index(field)
    norm = [False] * len(accepted)
    norm[field_index] = True
    return norm


def normalize_car_name(car_name: str) -> List[bool]:
    ...


def normalize_car_color(car_color: str) -> List[bool]:
    return normalize(car_color, CAR_COLORS)


def normalize_car_trans(car_trans: str) -> List[bool]:
    return normalize(car_trans, CAR_TRANSMISSIONS)


def normalize_options(options: List[str]) -> List[bool]:
    options = [option.lower() for option in options]
    return [True if option in options else False for option in OPTIONS_TITLES]
