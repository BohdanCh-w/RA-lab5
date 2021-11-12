import tkinter as tk
from tkinter import ttk
from logic.names import *
from .risk_id import RiskIdentification


class RiskManagerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('400x300')
        self.create_components()
        self.draw_components()

    def create_components(self):
        self.sections = ttk.Notebook(self)
        self.tab1 = RiskIdentification(self)
        self.tab2 = RiskIdentification(self)
        self.tab3 = RiskIdentification(self)
        self.tab4 = RiskIdentification(self)
        self.sections.add(self.tab1, text='Identification')
        self.sections.add(self.tab2, text='Analisis')
        self.sections.add(self.tab3, text='Removal')
        self.sections.add(self.tab4, text='monitoring')

    def draw_components(self):
        self.sections.pack(expand=True, fill=tk.BOTH)
