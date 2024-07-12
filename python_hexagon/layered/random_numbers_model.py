from pydantic import BaseModel


class RandomNumbersModel(BaseModel):
    min: int
    max: int
    set_cardinality: int
