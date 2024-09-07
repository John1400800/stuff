import tkinter as tk


class App:
    """GUI приложение на Tkinter для вычисления выражений
    на основе введённых значений. """
    TITLE = "Сивко Иван. ЛР1 Tkinter GUI. ПМИ-бо-23"
    FUNC = "a+b"
    LETTERS = "abc"
    HEIGHT = 200
    WIDTH = 400
    X_POS = 100
    Y_POS = 100

    def __init__(self, root):
        """Инициализация приложения,
        создание интерфейса и запуск главного цикла."""
        self.root = root
        self.entries = {}
        root.title(App.TITLE)
        self.center_window(App.WIDTH, App.HEIGHT)
        self.root.resizable(False, False)
        self.setup_ui()
        root.mainloop()

    def center_window(self, wwidth, wheight):
        """Располагает окно по центру
        используя высоту и ширину окна"""
        wpos = dict(zip(("width", "height"),
                        ((ssize - wsize) // 2
                         for wsize, ssize in zip(
                             (wwidth, wheight),
                             (self.root.winfo_screenwidth(),
                              self.root.winfo_screenheight()))
                         )))
        self.root.geometry(f"{wwidth}x{wheight}+{wpos["width"]}+{wpos["height"]}")

    def setup_ui(self):
        """Создание пользовательского интерфейса
        с элементами ввода и кнопкой."""
        for i in range(len(App.LETTERS) + 1):
            self.root.grid_rowconfigure(i, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        for row_, letter in enumerate(App.LETTERS):
            row_ = len(App.LETTERS) if letter == App.LETTERS[-1] else row_
            tk.Label(self.root, text=f"{letter}=").grid(
                row=row_, column=0, padx=10, pady=10, sticky="nsew")
            self.entries[letter] = tk.Entry(self.root)
            self.entries[letter].grid(
                row=row_, column=1, padx=10, pady=10, sticky="nsew")
        self.entries[App.LETTERS[-1]].config(state="readonly")
        tk.Button(text="calculate", command=self.calculate).grid(
            row=len(App.LETTERS) - 1, column=0, sticky="nsew")
        tk.Label(self.root, text=App.FUNC).grid(
            row=len(App.LETTERS) - 1, column=1, sticky="nsew")

    def calculate(self):
        """Рассчитывает результат выражения на основе введённых значений
        и выводит результат в воле вывода"""
        def func(a, b):
            return eval(App.FUNC, {}, {"a": a, "b": b})
        self.entries[App.LETTERS[-1]].config(state="normal")
        self.entries[App.LETTERS[-1]].delete(0, tk.END)
        try:
            self.entries[App.LETTERS[-1]].insert(0, str(func(
                *map(self.get_int_from_entry,
                           App.LETTERS[:-1]))))
        except ValueError:
            self.entries[App.LETTERS[-1]].insert(0, "Error")
        self.entries[App.LETTERS[-1]].config(state="readonly")

    def get_int_from_entry(self, letter):
        """Возвращает значение из поля ввода, преобразованное в int.
        Если поле пустое, возвращает 0."""
        value = self.entries[letter].get()
        return int(value) if value.strip() else 0


if __name__ == "__main__":
    App(tk.Tk())
