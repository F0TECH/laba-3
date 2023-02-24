class FullEncapsulation:

    def init(self, name, age, height):
        self.name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height


class FullEncapsulation:
    def __init(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    @property
    def name(self):
        return self._name