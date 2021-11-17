import tkinter as tk
from tkinter import ttk
from logic import names
from tkinter import font
from helper.counter import RowCounter


class RiskAnalisis(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_components()
        self.draw_components()

    def create_components(self):
        self.canvas = tk.Canvas(self, borderwidth=0, bg='#ffffff')
        self.frame = tk.Frame(self.canvas, bg='#ffffff')
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.canvas.create_window(
            (0, 0), window=self.frame, anchor='nw', tags='self.frame')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.frame.bind("<Configure>", self.on_configure)

        self.header = tk.Label(self.frame, bg='#ffffff',
                               text=names.risks_headers['risk_prob_head'],
                               font=font.Font(size=20))
        self.table = ttk.Treeview(self.frame, height=32)
        cols = ('id', 'descr', 'enabled', *[f'ex{i}' for i in range(10)],
                'er', 'lrer', 'vrer', 'level')
        self.table['columns'] = cols
        for col in cols:
            self.table.column(col, anchor=tk.CENTER, width=50)
        self.table.column('#0', width=0)
        self.table.column('descr', anchor=tk.W, width=600)
        self.table.column('level', width=100)

    def draw_components(self):
        self.vsb.pack(side="right", fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        self.header.grid(row=0)
        self.table.grid(row=1, sticky=tk.W)

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
