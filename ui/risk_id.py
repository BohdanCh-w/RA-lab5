import tkinter as tk
from tkinter import ttk
from logic import names
from tkinter import font
from helper.counter import RowCounter


class RiskIdentification(tk.Frame):
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

        self.frame.label_1 = tk.Label(self.frame, bg='#ffffff',
                                      text=names.risks_headers['risk_id_src'],
                                      font=font.Font(size=20))
        self.frame.label_2 = tk.Label(self.frame, bg='#ffffff',
                                      text=names.risks_headers['risk_id_acc'],
                                      font=font.Font(size=20))

        self.frame.tables = []
        for i in range(8):
            self.frame.tables.append(ttk.Treeview(self.frame))

        cols = ('id', 'descr', 'number', 'percent')
        for table in self.frame.tables:
            table['columns'] = cols
            for col in cols:
                table.column(col, anchor=tk.W, width=80)
            table.column('descr', width=800)
            table.column('#0', width=10)

    def draw_components(self):
        self.vsb.pack(side="right", fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        rc = RowCounter(0)
        self.frame.label_1.grid(row=rc.next(), pady=5)
        for table in self.frame.tables[:4]:
            table.grid(row=rc.next(), pady=5)
        self.frame.label_2.grid(row=rc.next(), pady=5)
        for table in self.frame.tables[4:]:
            table.grid(row=rc.next(), pady=5)

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
