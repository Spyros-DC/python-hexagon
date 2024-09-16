from python_hexagon.layered.random_numbers.controller import GenerateRandomNumbersController
from python_hexagon.layered.random_numbers.model import RandomNumbersModel


def test_generate_random_numbers_controller():
    controller = GenerateRandomNumbersController(model=RandomNumbersModel(min=1, max=10, set_cardinality=5))
    assert len(controller.execute()) == 5
    assert min(controller.execute()) >= 1
    assert max(controller.execute()) <= 10
