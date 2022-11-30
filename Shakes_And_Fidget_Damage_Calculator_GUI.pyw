# coding=utf8
# !/usr/bin/python

"""
author: Fabian Roscher
date: 25.11.2022
description: Shakes and Fidget Damage Calculator
version: 1.1
"""

from tkinter.messagebox import showerror
from customtkinter import StringVar, CTk, CTkFrame, CTkLabel, CTkOptionMenu, CTkEntry, CTkButton


def error():
    # displaying a messagebox with an error message
    showerror(title="Error", message="Please check your entries and make sure to write float numbers like 1.25 and not "
                                     "like 1,25.")


def calc_dmg(strength: int, armor: int, potion: float, pet_bonus: float) -> int:
    # calculates the damage
    strength += armor
    if potion != 0:
        strength *= potion
    strength = round(strength, 2)
    if pet_bonus != 0:
        strength *= pet_bonus
    return round(strength)


def character_limit(entry_text):
    # limits the entry to 10 characters
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:10])


def percent_sign(value: str) -> str:
    # takes the value before the % sign
    return value[0:-1] if value[-1] == "%" else value


def to_high_val(value: str) -> float:
    # checks if the value entered is too high e.g. when a number with a % sign was entered
    return float(value) / 100 + 1 if float(value) >= 2.0 else float(value)


def set_def(value: str) -> str:
    # sets the default value to 0 if nothing got typed in
    return 0 if value == "" else percent_sign(value)


class App:
    def __init__(self, master):
        # defining variables, styles and frames for the application
        super().__init__()
        self.__root = master
        self.__options = ["Battle Mage", "Berserk", "Mage", "Warrior", "Druid", "Scout", "Assassin",
                          "Demon Hunter"]
        # Variables
        self.__var = StringVar()
        self.__var.set(self.__options[0])  # default value
        self.__weapon_dmg = StringVar()
        self.__weapon_attribute = StringVar()
        self.__base_strength = StringVar()
        self.__pet_bonus = StringVar()
        self.__potion = StringVar()
        self.__head_bonus = StringVar()
        self.__chest_bonus = StringVar()
        self.__arm_bonus = StringVar()
        self.__shoe_bonus = StringVar()
        self.__necklace_bonus = StringVar()
        self.__belt_bonus = StringVar()
        self.__ring_bonus = StringVar()
        self.__shamrock_bonus = StringVar()
        self.__weapon_dmg_2 = StringVar()
        self.__weapon_attribute_2 = StringVar()
        self.__dmg = StringVar()
        self.__portal_bonus = StringVar()

        self.__root.title("Shakes and Fidget Damage Calculator")
        self.__frame_main = CTkFrame(self.__root)
        self.__frame_main.grid(row=0, column=0)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        self.__frame_entry = CTkFrame(self.__frame_main)
        self.__frame_entry.grid(row=1, column=0)
        self.__entry()

    def __entry(self):
        # setting all buttons, entry's and labels

        # deleting the old widgets (buttons, entry's ...)
        for widget in self.__frame_entry.winfo_children():
            widget.destroy()
        self.__frame_entry.grid_forget()

        self.__frame_main = CTkFrame(self.__root)
        self.__frame_main.grid(row=0, column=0)
        self.__root.columnconfigure(0, weight=1)
        self.__root.rowconfigure(0, weight=1)
        self.__frame_entry = CTkFrame(self.__frame_main)
        self.__frame_entry.grid(row=1, column=0)

        frame = CTkFrame(self.__frame_main)
        frame.grid(row=0, column=0)
        CTkLabel(frame, text="Choose your class: ").grid(row=0, column=0, padx=10, pady=10)
        CTkOptionMenu(frame, variable=self.__var, values=self.__options,
                      command=lambda event: self.__entry()).grid(row=0, column=1, padx=10, pady=10)

        self.__root.update()
        self.__root.minsize(620, 362)

        CTkLabel(self.__frame_entry, text="Weapon average damage:").grid(row=1, column=0,
                                                                         sticky="nw",
                                                                         padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__weapon_dmg, width=100).grid(row=1, column=1,
                                                                                     padx=10, pady=5,
                                                                                     sticky="nw")
        self.__weapon_dmg.trace("w", lambda *args: character_limit(self.__weapon_dmg))

        CTkLabel(self.__frame_entry, text="Weapon damage attribute:").grid(row=1, column=2,
                                                                           sticky="nw",
                                                                           padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__weapon_attribute, width=100).grid(row=1,
                                                                                           column=3,
                                                                                           padx=10,
                                                                                           pady=5,
                                                                                           sticky="nw")
        self.__weapon_attribute.trace("w", lambda *args: character_limit(self.__weapon_attribute))

        CTkLabel(self.__frame_entry, text="Damage base attribute:").grid(row=2, column=0,
                                                                         sticky="nw",
                                                                         padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__base_strength, width=100).grid(row=2,
                                                                                        column=1,
                                                                                        padx=10,
                                                                                        pady=5,
                                                                                        sticky="nw")
        self.__base_strength.trace("w", lambda *args: character_limit(self.__base_strength))

        CTkLabel(self.__frame_entry, text="Pet bonus:").grid(row=2, column=2, sticky="nw",
                                                             padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__pet_bonus, width=100).grid(row=2, column=3,
                                                                                    padx=10, pady=5,
                                                                                    sticky="nw")
        self.__pet_bonus.trace("w", lambda *args: character_limit(self.__pet_bonus))

        CTkLabel(self.__frame_entry, text="Potion bonus:").grid(row=3, column=0, sticky="nw",
                                                                padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__potion, width=100).grid(row=3, column=1,
                                                                                 padx=10, pady=5,
                                                                                 sticky="nw")
        self.__potion.trace("w", lambda *args: character_limit(self.__potion))

        CTkLabel(self.__frame_entry, text="Helm bonus:").grid(row=3, column=2, sticky="nw",
                                                              padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__head_bonus, width=100).grid(row=3, column=3,
                                                                                     padx=10, pady=5,
                                                                                     sticky="nw")
        self.__head_bonus.trace("w", lambda *args: character_limit(self.__head_bonus))

        CTkLabel(self.__frame_entry, text="Chest bonus:").grid(row=4, column=0, sticky="nw",
                                                               padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__chest_bonus, width=100).grid(row=4,
                                                                                      column=1,
                                                                                      padx=10,
                                                                                      pady=5,
                                                                                      sticky="nw")
        self.__chest_bonus.trace("w", lambda *args: character_limit(self.__chest_bonus))

        CTkLabel(self.__frame_entry, text="Arm bonus:").grid(row=4, column=2, sticky="nw",
                                                             padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__arm_bonus, width=100).grid(row=4, column=3,
                                                                                    padx=10, pady=5,
                                                                                    sticky="nw")
        self.__arm_bonus.trace("w", lambda *args: character_limit(self.__arm_bonus))

        CTkLabel(self.__frame_entry, text="Shoes bonus:").grid(row=5, column=0, sticky="nw",
                                                               padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__shoe_bonus, width=100).grid(row=5, column=1,
                                                                                     padx=10, pady=5,
                                                                                     sticky="nw")
        self.__shoe_bonus.trace("w", lambda *args: character_limit(self.__shoe_bonus))

        CTkLabel(self.__frame_entry, text="Necklace bonus:").grid(row=5, column=2, sticky="nw",
                                                                  padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__necklace_bonus, width=100).grid(row=5,
                                                                                         column=3,
                                                                                         padx=10,
                                                                                         pady=5,
                                                                                         sticky="nw")
        self.__necklace_bonus.trace("w", lambda *args: character_limit(self.__necklace_bonus))

        CTkLabel(self.__frame_entry, text="Belt bonus:").grid(row=6, column=0, sticky="nw",
                                                              padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__belt_bonus, width=100).grid(row=6, column=1,
                                                                                     padx=10, pady=5,
                                                                                     sticky="nw")
        self.__belt_bonus.trace("w", lambda *args: character_limit(self.__belt_bonus))

        CTkLabel(self.__frame_entry, text="Ring bonus:").grid(row=6, column=2, sticky="nw",
                                                              padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__ring_bonus, width=100).grid(row=6, column=3,
                                                                                     padx=10, pady=5,
                                                                                     sticky="nw")
        self.__ring_bonus.trace("w", lambda *args: character_limit(self.__ring_bonus))

        CTkLabel(self.__frame_entry, text="Shamrock bonus:").grid(row=7, column=0, sticky="nw",
                                                                  padx=10, pady=5)

        CTkEntry(self.__frame_entry, textvariable=self.__shamrock_bonus, width=100).grid(row=7,
                                                                                         column=1,
                                                                                         padx=10,
                                                                                         pady=5,
                                                                                         sticky="nw")
        self.__shamrock_bonus.trace("w", lambda *args: character_limit(self.__shamrock_bonus))

        CTkLabel(self.__frame_entry, text="Portal bonus:").grid(row=7, column=2, sticky="nw",
                                                                padx=10, pady=5)
        CTkEntry(self.__frame_entry, textvariable=self.__portal_bonus, width=100).grid(row=7,
                                                                                       column=3,
                                                                                       padx=10,
                                                                                       pady=5,
                                                                                       sticky="nw")
        self.__portal_bonus.trace("w", lambda *args: character_limit(self.__portal_bonus))

        # checks if the chosen character is assassin and if it is, add another entry field for the weapon damage and
        # attributes
        if self.__var.get() == "Assassin":
            CTkLabel(self.__frame_entry, text="Weapon 2 average damage:").grid(row=8, column=0,
                                                                               sticky="nw",
                                                                               padx=10, pady=5)

            CTkEntry(self.__frame_entry, textvariable=self.__weapon_dmg_2, width=100).grid(row=8,
                                                                                           column=1,
                                                                                           padx=10,
                                                                                           pady=5,
                                                                                           sticky="nw")
            self.__weapon_dmg_2.trace("w", lambda *args: character_limit(self.__weapon_dmg_2))

            CTkLabel(self.__frame_entry, text="Weapon 2 damage attribute:").grid(row=8, column=2,
                                                                                 sticky="nw",
                                                                                 padx=10,
                                                                                 pady=5)

            CTkEntry(self.__frame_entry, textvariable=self.__weapon_attribute_2, width=100).grid(
                row=8,
                column=3,
                padx=10,
                pady=5,
                sticky="nw")
            self.__weapon_attribute_2.trace("w", lambda *args: character_limit(self.__weapon_attribute_2))

            self.__root.minsize(640, 395)

        CTkButton(self.__frame_entry, text="Calculate", command=self.__calculate,
                  width=9).grid(row=9, column=3, padx=10, pady=5)

        CTkLabel(self.__frame_entry, text="Damage:").grid(row=9, column=0, padx=10, pady=10)
        CTkLabel(self.__frame_entry, textvariable=self.__dmg).grid(row=9, column=1, padx=10,
                                                                   pady=10)

        # by pressing the enter key the methode calculate gets called
        self.__root.bind("<Return>", lambda event: self.__calculate)

    def __calculate(self):
        try:
            # getting variables from the entry's
            # TODO: check if this can be optimized due to doing basically the same every time
            weapon_dmg: int = int(set_def(self.__weapon_dmg.get()))
            weapon_attribute: int = int(set_def(self.__weapon_attribute.get()))
            base_strength: int = int(set_def(self.__base_strength.get()))
            pet_bonus: float = to_high_val(set_def(self.__pet_bonus.get()))
            potion: float = to_high_val(set_def(self.__potion.get()))
            head_bonus: int = int(set_def(self.__head_bonus.get()))
            chest_bonus: int = int(set_def(self.__chest_bonus.get()))
            arm_bonus: int = int(set_def(self.__arm_bonus.get()))
            shoe_bonus: int = int(set_def(self.__shoe_bonus.get()))
            necklace_bonus: int = int(set_def(self.__necklace_bonus.get()))
            belt_bonus: int = int(set_def(self.__belt_bonus.get()))
            ring_bonus: int = int(set_def(self.__ring_bonus.get()))
            shamrock_bonus: int = int(set_def(self.__shamrock_bonus.get()))
            weapon_attribute_2: int = int(set_def(self.__weapon_attribute_2.get()))
            weapon_dmg_2: int = int(set_def(self.__weapon_dmg_2.get()))
            portal_bonus: int = int(set_def(self.__portal_bonus.get()))

        except ValueError:
            # throwing an error messagebox if a value was erroneously entered or a character was written in it instead
            # of an int
            error()
            return None

        # adding armor values to one variable
        armor = weapon_attribute + head_bonus + chest_bonus + arm_bonus + shoe_bonus + necklace_bonus + belt_bonus + \
                ring_bonus + shamrock_bonus
        strength = base_strength

        # checks which class is chosen
        if self.__var.get() == "Battle Mage" or self.__var.get() == "Berserk":
            # class specific calculations for damage
            bonus = armor * 0.11
            bonus = round(bonus, 2)
            strength += bonus
            strength = calc_dmg(strength, armor, potion, pet_bonus)
            dmg = weapon_dmg * (1 + strength / 10)
        elif self.__var.get() == "Assassin":
            armor += weapon_attribute_2
            strength = calc_dmg(strength, armor, potion, pet_bonus)
            dmg = (weapon_dmg + weapon_dmg_2) * 0.625 * (1 + strength / 10)
        else:
            strength = calc_dmg(strength, armor, potion, pet_bonus)
            dmg = weapon_dmg * (1 + strength / 10)

        # adding portal bonus to damage
        if portal_bonus != 0:
            dmg /= 100
            portal_bonus += 100
            dmg *= portal_bonus

        # rounding the damage to an int
        dmg = round(dmg)

        # setting the variable that displays the damage
        self.__dmg.set(str(dmg))


if __name__ == "__main__":
    # checks if the program is started as a main program and isn't imported
    root = CTk("system")
    calc = App(root)
    root.mainloop()
