class Counter:
    def __init__(self, start=0):
        self.__curr = start-1

    def next(self):
        self.__curr += 1
        return self.__curr

    def curr(self):
        return self.__curr


class RowCounter(Counter):
    def __init__(self, start=0):
        Counter.__init__(self, start)
