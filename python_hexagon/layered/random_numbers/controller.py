import random
from pydantic import BaseModel
from python_hexagon.layered.random_numbers.model import RandomNumbersModel


class GenerateRandomNumbersController(BaseModel):
    model: RandomNumbersModel

    def execute(self):
        return [random.randint(self.model.min, self.model.max) for _ in range(self.model.set_cardinality)]
    