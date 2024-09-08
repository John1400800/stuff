import tkinter as tk

class App:
    """Приложение для рисования паука с использованием библиотеки tkinter."""
    TITLE = "Сивко Иван. ЛР3 Tkinter GUI. ПМИ-бо-23"
    HEIGHT = 500
    WIDTH = 500

    def __init__(self, root):
        """Инициализация окна приложения, создание холста и рисование паука."""
        self.root = root
        root.title(App.TITLE)
        self.create_canvas(App.WIDTH, App.HEIGHT)
        root.resizable(False, False)
        self.draw_spider()
        root.mainloop()

    def create_canvas(self, wwidth, wheight):
        """Создание холста для рисования в центре экрана."""
        xpos, ypos = map(lambda ss, ws: (ss - ws) // 2,
                          *zip((wwidth, wheight),
                               (self.root.winfo_screenwidth(),
                                self.root.winfo_screenheight())))
        self.root.geometry(f"{wwidth}x{wheight}+{xpos}+{ypos}")
        self.canvas = tk.Canvas(width=wwidth, height=wheight, bg="white")
        self.canvas.pack()
        return self.canvas

    def draw_circle(self, canvas, x, y, radius, color):
        """Рисует круг на холсте."""
        canvas.create_oval(x - radius, y - radius,
                           x + radius, y + radius,
                           fill=color, outline='black')

    def draw_spider(self, canvas=None):
        """Рисует паука на холсте."""
        if canvas is None:
            canvas = self.canvas
        self.draw_circle(canvas, 250, 250, 40, 'black')  # Туловище
        self.draw_circle(canvas, 250, 185, 25, 'black')  # Голова
        canvas.create_line(250, 220, 150, 150, width=6)  # Верхняя левая нога
        canvas.create_line(250, 230, 140, 220, width=6)  # Средняя левая нога
        canvas.create_line(250, 240, 150, 290, width=6)  # Нижняя левая нога
        canvas.create_line(250, 220, 350, 150, width=6)  # Верхняя правая нога
        canvas.create_line(250, 230, 360, 220, width=6)  # Средняя правая нога
        canvas.create_line(250, 240, 350, 290, width=6)  # Нижняя правая нога


if __name__ == "__main__":
    App(tk.Tk())
