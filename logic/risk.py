class Risk:
    def __init__(self, descr_, enabled_=True, value_=0):
        self.descr = descr_
        self.enabled = enabled_
        self.value = value_

    def __str__(self):
        return f'{self.descr} - {self.value}'

    def __val(self):
        try:
            return sum(self.value)/len(self.value)
        except TypeError:
            return self.value

    def __add__(self, other):
        return self.__val() + other.__val()

    def __radd__(self, other):
        return other + self.__val()
