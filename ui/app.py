import tkinter as tk
from tkinter import ttk
from tkinter.constants import END
from logic.names import *
from logic.rand_risk import get_random_risks
from .risk_id import RiskIdentification
from .risk_rem import RiskRemoval
from .risk_analisis import RiskAnalisis
from logic import mock
from helper.counter import Counter


class RiskManagerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1500x750')

        self.is_removal = None
        self.is_analisis = None

        self.create_components()
        self.draw_components()
        self.risks = mock.get_random_risks()

    def create_components(self):
        self.sections = ttk.Notebook(self)
        self.tab1 = RiskIdentification(self)
        self.tab2 = RiskAnalisis(self)
        self.tab3 = RiskRemoval(self)
        self.tab4 = RiskIdentification(self)
        self.sections.add(self.tab1, text='Identification')
        self.sections.add(self.tab2, text='Analisis')
        self.sections.add(self.tab3, text='Removal')
        self.sections.add(self.tab4, text='monitoring')
        self.sections.bind('<<NotebookTabChanged>>', self.on_tab_change)

    def draw_components(self):
        self.sections.pack(expand=True, fill=tk.BOTH)

    def on_tab_change(self, event):
        tab = event.widget.tab('current')['text']
        if tab == 'Identification':
            self.update_iditification_tables()
        if tab == 'Analisis':
            if self.is_analisis is None:
                self.update_analisis_tab()
                self.is_analisis = True
        if tab == 'Removal':
            if self.is_removal is None:
                self.update_removal_tab()
                self.is_removal = True

    def update_analisis_tab(self):
        table = self.tab2.table
        src = self.get_risks_list()
        ct = Counter()

        values = []
        vrers = []
        for sourse, id in src:
            for j, risk in enumerate(sourse):
                val = [f'{i:4.2f}' for i in risk.value]
                avrg = sum(risk.value)/10
                risk.vrer = risk.lrer * avrg
                vrers.append(risk.vrer)
                values.append(
                    [f'{id}{j}', risk.descr, int(risk.enabled), *val,
                     f'{avrg:4.2f}', f'{risk.lrer:4.2f}', f'{risk.vrer:4.2f}']
                )

        max_ = max(vrers)
        min_ = min(vrers)
        mpr = (max_ - min_) / 3

        for sourse, id in src:
            for j, risk in enumerate(sourse):
                id = ct.next()
                if vrers[id] < mpr:
                    values[id].append('low')
                elif vrers[id] < 2 * mpr:
                    values[id].append('mid')
                else:
                    values[id].append('high')

                table.insert(parent='', index=tk.END, iid=id, text='',
                             values=values[id])
        table.heading('descr', text='Ризикові події', anchor=tk.W)
        table.heading('enabled', text='RP')
        for i in range(10):
            table.heading(f'ex{i}', text=f'Exp{i}')
        table.heading('er', text='er')
        table.heading('lrer', text='lrer')
        table.heading('vrer', text='vrer')
        table.heading('level', text='level')

    def update_removal_tab(self):
        tab = self.tab3
        src = self.get_risks_list()
        for sourse, id in src:
            for j, risk in enumerate(sourse):
                tab.add_row(f'{id}{j}', risk.descr)

    def update_iditification_tables(self):
        frame = self.tab1.frame
        src = self.get_risks_list()
        headers = [risks_sourses[1][i][0] for i in ['tech', 'cost', 'plan', 'mang']] \
            + [risks_events[1][i][0] for i in ['tech', 'cost', 'plan', 'mang']]
        for i, (sourse, id) in enumerate(src):
            frame.tables[i].delete(*frame.tables[i].get_children())
            count = 0
            for j, risk in enumerate(sourse):
                count += int(risk.enabled)
                frame.tables[i].insert(
                    parent='', index=j, iid=j, text='',
                    values=(f'{id}{j}', risk.descr, int(risk.enabled)))
            frame.tables[i].heading('descr', text=headers[i], anchor=tk.W)
            frame.tables[i].heading('number', text=count, anchor=tk.W)
            frame.tables[i].heading('percent', anchor=tk.W,
                                    text=f'{(count / len(sourse) * 100):4.2f}%')

    def get_risks_list(self):
        return [
            (self.risks.risks.sourses.T, 'T'),
            (self.risks.risks.sourses.C, 'C'),
            (self.risks.risks.sourses.P, 'P'),
            (self.risks.risks.sourses.M, 'M'),
            (self.risks.risks.accident.T, 'T'),
            (self.risks.risks.accident.C, 'C'),
            (self.risks.risks.accident.P, 'P'),
            (self.risks.risks.accident.M, 'M')
        ]
