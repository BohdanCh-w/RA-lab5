from .names import *
from .risk import *


class RisksManager:
    def __init__(self):
        self.risks = lambda: None
        self.risks.exp_num = 10
        self.risks.sourses = lambda: None
        src = risks_sourses[1]
        self.risks.sourses.headings = {
            'T': risks_sourses[1]['tech'][0],
            'C': risks_sourses[1]['cost'][0],
            'P': risks_sourses[1]['plan'][0],
            'M': risks_sourses[1]['mang'][0]
        }
        self.risks.sourses.T = [Risk(i) for i in src['tech'][1:]]
        self.risks.sourses.C = [Risk(i) for i in src['cost'][1:]]
        self.risks.sourses.P = [Risk(i) for i in src['plan'][1:]]
        self.risks.sourses.M = [Risk(i) for i in src['mang'][1:]]

        self.risks.accident = lambda: None
        acc = risks_events[1]
        self.risks.accident.headings = {
            'T': risks_events[1]['tech'][0],
            'C': risks_events[1]['cost'][0],
            'P': risks_events[1]['plan'][0],
            'M': risks_events[1]['mang'][0]
        }
        self.risks.accident.T = [Risk(i) for i in acc['tech'][1:]]
        self.risks.accident.C = [Risk(i) for i in acc['cost'][1:]]
        self.risks.accident.P = [Risk(i) for i in acc['plan'][1:]]
        self.risks.accident.M = [Risk(i) for i in acc['mang'][1:]]

    def print_risks(self):
        print('Risk sourses : ')
        print('Technical : ')
        for i, elem in enumerate(self.risks.sourses.T, 1):
            print(f'T{i} : {elem}')
        print('Cost : ')
        for i, elem in enumerate(self.risks.sourses.C, 1):
            print(f'C{i} : {elem}')
        print('Realisation : ')
        for i, elem in enumerate(self.risks.sourses.P, 1):
            print(f'P{i} : {elem}')
        print('Project Managment : ')
        for i, elem in enumerate(self.risks.sourses.M, 1):
            print(f'M{i} : {elem}')

        print('\nRisk accidents : ')
        print('Technical : ')
        for i, elem in enumerate(self.risks.accident.T, 1):
            print(f'T{i} : {elem}')
        print('Cost : ')
        for i, elem in enumerate(self.risks.accident.C, 1):
            print(f'C{i} : {elem}')
        print('Realisation : ')
        for i, elem in enumerate(self.risks.accident.P, 1):
            print(f'P{i} : {elem}')
        print('Project Managment : ')
        for i, elem in enumerate(self.risks.accident.M, 1):
            print(f'M{i} : {elem}')


if __name__ == '__main__':
    # risks = RisksManager()
    # risks.print_risks()
    print(risks_sourses)
