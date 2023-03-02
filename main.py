from calc.data.data import calcCommands, commandsEnum
from calc.models import Command

# a = CalcSymbol('Test')

# value1 = float(input('Введите значение a'))
# value2 = float(input('Введите значение b'))

# print(Command(accumulate).execute(value1, value2))
#
# print(Command(subtraction).execute(value1, value2))

class Calculator:
    __commands = calcCommands

    def calc(self, command: commandsEnum):
        commandData = self.__commands[command]
        print(commandData)
        return commandData['command']


calculator = Calculator()
res = calculator.calc(commandsEnum['plus'])(4, 10)
print(res)