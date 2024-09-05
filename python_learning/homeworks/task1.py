import tkinter as tk

class App:
    TITLE   = "Сивко Иван автора. ЛР1 Tkinter GUI. ПМИ-бо-23"
    FUNC    = "(a-b)**5 + a**5 - b**5"
    LETTERS = "abc"
    HEIGHT  = 200
    WIDTH   = 400
    X_POS   = 100
    Y_POS   = 100

    def __init__(self, root):
        self.root = root
        self.entries = dict();
        self.setup_ui()
        root.mainloop()

    def setup_ui(self):
        self.root.title(App.TITLE)
        self.root.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.root.resizable(False, False)

        for i in range(len(App.LETTERS)+1):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        for row_, letter in enumerate(App.LETTERS):
            row_ = len(App.LETTERS) if letter==App.LETTERS[-1] else row_
            tk.Label(self.root, text=f"{letter}=").grid(row=row_, column=0, padx=10, pady=10, sticky="nsew")
            self.entries[letter] = tk.Entry(self.root)
            self.entries[letter].grid(row=row_, column=1, padx=10, pady=10, sticky="nsew")
        tk.Button(text="calculate", command=self.calculate).grid(row=len(App.LETTERS)-1, column=0, sticky="nsew")
        tk.Label(self.root, text=App.FUNC).grid(row=len(App.LETTERS)-1, column=1, sticky="nsew")

    def calculate(self):
        func = lambda a, b: (a-b)**5 + a**5 - b**5
        self.entries[App.LETTERS[-1]].delete(0, tk.END)
        try:
            self.entries[App.LETTERS[-1]].insert(0, str(func(
                self.get_int_from_entry(App.LETTERS[0]),
                self.get_int_from_entry(App.LETTERS[1]))))
        except ValueError:
            self.entries[App.LETTERS[-1]].insert(0, "Error")

    def get_int_from_entry(self, letter):
        value = self.entries[letter].get()
        return int(value) if value.strip() else 0

if __name__ == "__main__":
    App(tk.Tk())
