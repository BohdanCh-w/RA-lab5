import tkinter as tk
from tkinter import ttk
from logic import names
from tkinter.font import Font
from helper.counter import RowCounter


class RiskChange(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self)
        self.parent = parent

        self.configure(bg="#ffffff")
        self.type = None
        self.enabled = None

        self.create_components()
        self.draw_components()

    def create_components(self):
        self.head = tk.Label(self, bg='#ffffff',
                             text=names.risks_headers['risk_change_head'],
                             font=Font(size=20))

        str_var = tk.StringVar(self)
        str_var.set('Виберіть групу')
        self.dd_type = tk.OptionMenu(self, str_var, *names.risk_monitor['set'],
                                     command=self.type_selected)
        self.l_code = tk.Label(self, bg='#ffffff',
                               text=names.risk_monitor['code'],
                               font=Font(size=14))
        self.e_code = tk.Entry(self, font=Font(size=14),
                               bg='#f5f5f5', width=10)
        self.b_code = tk.Button(self, text=names.risk_monitor['code_find'],
                                font=Font(size=14), command=self.find_risk)

        self.l_name = tk.Label(self, bg='#ffffff',
                               text=names.risk_monitor['name'],
                               font=Font(size=14))
        self.e_name = tk.Entry(self, font=Font(size=14),
                               bg='#f5f5f5', width=80)

        self.enabled = tk.IntVar()
        self.enabled.set(0)
        self.c_enabled = tk.Checkbutton(self, text=names.risk_monitor['enabled'],
                                        font=Font(size=14), variable=self.enabled)

        self.l_exp = tk.Label(self, bg='#ffffff',
                              text=names.risk_monitor['exp'],
                              font=Font(size=14))
        self.e_exp = [tk.Entry(self, font=Font(size=14),
                               width=10, bg='#f5f5f5')
                      for i in range(10)]

        self.l_damage = tk.Label(self, bg='#ffffff',
                                 text=names.risk_monitor['damage'],
                                 font=Font(size=14))
        self.e_damage = tk.Entry(self, font=Font(size=14), bg='#f5f5f5')

        self.l_exp_mon = tk.Label(self, bg='#ffffff',
                                  text=names.risk_monitor['exp_monitor'],
                                  font=Font(size=14))
        self.e_exp_mon = [tk.Entry(self, font=Font(size=14),
                                   width=10, bg='#f5f5f5')
                          for i in range(10)]

        self.l_damage_mon = tk.Label(self, bg='#ffffff',
                                     text=names.risk_monitor['damage_monitor'],
                                     font=Font(size=14))
        self.e_damage_mon = tk.Entry(self, font=Font(size=14), bg='#f5f5f5')

        self.b_change = tk.Button(self, text=names.risk_monitor['change'],
                                  font=Font(size=14),
                                  command=self.change_risk)

    def draw_components(self):
        rc = RowCounter()
        self.head.grid(row=rc.next(), column=0,
                       columnspan=10, pady=20)

        self.dd_type.grid(row=rc.next(), column=0,
                          columnspan=3, pady=30, sticky=tk.W)
        self.l_code.grid(row=rc.curr(), column=2, columnspan=2, sticky=tk.W)
        self.e_code.grid(row=rc.curr(), column=4, sticky=tk.W)
        self.b_code.grid(row=rc.curr(), column=5, columnspan=2, sticky=tk.W)

        self.l_name.grid(row=rc.next(), column=0, pady=10, sticky=tk.W)
        self.e_name.grid(row=rc.curr(), column=1, columnspan=7, sticky=tk.W)

        self.c_enabled.grid(row=rc.next(), column=0, columnspan=4, sticky=tk.W)

        tk.Label(self, bg='#ffffff', height=3).grid(row=rc.next())
        self.l_exp.grid(row=rc.next(), column=0, columnspan=10, sticky=tk.W)
        rc.next()
        for i, entry in enumerate(self.e_exp):
            entry.grid(row=rc.curr(), column=i, padx=5, sticky=tk.W)

        self.l_damage.grid(row=rc.next(), column=0,
                           columnspan=2, pady=10, sticky=tk.W)
        self.e_damage.grid(row=rc.curr(), column=3,
                           columnspan=2, pady=30, sticky=tk.W)

        tk.Label(self, bg='#ffffff', height=3).grid(row=rc.next())
        self.l_exp_mon.grid(row=rc.next(), column=0,
                            columnspan=10, sticky=tk.W)
        rc.next()
        for i, entry in enumerate(self.e_exp_mon):
            entry.grid(row=rc.curr(), column=i, padx=5, sticky=tk.W)

        self.l_damage_mon.grid(row=rc.next(), column=0,
                               columnspan=2, pady=10, sticky=tk.W)
        self.e_damage_mon.grid(row=rc.curr(), column=3,
                               columnspan=2, pady=30, sticky=tk.W)

        self.b_change.grid(row=rc.next(), column=4, columnspan=2)

    def find_risk(self):
        if self.type is None:
            raise ValueError('Type not selected')
        type = self.type == names.risk_monitor['set'][0]

        code = self.e_code.get().strip()
        if len(code) == 0:
            raise ValueError('Enter code of risk')

        group = code[0].upper()
        if group not in ('T', 'C', 'P', 'M'):
            raise ValueError('Wrong group code')

        try:
            num = int(code[1:])
        except ValueError:
            raise ValueError('Wrong number of code')

        self.risk = self.parent.get_risk(type, group, num)
        self.set_values(self.risk)

    def set_values(self, risk):
        self.e_name.delete(0, tk.END)
        self.e_name.insert(0, risk.descr)

        self.enabled.set(int(risk.enabled))

        for i, obj in enumerate(self.e_exp):
            obj.delete(0, tk.END)
            obj.insert(0, risk.value[i])

        self.e_damage.delete(0, tk.END)
        self.e_damage.insert(0, risk.lrer)

        for i, obj in enumerate(self.e_exp_mon):
            obj.delete(0, tk.END)
            obj.insert(0, risk.val_monitor[i])

        self.e_damage_mon.delete(0, tk.END)
        self.e_damage_mon.insert(0, risk.elrer)

    def change_risk(self):
        def data(): return None
        try:
            data.name = self.e_name.get()
            data.enabled = bool(self.enabled.get())
            data.exp = [float(self.e_exp[i].get()) for i in range(10)]
            data.damage = float(self.e_damage.get())
            data.exp_mon = [float(self.e_exp_mon[i].get()) for i in range(10)]
            data.damage_mon = float(self.e_damage_mon.get())
        except Exception as e:
            raise ValueError('Wrong data - ' + str(e))
        self.risk.descr = data.name
        self.risk.enabled = data.enabled
        self.risk.value = data.exp
        self.risk.lrer = data.damage
        self.risk.val_monitor = data.exp_mon
        self.risk.elrer = data.damage_mon

    def type_selected(self, type):
        self.type = type
