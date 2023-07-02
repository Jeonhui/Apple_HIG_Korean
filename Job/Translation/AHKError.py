from enum import Enum

class AHKError(Enum):
    FileNotFoundError = -1
    OverCapacityError = 0
    ResponseError = 1