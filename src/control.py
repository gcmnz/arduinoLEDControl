import serial


class LEDControl:
    def __init__(self, port: str = 'COM4', baudrate: int = 9600) -> None:
        self.__serial = serial.Serial(port=port, baudrate=baudrate)

    def __on(self) -> None:
        self.__serial.write(int.to_bytes(101, 1, 'big'))

    def __off(self) -> None:
        self.__serial.write(int.to_bytes(100, 1, 'big'))

    def switch_status(self, status: bool) -> None:
        if status:
            self.__on()
        else:
            self.__off()

    def set_brightness(self, value: int) -> None:
        self.__serial.write(value.to_bytes(length=1, byteorder='big'))
