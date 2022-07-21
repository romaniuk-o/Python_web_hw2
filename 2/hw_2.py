from abc import ABC, abstractmethod, ABCMeta
from collections import UserList


class AbstractClass(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self):
        pass


class Phone(AbstractClass):
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value


    @value.setter
    def value(self, value) -> None:
        codes_operators = ["067", "068", "096", "097", "098", "050",
                           "066", "095", "099", "063", "073", "093"]
        new_value = (value.strip().
                     removeprefix('+').
                     replace("(", '').
                     replace(")", '').
                     replace("-", ''))
        if new_value[:2] == '38' and len(new_value) == 12 and new_value[2:5] in codes_operators:
            self.__value = new_value
        else:
            raise TypeError

    def __str__(self):
        return f'User Phone: {str(self.value)}'


class Notate(AbstractClass, UserList):

    def __init__(self):
        super().__init__()

    def add_record(self, record) -> None:
        self.data.append(record)

    def __str__(self):
        count = 0
        for i in self.data:  # notates_list:
            count += 1
            print(f"{count}. {i}\n")
        return f'End of notates'

a = Phone('380638854917')
b = Notate()
b.append('aaaa')
b.append('bbbb')
print(a)
print(b)