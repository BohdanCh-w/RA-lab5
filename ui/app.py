import tkinter as tk
from tkinter import ttk
from logic.names import *
from logic.rand_risk import get_random_risks
from .risk_id import RiskIdentification
from .risk_rem import RiskRemoval
from logic import mock
from helper.counter import Counter


class RiskManagerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('1500x750')
        self.create_components()
        self.draw_components()
        self.risks = mock.get_random_risks()

    def create_components(self):
        self.sections = ttk.Notebook(self)
        self.tab1 = RiskIdentification(self)
        self.tab2 = RiskIdentification(self)
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
        if tab == 'Removal':
            self.update_removal_tab()

    def update_removal_tab(self):
        frame = self.tab3.frame
        src = self.get_risks_list()
        for sourse in src:
            pass

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
