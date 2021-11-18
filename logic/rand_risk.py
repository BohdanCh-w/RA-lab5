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
            obj.value = [round(random(), 3) for i in range(10)]
            obj.val_monitor = [round(random() * el, 3) for el in obj.value]
            obj.lrer = round(random(), 3)
            obj.elrer = round(random(), 3)
        else:
            obj.enabled = False

    return ret


# get_random_risks().print_risks()
