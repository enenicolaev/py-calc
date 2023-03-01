from collections.abc import Callable
from typing import List

ArgsType = List[float]


class Command:
    __roundLength = 6

    def __init__(self, command: Callable[[List[float]], float]):
        self.__command = command

    def execute(self, *args: ArgsType) -> float:
        return self.__round(self.__command(*args))

    def __round(self, value: float) -> float:
        return round(value, self.__roundLength)


# TODO test code to remove
operation = Command(lambda a, b, c: a+b+c)

operation.execute(2, 3, 4)
