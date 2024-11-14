import turtle

class SpiderApp:
    """Приложение для рисования паука с использованием библиотеки turtle."""
    WIDTH = 500
    HEIGHT = 500

    def __init__(self):
        """Инициализация окна приложения, настройка черепашки и рисование паука."""
        self.screen = turtle.Screen()
        self.screen.setup(width=self.WIDTH, height=self.HEIGHT)
        self.screen.title("Сивко Иван. ЛР3 Turtle GUI. ПМИ-бо-23")
        self.t = turtle.Turtle()
        self.t.speed(1)
        self.draw_spider()
        turtle.done()

    def draw_circle(self, x, y, radius, color):
        """Рисует круг на холсте."""
        self.t.penup()
        self.t.goto(x, y - radius)
        self.t.pendown()
        self.t.color(color)
        self.t.begin_fill()
        self.t.circle(radius)
        self.t.end_fill()

    def draw_line(self, x1, y1, x2, y2, width=6):
        """Рисует линию от одной точки к другой."""
        self.t.penup()
        self.t.goto(x1, y1)
        self.t.pendown()
        self.t.width(width)
        self.t.goto(x2, y2)

    def draw_spider(self):
        """Рисует паука на холсте."""
        self.draw_circle(0, 0, 40, 'black')     # Туловище (центр паука)
        self.draw_circle(0, 65, 25, 'black')    # Голова
        self.draw_line(0, 40, -100, 100)        # Верхняя левая нога
        self.draw_line(0, 30, -110, 30)         # Средняя левая нога
        self.draw_line(0, 30, -110, 0)         # Средняя левая нога
        self.draw_line(0, 20, -100, -50)        # Нижняя левая нога
        self.draw_line(0, 40, 100, 100)         # Верхняя правая нога
        self.draw_line(0, 30, 110, 30)          # Средняя правая нога
        self.draw_line(0, 30, 110, 0)          # Средняя правая нога
        self.draw_line(0, 20, 100, -50)         # Нижняя правая нога

if __name__ == "__main__":
    SpiderApp()

