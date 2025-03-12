import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

messageNum = []

class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Настройка окна
        self.setWindowTitle("Угадай число!!!")
        self.setGeometry(100, 100, 300, 200)

        # Создание виджетов
        self.label = QLabel("Введите число от 1 до 100: ", self)
        self.input = QLineEdit(self)
        self.button = QPushButton("Проверить", self)
        self.result_label = QLabel("", self)

        # Размещение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # Подключение кнопки к функции
        self.button.clicked.connect(self.check_value)

        # Генерация случайного числа
        self.target_number = random.randint(1, 100)
        self.attempts = 0

    def check_value(self):
        try:
            value = int(self.input.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите целое число!!!s")
            return

        self.attempts += 1
        messageNum.append(value)

        if value < self.target_number:
            self.result_label.setText(f"Загаданное число больше!!! Попытка: {self.attempts}; Прошлые числа {messageNum}")
        elif value > self.target_number:
            self.result_label.setText(f"Загаданное число меньше!!! Попытка: {self.attempts}; Прошлые числа {messageNum}")
        else:
            QMessageBox.information(self, "Победа!!!", f"Вы угадали число за {self.attempts} попыток!!!")
            self.reset_game()

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.setText("")
        self.input.clear()


app = QApplication(sys.argv)
game = GuessNumberGame()
game.show()
sys.exit(app.exec_())