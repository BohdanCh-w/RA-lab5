import tkinter as tk
from tkinter import ttk
from logic import names
from tkinter import font
from helper.counter import RowCounter


class RiskRemoval(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.rc = RowCounter()
        self.rows = []

        self.create_components()
        self.draw_components()

        self.frame.grid_columnconfigure(0, weight=20)
        self.frame.grid_columnconfigure(1, weight=200)
        self.frame.grid_columnconfigure(2, weight=200)

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

        self.head = tk.Label(self.frame, bg='#ffffff',
                             text=names.risks_headers['risk_rem_head'],
                             font=font.Font(size=20))
        self.table1 = tk.Label(self.frame, bg='#ffffff', text='#')
        self.table2 = tk.Label(self.frame, bg='#ffffff', text='Ризикові події')
        self.table3 = tk.Label(self.frame, bg='#ffffff', text='Рішення')

    def draw_components(self):
        self.vsb.pack(side="right", fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        self.head.grid(row=self.rc.next(), column=0, columnspan=3)
        self.table1.grid(row=self.rc.next(), column=0)
        self.table2.grid(row=self.rc.curr(), column=1)
        self.table3.grid(row=self.rc.curr(), column=2)

    def add_row(self, st, text):
        row = [
            tk.Label(self.frame, text=st,
                     bg='#ffffff', borderwidth=2),
            tk.Label(self.frame, text=text,
                     bg='#ffffff', borderwidth=2),
            tk.StringVar(self.frame),
        ]
        row[2].set('Виберіть тип')
        row.append(tk.OptionMenu(self.frame, row[2],
                                 *names.risks_removal))
        row[0].grid(row=self.rc.next(), column=0, sticky=tk.W)
        row[1].grid(row=self.rc.curr(), column=1, sticky=tk.W)
        row[3].grid(row=self.rc.curr(), column=2, sticky=tk.W)

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
