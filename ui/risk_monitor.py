import tkinter as tk
from tkinter import ttk
from logic import names
from tkinter import font


class RiskMonitor(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.configure(bg="#ffffff")
        self.create_components()
        self.draw_components()

    def create_components(self):
        self.header = tk.Label(self, bg='#ffffff',
                               text=names.risks_headers['risk_mon_head'],
                               font=font.Font(size=20))
        self.table = ttk.Treeview(self, height=32)
        cols = ('id', 'descr', 'enabled', *[f'ex{i}' for i in range(10)],
                'erper', 'elrer', 'evrer', 'level')
        self.table['columns'] = cols
        for col in cols:
            self.table.column(col, anchor=tk.CENTER, width=50)
        self.table.column('#0', width=0)
        self.table.column('descr', anchor=tk.W, width=600)
        self.table.column('level', width=100)

    def draw_components(self):
        self.header.grid(row=0)
        self.table.grid(row=1, sticky=tk.W)
