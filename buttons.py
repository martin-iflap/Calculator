from customtkinter import  CTkButton
from settings import *


class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, fg_color, hover, text_color, span=1):
        super().__init__(master = parent,
                         text = text,
                         command = func,
                         corner_radius = STYLING["corner_radius"],
                         font = font,
                         fg_color = fg_color,
                         hover_color = hover,
                         text_color = text_color)
        self.grid(column = col, row = row, columnspan=span, sticky="nsew", padx=STYLING["gap"], pady=STYLING["gap"])