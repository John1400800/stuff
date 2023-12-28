import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QFrame
from PyQt5.QtGui import QPainter, QColor, QPen, QImage, QPixmap, QCursor
from PyQt5.QtCore import Qt, QPoint, QTimer, QEvent


class Mand(QMainWindow):
    def __init__(self):
        super().__init__()
        # параметры окна
        self.setFixedSize(600, 400)
        self.setWindowTitle('Mandelbroat')
        # кол-во итераций
        self.max_iteration = 600  # 255
        # Создание палитры
        self.palette = [
            (
                int(255 * math.sin(i / 30.0 + 0.5) ** 2),
                int(255 * math.sin(i / 30.0 + 1.0) ** 2),
                int(255 * math.sin(i / 30.0 + 1.7) ** 2)
            ) for i in range(self.max_iteration - 1)
        ]
        self.palette.append((0, 0, 0))
        #  создаём изображение
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(self.width(), self.height())
        # создание списка изображения
        self.images = [{'params': (-2.0, -1.0, 1.0, 1.0), 'image': None}]
        self.images[-1]['image'] = QImage(self.width(),
                                          self.height(), QImage.Format_ARGB32_Premultiplied)
        # создаём таймер для строчного построителя
        self.mand_timer = QTimer(self)
        self.mand_timer.setInterval(30)
        self.mand_timer.timeout.connect(self.build_mand_line)
        # создание рамки
        self.frame = QFrame(self)
        self.frame.setGeometry(0, 0, 90, 60)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setLineWidth(3)
        self.frame.setStyleSheet('color:blue;')
        self.installEventFilter(self)
        self.mouse_pos = None
        # запускаем построитель
        self.start_build_mand()

    def start_build_mand(self):
        # спрячем рамку
        self.frame.hide()
        # создадим ГЕНЕРАТОР для отрисовки
        self.image_generator = self.mand_color()
        self.mand_timer.start()

    def build_mand_line(self):
        try:
            next(self.image_generator)
            self.image.setPixmap(QPixmap.fromImage(self.images[-1]['image']))
        except StopIteration:
            self.mand_timer.stop()
            # подвинуть рамку в начало
            # показать рамку
            self.frame.show()

    def mand_color(self):
        painter = QPainter()
        painter.begin(self.images[-1]['image'])
        # Комплексное после и его размеры
        xa, ya, xb, yb = self.images[-1]['params']
        # Размеры окна
        img_x, img_y = self.width(), self.height()
        for y in range(img_y):
            #  найдём комплексную ординату точки
            zy = y * (yb - ya) / img_y + ya
            for x in range(img_x):
                #  найдём комплексную абсцису точки
                zx = x * (xb - xa) / img_x + xa
                # Зададим начальные параметры последовательности
                c, z = zx + zy * 1j, 0
                for cnt in range(self.max_iteration):
                    if abs(z) > 2.0:
                        break
                    z = z * z + c
                # Параметры пера / цвета
                pen = QPen(QColor(*self.palette[cnt]), 1)
                painter.setPen(pen)
                painter.drawPoint(QPoint(x, y))
            yield True
        painter.end()

    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            self.frame.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.type() == QEvent.Leave:
            self.frame.setCursor(QCursor(Qt.ArrowCursor))
        elif event.type() == QEvent.MouseButtonPress:
            if event.buttons() == Qt.LeftButton:
                self.frame.setCursor(QCursor(Qt.ClosedHandCursor))
                self.mouse_pos = event.windowPos()
        elif event.type() == QEvent.MouseButtonRelease:
            self.frame.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton:
                # двигаем рамку
                move_vector = event.windowPos() - self.mouse_pos
                new_pos = self.frame.pos() + move_vector
                self.frame.move(int(new_pos.x()), int(new_pos.y()))
                self.move_pos = event.windowPos()
        elif event.type() == QEvent.MouseButtonDblClick:
            if event.buttons() == Qt.LeftButton:
                # вычислить координаты конплесного куска
                old_xa, old_ya, old_xb, old_yb = self.images[-1]['params']
                new_xa = old_xa + self.frame.x() * (old_xb - old_xa) / self.width()
                new_ya = old_ya + self.frame.y() * (old_yb - old_ya) / self.height()
                new_xb = new_xa + self.frame.width() * (old_xb - old_xa) / self.width()
                new_yb = new_ya + self.frame.height() * (old_yb - old_ya) / self.height()
                self.images.append(
                    {'params': (new_xa, new_ya, new_xb, new_yb)})
                # создать и положить в images новую картинку
                self.images[-1]['image'] = QImage(self.width(),
                                                  self.height(), QImage.Format_ARGB32_Premultiplied)
                self.start_build_mand()
            else:
                if len(self.images) > 1:
                    # удалим последний элемент списка и вернём картинку
                    self.images.pop()
                    self.image.setPixmap(
                        QPixmap.fromImage(self.images[-1]['image']))
        return False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    mand = Mand()
    mand.show()
    sys.exit(app.exec())
