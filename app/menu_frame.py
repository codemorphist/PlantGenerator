import logging
logger = logging.getLogger(__name__)

import tkinter as tk
from tkinter import ttk


class MenuButtonsFrame(ttk.Frame):
    def __init__(self, container, buttons: dict[str, callable]):
        super().__init__(container)

        self.buttons = {}
        for text, callback in buttons.items():
            self.buttons[text] = ttk.Button(self, text=text, 
                                            command=callback)
        self.configure_buttons()

    def configure_buttons(self):
        for row, btn in enumerate(self.buttons):
            self.buttons[btn].grid(row=row, column=0, padx=5, pady=5,
                        sticky="nsew")

class Menu(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        buttons = {
            "Generate Plant": lambda: self.controller.show_frame("PlantGenerator"),
            "Smash Plant": lambda: self.controller.show_frame("SmashPlant"),
            "Mass Smash": lambda: self.controller.show_frame("MassSmash"),
            "Exit": lambda: self.controller.quit()
        }

        self.buttons_frame = MenuButtonsFrame(self, buttons)

        self.configure_widgets()
     
    def configure_widgets(self):
        """
        Configure place and style of widgets and frames
        """
        self.buttons_frame.place(relx=0.5, rely=0.5, 
                                 anchor=tk.CENTER) 
