import math
import tkinter as tk
from tkinter import ttk


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("460x640")
        self.light_theme = True
        self.memory = 0.0
        self.history = []
        self.expression = ""
        self.input_text = tk.StringVar()
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.set_theme()
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(padx=10, pady=(12, 6), fill="x")
        self.input_field = tk.Entry(
            input_frame,
            font=("Consolas", 22),
            textvariable=self.input_text,
            bd=4,
            relief=tk.RIDGE,
            justify="right",
            bg=self.entry_bg,
            fg=self.fg_color,
        )
        self.input_field.pack(ipady=14, padx=4, fill="x")
        btns_frame = tk.Frame(self.root, bg=self.bg_color)
        btns_frame.pack(padx=10, pady=6, fill="both")
        buttons = [
            ["sin", "cos", "tan", "log", "C"],
            ["√", "x²", "^", "(", ")"],
            ["7", "8", "9", "/", "M+"],
            ["4", "5", "6", "*", "M-"],
            ["1", "2", "3", "-", "MR"],
            ["0", ".", "=", "+", "Theme"],
        ]

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                self.create_button(btns_frame, label, r, c)

        history_frame = tk.LabelFrame(
            self.root, text="History (last 10)", bg=self.bg_color, fg=self.fg_color
        )
        history_frame.pack(padx=10, pady=(8, 12), fill="both", expand=True)
        self.history_box = tk.Text(
            history_frame,
            height=8,
            bg=self.entry_bg,
            fg=self.fg_color,
            font=("Consolas", 12),
        )
        self.history_box.pack(
            side="left", fill="both", expand=True, padx=(6, 0), pady=6
        )
        scrollbar = ttk.Scrollbar(history_frame, command=self.history_box.yview)
        scrollbar.pack(side="right", fill="y", padx=(0, 6), pady=6)
        self.history_box["yscrollcommand"] = scrollbar.set
        self.input_field.focus_set()

    def set_theme(self):
        if self.light_theme:
            self.bg_color = "#f0f0f0"
            self.fg_color = "#000000"
            self.entry_bg = "#ffffff"
            self.button_bg = "#e0e0e0"
        else:
            self.bg_color = "#2b2b2b"
            self.fg_color = "#ffffff"
            self.entry_bg = "#3a3a3a"
            self.button_bg = "#4a4a4a"
        self.root.configure(bg=getattr(self, "bg_color", "#f0f0f0"))

    def toggle_theme(self):
        self.light_theme = not self.light_theme
        self.set_theme()
        try:
            self.input_field.configure(bg=self.entry_bg, fg=self.fg_color)
            self.history_box.configure(bg=self.entry_bg, fg=self.fg_color)
            for child in self.root.winfo_children():
                for w in child.winfo_children():
                    if isinstance(w, tk.Button):
                        w.configure(bg=self.button_bg, fg=self.fg_color)
        except Exception:
            pass

    def create_button(self, parent, text, row, col):
        btn = tk.Button(
            parent,
            text=text,
            width=6,
            height=2,
            font=("Arial", 14),
            bg=self.button_bg,
            fg=self.fg_color,
            bd=2,
            relief=tk.RAISED,
            command=lambda t=text: self.on_click(t),
        )
        btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
        parent.grid_columnconfigure(col, weight=1)

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            result = self.evaluate_expression(self.expression)
            if isinstance(result, (int, float)):
                self.history.append(f"{self.expression} = {result}")
                self.expression = str(result)
            else:
                self.history.append(f"{self.expression} = Error")
                self.expression = ""
            self.update_history()
        elif char == "√":
            self.expression += "√("
        elif char == "x²":
            self.expression += "^2"
        elif char == "^":
            self.expression += "^"
        elif char == "log":
            self.expression += "log("
        elif char in ("sin", "cos", "tan"):
            self.expression += f"{char}("
        elif char == "M+":
            val = self.evaluate_expression(self.expression)
            if isinstance(val, (int, float)):
                self.memory += float(val)
        elif char == "M-":
            val = self.evaluate_expression(self.expression)
            if isinstance(val, (int, float)):
                self.memory -= float(val)
        elif char == "MR":
            if float(self.memory).is_integer():
                self.expression += str(int(self.memory))
            else:
                self.expression += str(self.memory)
        elif char == "Theme":
            self.toggle_theme()
        else:
            self.expression += str(char)

        self.input_text.set(self.expression)

    def _sanitize_and_prepare(self, expr: str) -> str:
        e = expr.replace("√", "sqrt")
        e = e.replace("^", "**")
        e = e.replace("log(", "log10(")

        for fn in ("sin", "cos", "tan"):
            e = e.replace(f"{fn}(", f"{fn}(radians(")

        opens = e.count("(")
        closes = e.count(")")
        if opens > closes:
            e += ")" * (opens - closes)

        return e

    def evaluate_expression(self, expr):
        if not expr:
            return ""

        py_expr = self._sanitize_and_prepare(expr)
        allowed_names = {
            name: getattr(math, name) for name in dir(math) if not name.startswith("__")
        }
        allowed_names.update(
            {
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e,
                "radians": math.radians,
                "log10": math.log10,
            }
        )

        try:
            value = eval(py_expr, {"__builtins__": None}, allowed_names)
            if isinstance(value, (int, float)):
                return value
            return str(value)
        except Exception:
            return "Error"

    def update_history(self):
        self.history_box.delete(1.0, tk.END)
        for item in self.history[-10:]:
            self.history_box.insert(tk.END, item + "\n")
        self.history_box.see(tk.END)

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.on_click("="))
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        for key in "0123456789+-*/().":
            self.root.bind(key, lambda event, k=key: self.on_click(k))

        self.root.bind("c", lambda event: self.on_click("C"))
        self.root.bind("C", lambda event: self.on_click("C"))

    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
