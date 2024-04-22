import serial


class LEDControl:
    def __init__(self, port: str = 'COM4', baudrate: int = 9600) -> None:
        self.__serial = serial.Serial(port=port, baudrate=baudrate)

    def on(self) -> None:
        self.__serial.write(int.to_bytes(101, 1, 'big'))

    def off(self) -> None:
        self.__serial.write(int.to_bytes(100, 1, 'big'))

    def set_status(self, status: bool) -> None:
        if status:
            self.on()
        else:
            self.off()

    def set_brightness(self, value: int) -> None:
        self.__serial.write(value.to_bytes(length=1, byteorder='big'))


def main() -> None:
    led = LEDControl()

    run: bool = True
    while run:
        msg = input('>>> ')

        if msg == 'on':
            print('Включаем светодиод')
            led.on()

        elif msg == 'off':
            print('Выключаем светодиод')
            led.off()

        elif 'value' in msg:
            brightness: str = msg.split(' ')[1]
            print(f'Устанавливаем яркость: {brightness}')
            led.set_brightness(int(brightness))

        elif msg == 'exit':
            run = False


if __name__ == '__main__':
    main()
