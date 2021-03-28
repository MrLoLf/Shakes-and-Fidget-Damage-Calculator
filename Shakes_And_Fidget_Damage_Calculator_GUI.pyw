# coding=utf8

"""
author: Fabian Roscher
date: 28.03.2021
description: Shakes and Fidget Damage Calculator
version: 1.0
"""

try:
    from ttkthemes import ThemedTk
    from tkinter import ttk, IntVar, StringVar
    from tkinter.font import Font
    from tkinter.messagebox import showerror
except ImportError:
    from ttkthemes import ThemedTk
    from tkinter import ttk, IntVar, StringVar
    from tkinter.font import Font
    from tkinter.messagebox import showerror

    exit(-1)


def error():
    showerror(title="Error", message="Please check your entries and make sure to write float numbers like 1.25 and not "
                                     "like 1,25.")


def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:10])


class App:
    def __init__(self, master):
        super().__init__()
        self.root = master
        self.width = 1
        self.height = 1
        self.style = Font(family="Arial", size=16)
        self.button_style = ttk.Style()
        self.button_style.configure('my.TButton', font=('Arial', 16))
        self.options = ["Choose here", "Battle Mage", "Berserker", "Mage", "Warrior", "Druid", "Scout", "Assassin",
                        "Demon Hunter"]
        # Variables
        self.radi = IntVar()
        self.var = StringVar()
        self.var.set(self.options[0])  # default value
        self.weapon_dmg = StringVar()
        self.weapon_attri = StringVar()
        self.base_strength = StringVar()
        self.pet_bonus = StringVar()
        self.potion = StringVar()
        self.head_bonus = StringVar()
        self.chest_bonus = StringVar()
        self.arm_bonus = StringVar()
        self.shoe_bonus = StringVar()
        self.necklace_bonus = StringVar()
        self.belt_bonus = StringVar()
        self.ring_bonus = StringVar()
        self.shamrock_bonus = StringVar()
        self.weapon_dmg_2 = StringVar()
        self.weapon_attri_2 = StringVar()
        self.dmg = StringVar()

        self.root.title("Shakes and Fidget Damage Calculator")
        self.root.configure(bg="#3C3C3C")
        self.frame_main = ttk.Frame(self.root)
        self.frame_main.grid(row=0, column=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame_entry = ttk.Frame(self.frame_main)
        self.frame_entry.grid(row=1, column=0)
        self.gui()

    def gui(self):

        frame = ttk.Frame(self.frame_main)
        frame.grid(row=0, column=0)
        ttk.Label(frame, text="Choose your class: ", font=self.style).grid(row=0, column=0, padx=10, pady=10)
        ttk.OptionMenu(frame, self.var, *self.options, style="my.TButton",
                       command=lambda event: self.entry()).grid(row=0, column=1, padx=10, pady=10)

    def entry(self):

        for widget in self.frame_entry.winfo_children():
            widget.destroy()
        self.frame_entry.pack_forget()  # löschen der alten widgets (Label und Button ...)

        self.root.update()

        ttk.Label(self.frame_entry, text="Weapon average damage:", font=self.style).grid(row=1, column=0, sticky="nw",
                                                                                         padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.weapon_dmg, font=self.style, width=10).grid(row=1, column=1,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="nw")
        self.weapon_dmg.trace("w", lambda *args: character_limit(self.weapon_dmg))

        ttk.Label(self.frame_entry, text="Weapon damage attribute:", font=self.style).grid(row=1, column=2, sticky="nw",
                                                                                           padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.weapon_attri, font=self.style, width=10).grid(row=1, column=3,
                                                                                                    padx=10, pady=5,
                                                                                                    sticky="nw")
        self.weapon_attri.trace("w", lambda *args: character_limit(self.weapon_attri))

        ttk.Label(self.frame_entry, text="Damage base attribute:", font=self.style).grid(row=2, column=0, sticky="nw",
                                                                                         padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.base_strength, font=self.style, width=10).grid(row=2, column=1,
                                                                                                     padx=10, pady=5,
                                                                                                     sticky="nw")
        self.base_strength.trace("w", lambda *args: character_limit(self.base_strength))

        ttk.Label(self.frame_entry, text="Pet bonus:", font=self.style).grid(row=2, column=2, sticky="nw",
                                                                             padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.pet_bonus, font=self.style, width=10).grid(row=2, column=3,
                                                                                                 padx=10, pady=5,
                                                                                                 sticky="nw")
        self.pet_bonus.trace("w", lambda *args: character_limit(self.pet_bonus))

        ttk.Label(self.frame_entry, text="Potion bonus:", font=self.style).grid(row=3, column=0, sticky="nw",
                                                                                padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.potion, font=self.style, width=10).grid(row=3, column=1,
                                                                                              padx=10, pady=5,
                                                                                              sticky="nw")
        self.potion.trace("w", lambda *args: character_limit(self.potion))

        ttk.Label(self.frame_entry, text="Helm bonus:", font=self.style).grid(row=3, column=2, sticky="nw",
                                                                              padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.head_bonus, font=self.style, width=10).grid(row=3, column=3,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="nw")
        self.head_bonus.trace("w", lambda *args: character_limit(self.head_bonus))

        ttk.Label(self.frame_entry, text="Chest bonus:", font=self.style).grid(row=4, column=0, sticky="nw",
                                                                               padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.chest_bonus, font=self.style, width=10).grid(row=4, column=1,
                                                                                                   padx=10, pady=5,
                                                                                                   sticky="nw")
        self.chest_bonus.trace("w", lambda *args: character_limit(self.chest_bonus))

        ttk.Label(self.frame_entry, text="Arm bonus:", font=self.style).grid(row=4, column=2, sticky="nw",
                                                                             padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.arm_bonus, font=self.style, width=10).grid(row=4, column=3,
                                                                                                 padx=10, pady=5,
                                                                                                 sticky="nw")
        self.arm_bonus.trace("w", lambda *args: character_limit(self.arm_bonus))

        ttk.Label(self.frame_entry, text="Shoes bonus:", font=self.style).grid(row=5, column=0, sticky="nw",
                                                                               padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.shoe_bonus, font=self.style, width=10).grid(row=5, column=1,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="nw")
        self.shoe_bonus.trace("w", lambda *args: character_limit(self.shoe_bonus))

        ttk.Label(self.frame_entry, text="Necklace bonus:", font=self.style).grid(row=5, column=2, sticky="nw",
                                                                                  padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.necklace_bonus, font=self.style, width=10).grid(row=5, column=3,
                                                                                                      padx=10, pady=5,
                                                                                                      sticky="nw")
        self.necklace_bonus.trace("w", lambda *args: character_limit(self.necklace_bonus))

        ttk.Label(self.frame_entry, text="Belt bonus:", font=self.style).grid(row=6, column=0, sticky="nw",
                                                                              padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.belt_bonus, font=self.style, width=10).grid(row=6, column=1,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="nw")
        self.belt_bonus.trace("w", lambda *args: character_limit(self.belt_bonus))

        ttk.Label(self.frame_entry, text="Ring bonus:", font=self.style).grid(row=6, column=2, sticky="nw",
                                                                              padx=10, pady=5)
        ttk.Entry(self.frame_entry, textvariable=self.ring_bonus, font=self.style, width=10).grid(row=6, column=3,
                                                                                                  padx=10, pady=5,
                                                                                                  sticky="nw")
        self.ring_bonus.trace("w", lambda *args: character_limit(self.ring_bonus))

        ttk.Label(self.frame_entry, text="Shamrock bonus:", font=self.style).grid(row=7, column=0, sticky="nw",
                                                                                  padx=10, pady=5)

        ttk.Entry(self.frame_entry, textvariable=self.shamrock_bonus, font=self.style, width=10).grid(row=7, column=1,
                                                                                                      padx=10, pady=5,
                                                                                                      sticky="nw")
        self.shamrock_bonus.trace("w", lambda *args: character_limit(self.shamrock_bonus))

        if self.var.get() == "Assassin":
            ttk.Label(self.frame_entry, text="Weapon 2 average damage:", font=self.style).grid(row=7, column=2,
                                                                                               sticky="nw",
                                                                                               padx=10, pady=5)

            ttk.Entry(self.frame_entry, textvariable=self.weapon_dmg_2, font=self.style, width=10).grid(row=7, column=3,
                                                                                                        padx=10, pady=5,
                                                                                                        sticky="nw")
            self.weapon_dmg_2.trace("w", lambda *args: character_limit(self.weapon_dmg_2))

            ttk.Label(self.frame_entry, text="Weapon 2 damage attribute:", font=self.style).grid(row=8, column=0,
                                                                                                 sticky="nw", padx=10,
                                                                                                 pady=5)

            ttk.Entry(self.frame_entry, textvariable=self.weapon_attri_2, font=self.style, width=10).grid(row=8,
                                                                                                          column=1,
                                                                                                          padx=10,
                                                                                                          pady=5,
                                                                                                          sticky="nw")
            self.weapon_attri_2.trace("w", lambda *args: character_limit(self.weapon_attri_2))

            ttk.Button(self.frame_entry, text="Calculate", command=self.calculate, style="my.TButton",
                       width=9).grid(row=8, column=3, padx=10, pady=5)
        else:
            ttk.Button(self.frame_entry, text="Calculate", command=self.calculate, style="my.TButton",
                       width=9).grid(row=7, column=3, padx=10, pady=5)

        ttk.Label(self.frame_entry, text="Damage:", font=self.style).grid(row=9, column=0, padx=10, pady=10)
        ttk.Label(self.frame_entry, textvariable=self.dmg, font=self.style).grid(row=9, column=1, padx=10, pady=10)

        self.root.bind("<Return>", lambda event: self.calculate())

    def calculate(self):
        try:

            weapon_dmg = self.weapon_dmg.get()
            weapon_attri = self.weapon_attri.get()
            base_strength = self.base_strength.get()
            pet_bonus = self.pet_bonus.get()
            potion = self.potion.get()
            head_bonus = self.head_bonus.get()
            chest_bonus = self.chest_bonus.get()
            arm_bonus = self.arm_bonus.get()
            shoe_bonus = self.shoe_bonus.get()
            necklace_bonus = self.necklace_bonus.get()
            belt_bonus = self.belt_bonus.get()
            ring_bonus = self.ring_bonus.get()
            shamrock_bonus = self.shamrock_bonus.get()
            weapon_attri_2 = self.weapon_attri_2.get()
            weapon_dmg_2 = self.weapon_dmg_2.get()
            if weapon_dmg == "":
                weapon_dmg = 0
            if weapon_attri == "":
                weapon_attri = 0
            if base_strength == "":
                base_strength = 0
            if pet_bonus == "":
                pet_bonus = 0
            if float(pet_bonus) >= 2:
                pet_bonus = float(pet_bonus)
                pet_bonus /= 100
                pet_bonus += 1
            if potion == "":
                potion = 0
            if float(potion) >= 2:
                potion = float(potion)
                potion /= 100
                potion += 1
            if head_bonus == "":
                head_bonus = 0
            if chest_bonus == "":
                chest_bonus = 0
            if arm_bonus == "":
                arm_bonus = 0
            if shoe_bonus == "":
                shoe_bonus = 0
            if necklace_bonus == "":
                necklace_bonus = 0
            if belt_bonus == "":
                belt_bonus = 0
            if ring_bonus == "":
                ring_bonus = 0
            if shamrock_bonus == "":
                shamrock_bonus = 0
            if weapon_dmg_2 == "":
                weapon_dmg_2 = 0
            if weapon_attri_2 == "":
                weapon_attri_2 = 0

            weapon_dmg = int(weapon_dmg)
            weapon_attri = int(weapon_attri)
            base_strength = int(base_strength)
            pet_bonus = float(pet_bonus)
            potion = float(potion)
            head_bonus = int(head_bonus)
            chest_bonus = int(chest_bonus)
            arm_bonus = int(arm_bonus)
            shoe_bonus = int(shoe_bonus)
            necklace_bonus = int(necklace_bonus)
            belt_bonus = int(belt_bonus)
            ring_bonus = int(ring_bonus)
            shamrock_bonus = int(shamrock_bonus)
            weapon_dmg_2 = int(weapon_dmg_2)
            weapon_attri_2 = int(weapon_attri_2)

        except ValueError:
            error()
            return None

        armor = weapon_attri + head_bonus + chest_bonus + arm_bonus + shoe_bonus + necklace_bonus + belt_bonus + \
                ring_bonus + shamrock_bonus
        strength = base_strength

        if self.var.get() == "Battle Mage" or self.var.get() == "Berserker":
            bonus = armor * 0.11
            bonus = round(bonus, 2)
            strength += bonus
            strength += armor
            print(potion)
            if potion != 0:
                strength *= potion
            strength = round(strength, 2)
            print(pet_bonus)
            if pet_bonus != 0:
                strength *= pet_bonus
            strength = round(strength)
            dmg = weapon_dmg * (1 + strength / 10)

        elif self.var.get() == "Assassin":
            armor += weapon_attri_2
            strength += armor
            if potion != 0:
                strength *= potion
            strength = round(strength, 2)
            if pet_bonus != 0:
                strength *= pet_bonus
            strength = round(strength)
            dmg = (weapon_dmg + weapon_dmg_2) * 0.625 * (1 + strength / 10)

        else:
            strength += armor
            if potion != 0:
                strength *= potion
            strength = round(strength, 2)
            if pet_bonus != 0:
                strength *= pet_bonus
            strength = round(strength)
            dmg = weapon_dmg * (1 + strength / 10)

        dmg = round(dmg)
        self.dmg.set(dmg)

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    calc = App(root)
    root.mainloop()
