from .risks import RisksManager
from random import random, choice


def get_random_risks():
    ret = RisksManager()

    values = []
    values.extend(ret.risks.sourses.T)
    values.extend(ret.risks.sourses.C)
    values.extend(ret.risks.sourses.P)
    values.extend(ret.risks.sourses.M)
    values.extend(ret.risks.accident.T)
    values.extend(ret.risks.accident.C)
    values.extend(ret.risks.accident.P)
    values.extend(ret.risks.accident.M)
    for obj in values:
        if choice([True, False]):
            obj.value = [random() for i in range(10)]
            obj.val_monitor = [random() * el for el in obj.value]
            obj.lrer = random()
            obj.elrer = random()
        else:
            obj.enabled = False

    return ret


# get_random_risks().print_risks()
