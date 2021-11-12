from risks import Risks
from random import random, choice


def get_random_risks():
    ret = Risks()

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
            obj[1] = random()
        else:
            obj[0] = False

    return ret


get_random_risks().print_risks()
