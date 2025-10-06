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

        self.display_num = []
        self.full_operation = []

        self.create_widgets()


    def create_widgets(self):
        """Create all the widgets with for loops"""
        main_font = ctk.CTkFont(family=FONT, size=NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family=FONT, size=OUTPUT_FONT_SIZE)

        OutputLabel(self, 0, "se", main_font, self.formula_string)
        OutputLabel(self, 1, "e", result_font, self.result_string)

        for key in OPERATORS.keys():
            func_name = key
            func = getattr(self, func_name)
            Button(parent=self,
                   func=func,
                   text=OPERATORS[key]["text"],
                   col=OPERATORS[key]["col"],
                   row=OPERATORS[key]["row"],
                   font=main_font,
                   fg_color=COLORS["operations_and_math"]["fg_color"],
                   hover=COLORS["operations_and_math"]["hover"],
                   text_color=COLORS["operations_and_math"]["text_color"])

        for key in NUM_POSITION.keys():
            Button(parent=self,
                   func=lambda k=key: self.num_click(k),
                   text=str(key),
                   col=NUM_POSITION[key]["col"],
                   row=NUM_POSITION[key]["row"],
                   font=main_font,
                   span=NUM_POSITION[key]["span"],
                   fg_color=COLORS["nums"]["fg_color"],
                   hover=COLORS["nums"]["hover"],
                   text_color=COLORS["nums"]["text_color"])

        for key in MATH_POSITIONS.keys():
            Button(parent=self,
                   func=lambda k=key: self.operator_click(k),
                   text=MATH_POSITIONS[key]["character"],
                   col=MATH_POSITIONS[key]["col"],
                   row=MATH_POSITIONS[key]["row"],
                   font=main_font,
                   fg_color=COLORS["operations_and_math"]["fg_color"],
                   hover=COLORS["operations_and_math"]["hover"],
                   text_color=COLORS["operations_and_math"]["text_color"])


    def clear(self):
        """Reset string variables and clear lists"""
        self.result_string.set("0")
        self.formula_string.set("")
        self.display_num.clear()
        self.full_operation.clear()

    def percent(self):
        """Turn the current number into a percentage of the preceding number"""
        current_operation = "".join(self.full_operation)
        if current_operation:
            main_num = self.full_operation[-2]
            current_num = "".join(self.display_num)
            new_num = (float(main_num) / 100 * float(current_num))
            if new_num.is_integer():
                new_num = int(new_num)
            else:
                new_num = round(new_num, 3)
            self.result_string.set(str(current_num)+"%")
            self.display_num = [str(new_num)]
        else:
            current_num = "".join(self.display_num)
            if current_num:
                new_num = float(current_num) / 100
                if new_num.is_integer():
                    new_num = int(new_num)
                else:
                    new_num = round(new_num, 6)
                self.display_num = [str(new_num)]
                self.result_string.set(str(new_num))

    def invert(self):
        """Multiply current number by -1"""
        current_num = "".join(self.display_num)
        if current_num:
            new_num = float(current_num) * -1
            if new_num.is_integer():
                new_num = int(new_num)
            else:
                new_num = round(new_num, 3)
            self.display_num = [str(new_num)]
            self.result_string.set("".join(self.display_num))

    def num_click(self, value):
        """Append the value of the clicked number inside the display_num list
           and refresh result string"""
        self.display_num.append(str(value))
        full_num = "".join(self.display_num)
        self.result_string.set(full_num)

    def operator_click(self, value):
        """Append the display_num and the operator to full_operation list
           If operator is = compute and display result using eval
           Set the result to be the display_num"""
        current_num = "".join(self.display_num)
        if current_num:
            self.full_operation.append(current_num)
            if value != "=":
                self.full_operation.append(value)
                self.display_num.clear()
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
                self.display_num = [str(result)]
                self.full_operation.clear()


class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, font=font, textvariable=string_var)
        self.grid(column=0, columnspan = 4 ,row = row, sticky = anchor, padx=10)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()