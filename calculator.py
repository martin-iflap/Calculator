import customtkinter as ctk
from buttons import Button
from settings import *

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.geometry(APP_SIZE)
        self.resizable(False, False)
        self.title("Calculator")

        self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = "a")
        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = "a")

        self.result_string = ctk.StringVar(value="0")
        self.formula_string = ctk.StringVar(value="")

        self.display_nums = []
        self.full_operation = []

        self.create_widgets()


    def create_widgets(self):
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        OutputLabel(self, 0, "se", main_font, self.formula_string)
        OutputLabel(self, 1, "e", result_font, self.result_string)

        # Button(parent=self,
        #        func=self.invert,
        #        text=OPERATORS["invert"]["text"],
        #        col=OPERATORS["invert"]["col"],
        #        row=OPERATORS["invert"]["row"],
        #        font=main_font)

        for key in OPERATORS.keys():
            func_name = key
            func = getattr(self, func_name)

            Button(parent=self,
                   func=func,
                   text=OPERATORS[key]["text"],
                   col=OPERATORS[key]["col"],
                   row=OPERATORS[key]["row"],
                   font=main_font)

        for key in NUM_POSITION.keys():
            Button(parent=self,
                   func=lambda k=key: self.num_click(k),
                   text=str(key),
                   col=NUM_POSITION[key]["col"],
                   row=NUM_POSITION[key]["row"],
                   font=main_font,
                   span=NUM_POSITION[key]["span"])

        for key in MATH_POSITIONS.keys():
            Button(parent=self,
                   func=lambda k=key: self.operator_click(k),
                   text=MATH_POSITIONS[key]["character"],
                   col=MATH_POSITIONS[key]["col"],
                   row=MATH_POSITIONS[key]["row"],
                   font=main_font)


    def clear(self):
        self.result_string.set("")
        self.formula_string.set("")
        self.display_nums.clear()
        self.full_operation.clear()

    def percent(self):
        print("%")

    def invert(self):
        print("invert")

    def num_click(self, value):
        self.display_nums.append(str(value))
        full_num = "".join(self.display_nums)
        self.result_string.set(full_num)

    def operator_click(self, value):
        current_num = "".join(self.display_nums)
        if current_num:
            self.full_operation.append(current_num)
            if value != "=":
                self.full_operation.append(value)
                self.display_nums.clear()
                self.result_string.set("")
                self.formula_string.set(" ".join(self.full_operation))

            else:
                formula = " ".join(self.full_operation)
                result = eval(formula)
                if isinstance(result, float):
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 3)
                self.result_string.set(result)
                self.formula_string.set(formula)
                self.display_nums = [str(result)]
                self.full_operation.clear()


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan = 4 ,row = row, sticky = anchor, padx=10)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()