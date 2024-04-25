import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QSlider, QPushButton
from PyQt5.Qt import Qt

from src import CSS_STYLES, FONT_STYLE
from src import LEDControl


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Управление светодиодом на Arduino Nano v3')
        self.setMinimumSize(400, 200)
        self.setStyleSheet(CSS_STYLES)

        self.__value: int = 0
        self.__status: bool = False

        self.__led_control = LEDControl()

        self.__label_statuses: dict[bool, str] = {
            True: 'On',
            False: 'Off'
        }
        self.__button_statuses: dict[bool, str] = {
            True: 'Turn off',
            False: 'Turn on'
        }

        self.__info_label = QLabel(f"{FONT_STYLE}Value: {self.__value}     Status: {self.__label_statuses[self.__status]}</font>")
        self.__info_label.setAlignment(Qt.AlignCenter)

        # Ползунок установки яркости светодиода
        self.__slider = QSlider()
        self.__slider.setOrientation(Qt.Horizontal)
        self.__slider.valueChanged.connect(self.__slider_value_changed)

        # Кнопка вкл/выкл светодиода
        self.__switch_status_button = QPushButton('Turn on')
        self.__switch_status_button.clicked.connect(self.__switch_status)

        self.__vlayout = QVBoxLayout()
        self.__vlayout.addWidget(self.__info_label)
        self.__vlayout.addWidget(self.__slider)
        self.__vlayout.addWidget(self.__switch_status_button)

        self.__main_v_layout = QVBoxLayout()
        self.__main_v_layout.addLayout(self.__vlayout)
        self.__main_v_layout.setAlignment(Qt.AlignCenter)

        self.setLayout(self.__main_v_layout)

    def __slider_value_changed(self, value: int) -> None:
        self.__value = value
        self.__info_label.setText(f"{FONT_STYLE}Value: {value}     Status: {self.__label_statuses[self.__status]}</font>")

        self.__led_control.set_brightness(value)

    def __switch_status(self) -> None:
        self.__status = not self.__status

        self.__info_label.setText(f"{FONT_STYLE}Value: {self.__value}     Status: {self.__label_statuses[self.__status]}</font>")
        self.__switch_status_button.setText(self.__button_statuses[self.__status])

        self.__led_control.switch_status(self.__status)


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
