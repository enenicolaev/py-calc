from typing import Dict, Any

# TODO add interface for dictionary
# class CommandI:
#     argsNumber: int
#     def command(self, args: Any) -> float:
#         pass
#
# commandI = Dict[str, CommandI]

import enum


@enum.unique
class CommandsEnum(enum.Enum):
    plus = 'plus'
    minus = 'minus'
    multiple = 'multiple'
    division = 'division'


commandsEnum = {
    'plus': CommandsEnum.plus.value,
    'minus': CommandsEnum.minus.value,
    'multiple': CommandsEnum.multiple.value,
    'division': CommandsEnum.division.value,
}

calcCommands = {
    commandsEnum['plus']: {
        'argsNumber': 2,
        'command': lambda x, y: x + y,
    },
    commandsEnum['minus']: {
        'argsNumber': 2,
        'command': lambda x, y: x - y,
    },
    commandsEnum['multiple']: {
        'argsNumber': 2,
        'command': lambda x, y: x * y,
    },
    commandsEnum['division']: {
        'argsNumber': 2,
        'command': lambda x, y: x / y,
    }
}
